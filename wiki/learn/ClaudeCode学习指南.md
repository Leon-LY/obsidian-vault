---
title: Claude Code 学习指南
type: concept
tags: [技能/AI工具, 技能/项目管理]
status: draft
created: 2026-06-09
related:
  - Obsidian第二大脑
  - 全栈开发学习路线
---

# Claude Code 学习指南

> 一句话：Claude Code 是 Anthropic 的终端原生 AI 编程助手，本页汇总官方文档和社区精华资源。

## 官方文档（首选）

- **[Claude Code 高级用户技巧（中文）](https://support.claude.com/zh-CN/articles/14554000-claude-code-%E9%AB%98%E7%BA%A7%E7%94%A8%E6%88%B7%E6%8A%80%E5%B7%A7)** — Anthropic 官方必读
- **[Skills 官方文档](https://code.claude.com/docs/en/skills.md)** — 自定义命令和技能的完整规范
- **[Best Practices 参考](https://github.com/xobotyi/cc-foundry/blob/master/plugins/ai-helpers/skills/claude-code-sdk/references/best-practices.md)** — 上下文管理、策略、扩展机制选择

## 社区精华指南

| 资源 | 推荐理由 |
|------|----------|
| **[Ultimate Guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide)** | ⭐ 最推荐。6 个月实战，48 张图、271 题测验、181 模板 |
| **[Best Practices](https://github.com/MuhammadUsmanGM/claude-code-best-practices)** | 持续更新至 2026.05，11 个 CLAUDE.md 模板 |
| **[Field Guide](https://github.com/lawwu/claude-code-field-guide)** | 一线实践，不玩概念全是实操 |
| **[45 Tips](https://github.com/ykdojo/claude-code-tips)** | 45 条实用技巧（语音输入、容器化、上下文管理） |
| **[基础指南](https://github.com/roeyw5/claude-code-guide)** | 新手友好，从安装到高级配置 |

## 核心心法

| 原则 | 说明 |
|------|------|
| **验证第一** | 永远给 Claude 检验自己工作的方式（测试、截图、linter） |
| **上下文纪律** | 每换任务就 `/clear`；上下文是最稀缺的资源 |
| **CLAUDE.md 当代码维护** | 每次纠正后立即更新，提交到 git |
| **Plan Mode 先行** | 跨多文件或不确定怎么做时，先计划模式 |
| **Skills > MCP** | 优先 CLI 和 skill，少挂 MCP 服务器（省上下文） |
| **子代理隔离** | 调研/验证交给子代理，主上下文保持干净 |
| **Worktree 并行** | git worktree 同时跑 3-5 个会话 |

## 技能与命令体系

### 目录结构

```
project/
├── .claude/
│   ├── commands/         # /xxx 斜杠命令
│   ├── skills/           # SKILL.md 技能包
│   ├── agents/           # 子代理
│   └── settings.json     # hooks / MCP / 权限
└── CLAUDE.md             # 项目级全局指令
```

用户级在 `~/.claude/` 同样结构。

### 自定义命令（.md 文件）

```markdown
# .claude/commands/review-pr.md
Analyze the diff of the current PR and check:
1. Security vulnerabilities
2. Missing tests
3. Compliance with conventions ($ARGUMENTS)
```

- `$ARGUMENTS` 做动态参数
- `/review-pr` 或 `/review-pr security` 调用

### Skills 前文 YAML

```yaml
---
name: api-endpoint
description: 按项目规范生成 REST API 端点
---
```

关键字段：`name` / `description` / `when_to_use` / `allowed-tools` / `context: fork`（子代理隔离）/ `model` / `effort`（low~max）

### 配置模板（可直接抄）

- **[claude-code-config](https://github.com/jarrodwatts/claude-code-config)** — 全套配置（rules/hooks/agents/skills）
- **[claude-spellbook](https://github.com/kid-sid/claude-spellbook)** — 64 skill + 18 command + 7 agent 合集

## 关联笔记

- [[Obsidian第二大脑]] — 知识管理与 AI 工具的协同
- [[全栈开发学习路线]] — 编程学习路径
