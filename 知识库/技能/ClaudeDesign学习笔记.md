---
title: Claude Design 学习笔记
type: concept
tags: [技能/AI工具]
status: draft
source: 笔记同步助手/2026-06-10/全面掌握 Claude Design：可交互可编辑PPT学习笔记.md
created: 2026-06-10
updated: 2026-06-10
---

# Claude Design

> 一句话：通过对话生成高质量可交互 HTML PPT 的 AI 设计工具，Opus 4.7 视觉能力驱动，审美断档领先。

## 概述

Claude Design 是 Anthropic 推出的 AI 设计类产品，专门通过对话生成设计稿（PPT/网页），核心优势在于：
- **审美碾压**：Opus 4.7 视觉能力比上一代提升 13 个百分点，且 Claude Design 对视觉能力的使用方式与其他 Agent 不同——同样接入 Opus 4.7 的 Claude Code 无法达到同样效果
- **HTML 可交互**：生成的是 HTML 页面，可利用互联网几十年的开源库积累
- **四种编辑方案**：Edit / Comet / Twix / Draw

## 核心能力矩阵

### 一、动态视觉资源

| 库 | 用途 | PPT 场景 |
|---|------|----------|
| **3GS / Three.js** | 前端 3D 渲染库 | 分子结构模型课件 |
| **Matter.js** | 2D 物理引擎 | 自由落体物理课件 |
| **ECharts** | 数据可视化图表库 | 3D 可交互图表分析 PPT |
| **Spline** | 3D 设计平台 | 导入 3D 效果链接生成动态 PPT（如旋转地球） |

此外还可调用：地图库、金融 K 线、代码展示、复杂公式等。

### 二、四种编辑方案

| 功能 | 操作方式 | 适用场景 |
|------|----------|----------|
| **Edit** | 手动输入参数（字号/字重/行间距/不透明度） | 传统 PPT 式精调 |
| **Comet** | 选中元素 + 提示词精准控制 | "把宽度调成两倍" |
| **Twix** | 预埋调节控件（圆角弧度/主题配色） | 需要实时预览的参数 |
| **Draw** | 手绘圈选 + 文字说明 | 懒人快速标注 |

### 三、进阶技巧

- **Figma 像素级精修**：安装 HTML2Design 插件 → 导入 Figma → 无限缩放精修
- **演讲翻页绑定**：对话将演示流程与翻页笔按键绑定，图表自动停在预设观察位

## 局限

- 偶尔添加多余英文元素
- 与 Claude Code 生态结合还不紧密
- 生成的网页无法通过链接分享
- **跨页面调整**仍然是所有 HTML 生成 PPT 产品的老大难问题——最佳实践是先生成前用文字理清每页逻辑

## 关联知识

- [[ClaudeCode学习指南]] — Claude Code 的 goal/loop/batch/simplify 命令
- [[Obsidian首页设计]] — 同样涉及设计审美
- [[Obsidian插件推荐]] — Obsidian 中的 PPT 展示插件可选方案
