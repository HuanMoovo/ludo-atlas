# -*- coding: utf-8 -*-
"""把仓库 Markdown 汇总为 VitePress 内容目录。

规则:
- 拷贝 docs/ resources/ playbooks/ templates/ 与 GLOSSARY.md。
- README.md 重命名为 index.md（目录首页）。
- 正文中 .../README.md 形式的链接改写为目录链接。
"""
import os
import re
import shutil

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(REPO, 'site')
OUT = os.path.join(SITE, 'content')


def _rep(m):
    return '](' + (m.group(1) or './') + ')'


def rewrite(text: str) -> str:
    return re.sub(r'\]\(([^)]*?)README\.md\)', _rep, text)


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copyfile(os.path.join(SITE, 'home.md'), os.path.join(OUT, 'index.md'))
    for src_rel in ['docs', 'resources', 'playbooks', 'templates']:
        src = os.path.join(REPO, src_rel)
        for dirpath, dirs, files in os.walk(src):
            for fn in files:
                if not fn.endswith('.md'):
                    continue
                rel = os.path.relpath(os.path.join(dirpath, fn), REPO)
                name = 'index.md' if fn == 'README.md' else fn
                dst = os.path.join(OUT, os.path.dirname(rel), name)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                text = open(os.path.join(dirpath, fn), encoding='utf-8').read()
                open(dst, 'w', encoding='utf-8', newline='\n').write(rewrite(text))
    for extra in ['GLOSSARY.md']:
        s = os.path.join(REPO, extra)
        if os.path.exists(s):
            shutil.copyfile(s, os.path.join(OUT, extra.lower()))
    print('content ready:', sum(len(fs) for _, _, fs in os.walk(OUT)), 'files')


if __name__ == '__main__':
    main()
