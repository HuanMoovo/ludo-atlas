# -*- coding: utf-8 -*-
"""把仓库 Markdown 汇总为 MkDocs 内容目录（site/build），供 Material 主题构建。

流程：python site/prepare.py → mkdocs build（配置见仓库根 mkdocs.yml）。

规则：
- 拷贝 docs/ resources/ playbooks/ templates/ examples/ 的 Markdown。
- README.md 重命名为 index.md（目录首页），正文中 .../README.md 链接改写为目录链接。
- 拷贝根文件（术语表、贡献指南、路线图、更新日志、许可）与品牌 logo。
- 由 site/home.md 生成首页 index.md，并注入当前文档统计。
"""
import os
import re
import shutil

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(REPO, 'site')
OUT = os.path.join(SITE, 'build')

COPY_DIRS = ['docs', 'resources', 'playbooks', 'templates', 'examples']
COPY_FILES = ['GLOSSARY.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md', 'GOVERNANCE.md',
              'CHANGELOG.md', 'LICENSE', 'LICENSE-CODE']
COUNT_DIRS = ['docs', 'resources', 'playbooks', 'templates']


def _rep(m):
    """README.md 链接 → index.md 链接（保留锚点）；外链不动。"""
    if m.group(1).startswith(('http://', 'https://')):
        return m.group(0)
    return '](' + (m.group(1) or '') + 'index.md' + (m.group(2) or '') + ')'


def _rep_dir(m):
    """templates/ → doc-templates/（MkDocs 默认排除 docs 根级 /templates/ 目录）。"""
    prefix = m.group(1)
    if '://' in prefix:
        return m.group(0)
    if not (prefix == '' or prefix.endswith('/')):
        return m.group(0)
    return '](' + prefix + 'doc-templates/'


def rewrite(text: str) -> str:
    text = re.sub(r'\]\(([^)]*?)README\.md(#[^)]*)?\)', _rep, text)
    text = re.sub(r'\]\(([^)]*?)templates/', _rep_dir, text)
    return text


def _stats():
    """文档数（≥60 行的 md）、总字数（万）、类型数、引擎轨道数。"""
    files = []
    for d in COUNT_DIRS:
        for dirpath, _, fs in os.walk(os.path.join(OUT, d)):
            files += [os.path.join(dirpath, f) for f in fs
                      if f.endswith('.md') and not re.search(r'\.(?:en|ja)\.md$', f)]
    glossary = os.path.join(OUT, 'GLOSSARY.md')
    if os.path.exists(glossary):
        files.append(glossary)
    texts = [open(f, encoding='utf-8').read() for f in files]
    n = sum(1 for t in texts if t.count('\n') >= 60)
    w = round(sum(len(t) for t in texts) / 10000, 1)
    genres_dir = os.path.join(OUT, 'docs', 'genres')
    engines_dir = os.path.join(OUT, 'docs', 'engines')
    g = len([x for x in os.listdir(genres_dir) if os.path.isdir(os.path.join(genres_dir, x))])
    e = len([x for x in os.listdir(engines_dir) if os.path.isdir(os.path.join(engines_dir, x))])
    return n, w, g, e


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    # 1) 正文目录（只收 Markdown；README.md → index.md，链接同步改写）
    n_md = 0
    for src_rel in COPY_DIRS:
        src = os.path.join(REPO, src_rel)
        for dirpath, dirs, fs in os.walk(src):
            dirs[:] = [d for d in dirs if d not in ('__pycache__', 'node_modules')]
            for fn in fs:
                if not fn.endswith('.md'):
                    continue
                rel = os.path.relpath(os.path.join(dirpath, fn), REPO)
                parts = rel.split(os.sep)
                if parts[0] == 'templates':
                    parts[0] = 'doc-templates'
                    rel = os.sep.join(parts)
                mm = re.fullmatch(r'README\.(en|ja)\.md', fn)
                if fn == 'README.md':
                    name = 'index.md'
                elif mm:
                    name = 'index.' + mm.group(1) + '.md'
                else:
                    name = fn
                dst = os.path.join(OUT, os.path.dirname(rel), name)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                text = open(os.path.join(dirpath, fn), encoding='utf-8').read()
                open(dst, 'w', encoding='utf-8', newline='\n').write(rewrite(text))
                n_md += 1

    # 2) 根文件（供“关于”板块与站内引用；Markdown 同样做链接改写）
    for fn in COPY_FILES:
        s = os.path.join(REPO, fn)
        if not os.path.exists(s):
            continue
        dst = os.path.join(OUT, fn)
        if fn.endswith('.md'):
            text = open(s, encoding='utf-8').read()
            open(dst, 'w', encoding='utf-8', newline='\n').write(rewrite(text))
        else:
            shutil.copyfile(s, dst)

    # 3) 资产：logo 与自定义样式
    shutil.copyfile(os.path.join(REPO, 'assets', 'logo.svg'), os.path.join(OUT, 'logo.svg'))
    shutil.copyfile(os.path.join(SITE, 'styles', 'extra.css'), os.path.join(OUT, 'extra.css'))

    # 4) 首页（注入统计；支持 site/home.en.md 英文版）
    n, w, g, e = _stats()
    stats_by_locale = {
        '': f'{n} 份中文文档 · 约 {w} 万字 · {g} 类类型手册 · {e} 条引擎轨道',
        '.en': f'{n} documents · ~{round(w * 10)}k characters · {g} genre handbooks · {e} engine tracks',
    }
    for loc, stats in stats_by_locale.items():
        src = os.path.join(SITE, 'home%s.md' % loc)
        if not os.path.exists(src):
            continue
        home = open(src, encoding='utf-8').read().replace('{{STATS}}', stats)
        open(os.path.join(OUT, 'index%s.md' % loc), 'w', encoding='utf-8', newline='\n').write(home)
        print(f'  home[{loc or "zh"}] -> index{loc}.md')

    print(f'content ready: {n_md} md files; stats: {stats_by_locale[""]}')


if __name__ == '__main__':
    main()
