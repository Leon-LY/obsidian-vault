---
title: Obsidian 首页设计
type: concept
tags: [技能/需求分析, 技能/技术方案]
status: reviewed
graph_visible: true
created: 2026-06-10
updated: 2026-06-10
related:
  - Obsidian第二大脑
  - Obsidian插件推荐
source: 笔记同步助手 小红书文章
---

# Obsidian 首页设计

> 一句话：首页不是装饰目录，而是每天进入知识库的第一张桌面——操作台 + 洞察镜 + 快捷入口。

## 四种实现方案对比

| 方案 | 难度 | 布局自由度 | 优点 | 缺点 |
|------|------|-----------|------|------|
| **Components 插件** | ⭐ | 极高 | Notion 风格、固定侧栏、按钮/看板/热力图原生组件 | 需要装插件，部分组件需学习 |
| Dataview 动态查询 | ⭐ | 中 | 纯查询无需 CSS，vault 内数据任意聚合 | 只有列表/表格，无 UI 组件 |
| Dataview + CSS 片段 | ⭐⭐ | 中高 | 卡片布局 + 视觉优化，当前首页方案 | CSS 调试耗时 |
| HTML + CSS 自定义 | ⭐⭐⭐ | 最高 | 完全掌控布局和样式 | 排查兼容性需要经验 |

> 当前首页采用方案 3（Dataview + CSS），未来可考虑迁移到 Components 插件获得更多交互能力。

## Components 插件方案（2026 年新趋势）

来源：小红书@乌贼不想跳舞，[原文链接](http://xhslink.com/o/Aab1pXyRdsC)

### 整体布局（Notion 风格）

Components 插件可以让 Obsidian 实现类似 Notion 的页面体验：

```
┌──────┬──────────────────────────┬──────┐
│ 左侧  │                         │ 右侧  │
│ 导航栏 │     主页内容区域         │ 本周  │
│ 固定  │  · 统计数字 · 四个按钮    │ 任务  │
│      │  · 任务看板 · 热力图      │ 看板  │
│ 快捷  │                         │ 固定  │
│ 跳转  │                         │      │
└──────┴──────────────────────────┴──────┘
```

- **左侧导航栏**：独立文档，固定位置，可快速跳转到首页、阅读库、影音库等
- **右侧任务区**：本周任务文档，固定位置，实时查看进度和复盘
- **中央主页**：组件自由组合

### 核心组件

| 组件 | 实现方式 | 用途 |
|------|----------|------|
| 统计数字 | 从日记属性抓取，点击可跳转 | 日记数量、阅读数量等可视化 |
| 时间展示 | Components 内置 | 顶部实时时间显示 |
| 灵感卡片 | 按钮 → 新建卡片 → 标记"未整理" | 卡片笔记法，方便后续复盘 |
| 接日记 | 按钮 → 打开/自动创建今日日记 | 快速进入日记 |
| 任务看板 | 新建任务 → 看板自动更新 → 进度条 | 支持分类（work/creation）和状态（未开始/进行中/已完成） |
| 热力图 | 从日记属性抓取 | 点击任意格子跳转到对应日期日记 |

### 与本 vault 的适配度

| 功能 | 当前首页 | Components 可实现 |
|------|----------|-------------------|
| 固定侧栏导航 | ❌ | ✅ 左侧快捷跳转 |
| 本周任务看板 | ❌ | ✅ 进度条 + 拖拽 |
| 热力图 | ❌ | ✅ 日记关联 |
| 卡片笔记 | ❌ | ✅ 灵感卡片 |
| 一键接日记 | ❌ | ✅ 自动创建 |
| 知识分类卡片 | ✅ 表格 | 可保留 |

## 核心理念（不变）

首页应该同时做到三件事：
1. **让我愿意打开** — 视觉和体验上让人想用
2. **让我快速进入状态** — 今天要做什么、最近关注什么
3. **让我知道下一步该做什么** — 落到行动建议，不空转

## CSS 隔离技巧
```css
.knowledge-home .markdown-preview-section {
  width: min(100%, 1360px) !important;
}
```

## 核心参考来源

- **Components 方案**：[小红书@乌贼不想跳舞](http://xhslink.com/o/Aab1pXyRdsC) — Components 插件实现 Notion 风格首页
- **Neon Homepage**：[HOCA-1/neon-homepage-vault](https://github.com/HOCA-1/neon-homepage-vault)
- **XDA 教程**：[Dataview 实时仪表盘](https://www.xda-developers.com/used-obsidians-dataview-plugin-live-dashboard/)
- **中文论坛**：[分享首页布局和实现方式](https://forum-zh.obsidian.md/t/topic/55028)

## 关联笔记

- [[Obsidian第二大脑]] — 知识管理体系的总纲
- [[Obsidian Components插件]] — Components 详细实操指南（六步上手）
- [[Obsidian主题美化]] — 主题与界面美化定制
- [[Obsidian插件推荐]] — Dataview / Components 等首页必备插件
- [[首页]] — 本 vault 当前的首页实现
