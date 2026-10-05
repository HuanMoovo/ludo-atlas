# -*- coding: utf-8 -*-
"""MkDocs hook：构建时按目录结构与索引页顺序生成全站导航（nav）。

约定：
- 每个目录的 index.md 即该目录首页；子目录按所在父级 index.md 中链接出现顺序排列，其余按名称排序。
- 导航标题取文档 H1：形如「Ludo Atlas · X · Y」取末段；含「 — 」取后半；含「 · 」取前半。
"""

import os
import re


def _read(path):
    try:
        with open(path, encoding='utf-8') as f:
            return f.read()
    except OSError:
        return ''


def _h1(path):
    m = re.search(r'^#\s+(.+?)\s*$', _read(path), re.M)
    return m.group(1).strip() if m else os.path.basename(os.path.dirname(path))


def _short(title):
    t = title
    if t.startswith('Ludo Atlas'):
        # 只在括号外按「·」切段取末段（括号内的「·」属于说明文字）
        parts, cur, depth = [], '', 0
        for ch in t:
            if ch == '（':
                depth += 1
            elif ch == '）':
                depth = max(0, depth - 1)
            if ch == '·' and depth == 0:
                parts.append(cur)
                cur = ''
            else:
                cur += ch
        parts.append(cur)
        parts = [p.strip() for p in parts if p.strip()]
        t = parts[-1]
    # 形如「游戏简史（领域史 · 技术史 · 代表作品）」的枚举式括号说明不进短标题
    m = re.match(r'^([^（]{4,})（[^）]*·[^）]*）$', t)
    if m:
        t = m.group(1).strip()
    if ' — ' in t:
        t = t.split(' — ')[-1].strip()
    elif ' · ' in t:
        t = t.split(' · ')[0].strip()
    return t


def _label(base, rel_md):
    return _short(_h1(os.path.join(base, rel_md)))


def _order(base, index_rel):
    """从索引页中解析链接顺序：子目录（x/README.md）与同目录文件（x.md）。"""
    t = _read(os.path.join(base, index_rel))
    dirs, files = [], []
    for m in re.finditer(r'\]\(([a-z0-9\-]+)/(?:README|index)\.md\)', t):
        if m.group(1) not in dirs:
            dirs.append(m.group(1))
    for m in re.finditer(r'\]\(([a-z0-9\-]+\.md)\)', t):
        if m.group(1) not in files:
            files.append(m.group(1))
    return dirs, files


def _node(base, rel):
    """目录 → 导航节点；叶子目录（仅 index.md）返回 {label: path}。"""
    ab = os.path.join(base, rel)
    idx = f'{rel}/index.md'
    has_idx = os.path.exists(os.path.join(base, idx))
    subdirs = sorted(d for d in os.listdir(ab)
                     if os.path.isdir(os.path.join(ab, d)) and not d.startswith('.'))
    files = sorted(f for f in os.listdir(ab)
                   if f.endswith('.md') and f != 'index.md'
                   and not re.search(r'\.(?:en|ja)\.md$', f))
    d_order, f_order = _order(base, idx) if has_idx else ([], [])
    label = _label(base, idx) if has_idx else rel.split('/')[-1]
    if not subdirs and not files:
        return {label: idx}
    kids = []
    if has_idx:
        kids.append({label: idx})
    for d in [x for x in d_order if x in subdirs] + [x for x in subdirs if x not in d_order]:
        kids.append(_node(base, f'{rel}/{d}'))
    for f in [x for x in f_order if x in files] + [x for x in files if x not in f_order]:
        kids.append({_label(base, f'{rel}/{f}'): f'{rel}/{f}'})
    return {label: kids}


def _section(base, rel, label=None):
    node = _node(base, rel)
    if label:
        key = next(iter(node))
        return {label: node[key]}
    return node


def build_nav(base):
    def _have(rel):
        return os.path.exists(os.path.join(base, rel))

    nav = [{'首页': 'index.md'}]
    if _have('docs/preface.md'):
        nav.append({'前言': 'docs/preface.md'})
    nav.append({'总目录': 'docs/index.md'})
    for rel, label in [
        ('docs/start', '入门'),
        ('docs/fundamentals', '基础学科'),
        ('docs/genres', '类型手册'),
        ('docs/engines', '引擎轨道'),
        ('docs/pipelines', '管线与工作流'),
        ('docs/ai', 'AI 工作流'),
        ('docs/teams', '团队与规模'),
        ('docs/publishing', '发行与商业化'),
    ]:
        if _have(f'{rel}/index.md'):
            nav.append(_section(base, rel, label))
    if _have('docs/pitfalls/index.md') and _have('docs/postmortems/index.md'):
        nav.append({'避坑与复盘': [_node(base, 'docs/pitfalls'), _node(base, 'docs/postmortems')]})
    if _have('resources/index.md'):
        nav.append(_section(base, 'resources', '资源大全'))
    if _have('playbooks/index.md'):
        nav.append(_section(base, 'playbooks', '实践手册'))
    if _have('doc-templates/index.md') and _have('examples/index.md'):
        nav.append({'模板与示例': [_node(base, 'doc-templates'), _node(base, 'examples')]})
    about = []
    if _have('docs/meta/index.md'):
        about += list(_node(base, 'docs/meta').values())[0]
    for f in ['GLOSSARY.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md', 'GOVERNANCE.md', 'CHANGELOG.md']:
        if _have(f):
            about.append({_label(base, f): f})
    if about:
        nav.append({'关于': about})
    return nav


def on_config(config):
    config['nav'] = build_nav(config['docs_dir'])
    return config
