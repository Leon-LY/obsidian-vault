---
name: twin-design
description: |
  Twin Planet (双生星球) UI/UX design system for the twins parenting mini-program (uni-app Vue3). 
  Use this skill whenever working on any frontend design, UI component, layout, color scheme, 
  accessibility feature, or visual element for the 双生星球 project.
  Trigger on: twin design, twin UI, twin colors, twin branding, baby card layout, grandma 
  accessibility, pediatric safety, dark mode parenting app, WeChat mini-program UI.
---

# 双生星球 · Twin Design

## Color Scheme

| Purpose | Name | Hex |
|------|------|------|
| Baby A (安宁) | Sky Blue | `#4299E1` |
| Baby B (安然) | Soft Pink | `#F56565` |
| Background | Warm White | `#FFFBF5` |
| Card Background | Pure White | `#FFFFFF` |
| Primary Text | Dark Gray | `#2D3748` |
| Secondary Text | Medium Gray | `#A0AEC0` |
| AI/Accent | Mint Green | `#48BB78` |
| Warning | Warm Orange | `#ED8936` |

## Grandma Accessibility Standards

These 5 standards apply globally. Enable by default for users aged 55+.

1. **One-button-no-three (一就是一定制)**: One button per task. Homepage has exactly 3 large buttons (Record / Compare / Help). Minimum 40px spacing between buttons.
2. **Audio-over-text (能听不看)**: All reminders support TTS audio playback. Use `wx.createInnerAudioContext` with pre-generated MP3 files on COS for common phrases; real-time TTS synthesis only for custom content.
3. **Pictures-over-numbers (图画替代数字)**: Replace raw numbers with visual indicators. The "Little Sprout" (小苗苗) widget shows green/yellow/red state instead of sync rate percentage. Growth curves use intuitive color gradients, not percentiles alone.
4. **Anti-mistouch spacing (防误触隔离)**: Minimum 40px white space between action buttons and data displays. Critical actions (like SOS) get extra isolation.
5. **Large font mode (大字模式)**: Default font size ≥18px when enabled. Manual toggle in Settings. Auto-detect via behavior: if first operation takes >30s, offer "Would you like large font mode?"

## Twin Baby Card Layout

Every card representing a baby follows this pattern:

```
┌──────────────────────────────────────────┐
│  [Baby Avatar]   Baby Name (#Color)       │
│  ● Last Feed: 2h ago (120ml)             │
│  ● Last Sleep: 45min (awake now)          │
│  ● Status: 😊 Playing                     │
└──────────────────────────────────────────┘
```

On the homepage, show both baby cards side-by-side (dual-card layout). Each baby's color serves as their visual identity — use it for left-border, avatar ring, and data point markers on charts.

## Pediatrician Safety Red Lines

Every feature must comply with these 6 rules. Violating any one blocks release.

| # | Rule | Implementation |
|:--:|------|------|
| 1 | No medical judgment | Never output "建议就医", "建议观察", or any disease possibility |
| 2 | No vaccine decision | Vaccine conflict detection only shows facts ("3 days ago: fever 38.2°C"), never "建议推迟" or "可以接种" |
| 3 | No symptom analysis | Anomaly event log is a plain-text notepad — no AI classification, no pattern matching |
| 4 | Color ≠ diagnosis | Growth curve difference rate colors carry mandatory disclaimer: "颜色仅为统计标记，不代表医学诊断" |
| 5 | All AI content disclaimed | Every AI-generated text includes "仅供参考，不构成医疗建议" |
| 6 | Photo encryption | Anomaly event log photos (rashes, gait) are sensitive health data — SSE-COS encrypted, thumbnails only, originals auto-delete in 7 days |

## Interaction Principles

- **One-hand operation**: All core buttons in the lower half of the screen. Target size ≥44x44px for tap areas.
- **Zero-think recording**: Complete a feeding/sleep record in ≤2 taps. No forms, no confirm buttons. Tap to start timer, tap to stop.
- **Dark mode**: Auto-switch for nighttime (22:00-06:00). Dark background #1A202C with muted accent colors. Reduce blue light for the sleeping partner.
- **Baby-as-hero**: Every baby has a unique color + avatar. No ambiguity about whose data is being viewed.

## Brand Identity

- **Name**: 双生星球 (Twin Planet)
- **Slogan**: 一个 App 管好两个娃
- **Internal philosophy**: 看见每一个人 (See Every Person)
- **Mascot**: A pair of little stars/planets (one blue, one pink)
- **Tone**: Professional but warm girlfriend — not too sweet, not too cold

## Platform: WeChat Mini Program (uni-app Vue3)

- Vue3 Composition API with `<script setup>`
- ECharts for data visualization (split-package loading, main package <2MB)
- Pinia for state management
- HBuilderX + Vite build toolchain
- Custom components for twin-specific UI: `BabySwitcher`, `DualTimeline`, `GrowthChart`, `QuickLog`
