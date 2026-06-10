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
- [[ClaudeDesign学习笔记]] — Claude Design 生成高颜值 PPT

---

## 新增：goal/loop/batch/simplify/debug 命令体系

> 来源：[[笔记同步助手/2026-06-10/让 Claude Code 趁你睡觉就把活干完的命令 - 学习笔记\|学习笔记]]，详见原文

### 命令速查

| 命令 | 用途 | 核心场景 |
|------|------|----------|
| **goal** | 设定完成条件，自动判断是否终止 | "测试全部通过，退出码 0，不改其他文件" |
| **auto mode** | 减少单轮内工具确认次数 | 配合 goal 实现真正无人值守 |
| **loop** | 按计划轮询外部状态变化 | 部署还在跑、长构建未结束、等集成测试结果 |
| **batch** | 大任务拆成 5-30 个独立单元并行执行 | 框架迁移、批量模块改造 |
| **simplify** | 改动后代码清理优化 | 提交前清理：复用 helper、简化逻辑、检查效率 |
| **debug/doctor** | CLI 自身问题诊断 | 先 doctor（跑不起来），后 debug（时灵时不灵） |

### 关键心法

- **goal 是核心**：条件不能太虚。"修好 bug"不行，要写成"test.ts 测试全过，npm test 退出码 0"。最多写 4000 字符，可包含安全阀（最多 20 轮/30 分钟停）
- **自主 ≠ 不管**：前提是你先把终点定义清楚。spec 清楚+验证硬 → 睡一觉代码写好；spec 错+验证松 → 高效产出方向全错的代码
- **batch 最大风险在拆分**：认真审它拆出来的计划（边界/依赖/文件范围），没看明白别批准
- **simplify 不再查 correctness bug**：从 v2.1.154 起，bug 查改用 `code review`，simplify 仅做提交前清理
