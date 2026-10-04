import { defineConfig } from 'vitepress'

const REPO = 'https://github.com/HuanMoovo/gamedev-atlas'

export default defineConfig({
  lang: 'zh-CN',
  title: 'GameDev Atlas',
  description: '游戏开发全景手册：类型流程 × 开源工具链 × 学习资源 × AI 工作流',
  srcDir: 'content',
  cleanUrls: true,
  ignoreDeadLinks: true,
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '文档索引', link: '/docs/' },
      { text: '资源大全', link: '/resources/' },
      { text: 'GitHub', link: REPO },
    ],
    search: { provider: 'local' },
    socialLinks: [{ icon: 'github', link: REPO }],
    outline: { level: [2, 3], label: '本页目录' },
    docFooter: { prev: '上一篇', next: '下一篇' },
    footer: {
      message: '文档 CC BY-SA 4.0 · 代码 MIT',
      copyright: 'GameDev Atlas 社区维护',
    },
  },
})
