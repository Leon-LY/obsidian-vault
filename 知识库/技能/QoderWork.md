---
title: QoderWork
type: concept
tags: [技能/AI工具, 技能/全栈开发]
status: draft
graph_visible: true
created: 2026-06-10
related:
  - 全栈开发学习路线
  - ClaudeCode学习指南
source: 笔记同步助手 微信公众号文章
---

# QoderWork — AI 设计工作台

> 一句话：阿里出品的 AI 设计工具，用自然语言做可交付的专业设计，直接输出前端工程代码，实现"设计即代码"。

## 概述

QoderWork Design Desk 是阿里 QoderWork 团队推出的 AI 设计工作台。定位是用自然语言做出可交付的专业设计，从想法到工程级产物，中间不需要 Figma。

核心亮点：
- **140 种风格参考** — Airbnb、Apple、Figma 等内置风格，选定即锚定设计语言
- **画笔标注修改** — 直接在画布上圈区域写需求，AI 识别并修改
- **Nudge 微调面板** — 对颜色、间距、圆角、布局等参数精细调整，拉滑块即可
- **Handoff to Qoder** — 设计一键转为 React + Vite 前端工程，在 Qoder IDE 中继续开发
- **本地桌面端** — 不依赖海外服务，支持语音输入

## 与 Claude Design 的对比

| 维度 | QoderWork Design | Claude Design |
|------|-----------------|---------------|
| 风格控制 | 140 种风格参考 + Nudge 微调 | 全靠 prompt 描述 |
| 修改方式 | 画笔标注 + 拉滑块 | 重新描述需求 |
| 产出格式 | React + Vite 工程文件 | 单个 HTML 文件 |
| 部署方式 | 本地桌面端 | 海外服务依赖 |
| 适用场景 | 组件密集型页面、SaaS、看板 | 快速原型、单页面 |

## 它的意义

QoderWork 代表的趋势是：**"设计"和"前端"之间的边界正在被 AI 抹掉。** 设计师和开发者操作同一份文件，不存在"交付"环节，设计文件变成了团队一起维护的代码资产。

## 相关链接

- [QoderWork 官网](https://www.qoderwork.ai)
- [Token Farm Dashboard（文中案例）](https://qwwzdyj.github.io/token-farm-dashboard/)

## 关联笔记

- [[全栈开发学习路线]] — 前端工程化是学习路线的一部分
- [[ClaudeCode学习指南]] — 与 Claude Design/AI 编程工具的对比
