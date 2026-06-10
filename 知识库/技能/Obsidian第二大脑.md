---
title: Obsidian 第二大脑
type: concept
tags: [技能/知识管理, 技能/项目管理]
status: draft
created: 2026-06-09
related:
  - ClaudeCode学习指南
  - 全栈开发学习路线
  - 爱山东APP
---

# Obsidian 第二大脑

> 一句话：基于 Markdown 和双向链接的个人知识管理系统，本 Vault 就是它的实践。

## 核心理念

### CODE 方法论
- **Capture（捕获）** — 随手记到 Inbox/
- **Organize（组织）** — 转成结构化笔记
- **Distill（提炼）** — 提取核心概念、建立链接
- **Express（表达）** — 输出方案、周报、文章

### PARA 分类法
- **P**rojects — 活跃项目（本 vault 的 projects/）
- **A**reas — 关注领域（本 vault 的 wiki/concepts/）
- **R**esources — 参考素材（本 vault 的 raw/）
- **A**rchives — 归档

## 本 Vault 的实践

详见 [[CLAUDE.md]]，核心结构：

| 文件夹 | 用途 |
|--------|------|
| `raw/` | 原始素材 |
| `Inbox/` | 零散想法 |
| `wiki/` | 结构化知识（概念/实体/对比/问题） |
| `output/` | AI 产出文档 |
| `projects/` | 活跃项目 |

## 必装插件栈（2025-2026 共识）

| 插件 | 用途 |
|------|------|
| **Dataview** | 像数据库一样查询笔记 |
| **Tasks** | 任务管理 |
| **Templater** | 高级模板 |
| **Calendar** | 日期导航 |
| **Copilot / Local LLM** | AI 辅助总结、打标签、发现关联 |

## 社区资源

- **[Minimal Second Brain](https://github.com/gokhanarkan/minimal-second-brain)** — 极简 AI 原生 Vault。3 文件夹、零模板，Claude Code 友好，含 MANIFEST.md
- **[LLM-Maintained Second Brain](https://github.com/NicholasSpisak/second-brain)** — 基于 Karpathy 的 LLM Wiki 模式：raw/ → LLM → wiki — 跟本 vault 的模式几乎一样！
- **[Open Second Brain (MCP)](https://mcpserver.space/mcp/open-second-brain/)** — AI 交互记录为 .md，每晚"做梦"整合
- **[2年+经验总结](https://nicolas.lienart.net/blog/obsidian-review/)** — 4000+ 笔记，建议：一个 vault 管所有、多用别名、内部链接 > 标签
- **[Obsidian Sync 建 Wiki](https://digitechbytes.com/digital-lifestyle-productivity/second-brain-obsidian-sync/)**

## Dataview 开发入门

```
// 插件中获取 Dataview API
const dvApi = app.plugins.plugins.dataview.api;

// 查询带标签的页面
const pages = dvApi.pages("#重要");

// 执行 DQL 查询
const result = await dvApi.query("LIST FROM #项目/进行中");
```

**核心方法**：`dv.pages()` / `dv.page()` / `dv.query()` / `dv.table()` / `dv.list()` / `dv.taskList()`

**注意**：插件 API 没有 `.el()` / `.header()` 等渲染方法——那些只在 `dataviewjs` 代码块中可用。

## 同类参考

- [[ClaudeCode学习指南]] — AI 辅助编程工具
- [[全栈开发学习路线]] — 编程学习路径
