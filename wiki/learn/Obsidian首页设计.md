---
title: Obsidian 首页设计
type: concept
tags: [技能/需求分析, 技能/技术方案]
status: draft
created: 2026-06-10
updated: 2026-06-10
related:
  - Obsidian第二大脑
  - Obsidian插件推荐
source: 笔记同步助手 小红书文章
---

# Obsidian 首页设计

> 一句话：首页不是装饰目录，而是每天进入知识库的第一张桌面——操作台 + 洞察镜 + 快捷入口。

## 核心理念

首页应该同时做到三件事：
1. **让我愿意打开** — 视觉和体验上让人想用
2. **让我快速进入状态** — 今天要做什么、最近关注什么
3. **让我知道下一步该做什么** — 落到行动建议，不空转

首页定位：**不是目录，而是工作流入口。**

## 经典布局

参考成熟方案，首页通常分三个区域：

### 首屏（Splash）
- 背景图 + 标题 + 副标题，建立进入感
- 快捷按钮：今日日记、AI洞察
- 风格参考：绿植工作台、霓虹 Dashboard、极简信息流

### 操作台（Dashboard）
- **今日行动** — 今天真正要推进的事情
- **今日输入** — 今天吸收了什么（文章、会议、资料）
- **今日输出** — 今天真正产出了什么

比单纯 TodoList 更有价值：提醒你今天不是只要忙，而是确认有没有形成输出。

### 洞察镜（Insight Mirror）
AI 根据最近日记、工作笔记、学习笔记生成的七维洞察：
1. 总览
2. 潜意识偏好
3. 被遗忘的内容
4. 认知盲区
5. 热点趋势
6. 注意力热力图
7. 行动建议

每张卡片：洞察标题 + 一句话结论 + 关键词标签 + 查看详情入口。

## 实现技术栈

| 方案 | 难度 | 适用场景 |
|------|------|----------|
| Dataview 动态查询 | ⭐ | 入门，纯查询无需 CSS |
| Dataview + CSS 片段 | ⭐⭐ | 中等，卡片布局 + 视觉优化 |
| HTML + CSS 自定义 | ⭐⭐⭐ | 高阶，完全掌控布局和样式 |
| AI 生成首页 | ⭐ | 让 AI 帮你写 CSS，抄作业改 |

### CSS 隔离技巧
首页专属 class，不影响其他笔记：
```yaml
---
cssclasses:
  - knowledge-home
---
```
```css
.knowledge-home .markdown-preview-section {
  width: min(100%, 1360px) !important;
  max-width: none !important;
}
```

### 文件结构推荐
```
首页.md          — 页面结构（首屏 + 操作台 + 洞察镜 + 快捷入口）
AI洞察/当日.md   — AI 生成的七维洞察内容（每天更新）
.obsidian/snippets/ — CSS 样式文件
```

## 核心参考来源

- **小红书文章**：《Obsidian首页太简陋？我用AI给自己做了一个个人知识工作台》
- **Neon Homepage**：[HOCA-1/neon-homepage-vault](https://github.com/HOCA-1/neon-homepage-vault) — 霓虹风格仪表盘
- **模块化仪表盘**：[JiaoTangXQ/obsidian-theme](https://github.com/JiaoTangXQ/obsidian-theme) — 纯 Dataview 实现
- **XDA 教程**：[Dataview 实时仪表盘](https://www.xda-developers.com/used-obsidians-dataview-plugin-live-dashboard/)
- **中文论坛**：[分享首页布局和实现方式](https://forum-zh.obsidian.md/t/topic/55028)

## 关联笔记

- [[Obsidian第二大脑]] — 知识管理体系的总纲
- [[Obsidian插件推荐]] — Dataview 等首页必备插件
- [[首页]] — 本 vault 当前的首页实现

## 开放问题

- 如何让 AI 洞察真正本地化运行（不依赖外部 API）？
- 首页数据量的平衡点——多少信息是恰到好处？
