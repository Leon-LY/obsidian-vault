---
name: twin-rules
description: |
  Twin Planet (双生星球) project management rules — schedule, phases, sprints, deliverables, 
  acceptance criteria, burnout protection, and stop-decision points for the twins parenting mini-program.
  Use this skill whenever working on project planning, task breakdown, sprint planning, milestone 
  tracking, or any decision about what to build and when for the 双生星球 project.
  Trigger on: twin schedule, twin sprint, twin phase, twin milestone, twin roadmap, twin planning,
  twin acceptance criteria, twin stop decision, burnout protection, what to build next.
---

# 双生星球 · Twin Rules

## Project Overview

- **Goal**: 12-week MVP → WeChat Mini Program for twin parenting
- **Developer**: Leon (solo full-stack, also a twin dad of 4-year-old 龙凤胎)
- **Tech**: uni-app (Vue3) + 腾讯云 CloudBase + DeepSeek
- **Total MVP Features**: 22 (P0:4 + P1:13 + P2:5)
- **Estimated Effort**: ~86 person-days (P0+P1), P2 deferred to Phase 2

## Phase Timeline

```
Phase 0: Week 1-2   → Foundation (domain, TCB env, curve demo, 20 articles)
Phase 1: Week 3-14  → 12-week MVP development (6 sprints, 22 features)
Phase 2: Month 4-6  → Growth iteration (AI engine, community, monetization)
Phase 3: Month 7+   → Native App + IoT + B2B
```

## Phase 1 Sprint Plan (12 weeks)

### Sprint 1 (Week 3-4): Onboarding
- WeChat login, family creation, add twins with colors
- **Build ALL core tables** (including anomaly_events pre-created)
- Deliverable: Registration → family → baby flow complete

### Sprint 1.5 (Week 4-5): Activation
- Newbie village guide (Day 0-7 automated message chain)
- Grandma accessibility mode (大字版 + TTS + 小苗苗 widget)
- Deliverable: 7-day onboarding flow ready

### Sprint 2 (Week 5-6): Core Recording
- Minimal dual-track feeding + sleep recording
- Voice input for recording
- Deliverable: Core recording functional (max 2 taps)

### Sprint 2.5 (Week 6-7): Emotional Anchors
- Sprout Diary (萌芽日记, 4 days) — twin interaction timeline
- "What I Did Today" (今天我做了什么, 2 days) — dad contribution log
- Deliverable: Interaction timeline + dad contribution entry

### Sprint 3 (Week 7-8): Dashboard
- Homepage dual-baby dashboard + dual-track timeline
- Dad's Snapshot homepage (三明治卡片)
- Shift handover voice note (极简版: record → COS → red dot alert)
- Deliverable: Full homepage experience with multi-role views

### Sprint 3.5 (Week 8-9): Collaboration Engine
- Dad Duty Mode (爸爸值班模式, 5 days) — SOP checklist engine
- Caregiver Interruption Notification (照顾者中断通知) — stats-based trigger only, no keyword matching
- Deliverable: SOP engine + anomaly detection rules

### Sprint 4 (Week 9-10): Growth Center + Guardian System
- Growth comparison curves (WHO LMS, Phase 0 Demo compressed to 7 days)
- Mama/Papa Battery Meter (妈妈/爸爸电量表)
- One-on-One Time Guardian (一人时光守护者)
- Deliverable: Core differentiation live + guardian system closed

### Sprint 5 (Week 10-11): Retention Loop
- Smart reminders (feeding + vaccine, with disclaimer)
- WeChat subscription messages
- 7-day voice companionship (7真人录音)
- Clinic Quick Card (就诊速查卡)
- Deliverable: Retention loop established

### Sprint 6 (Week 11-12): Launch Prep
- Comparison photo auto-pairing
- Anomaly event log (异常事件日志)
- Knowledge base (20+ articles) + bug fixes
- Deliverable: Security + spread engines ready, beta test package

### Buffer (Week 13-14)
- Beta testing with 50 seed users
- Bug fixes and polish

## Key Deliverables Per Sprint

| Sprint | P0 Deliverables | P1 Deliverables |
|:---:|------|------|
| 1 | Login + family + baby creation | Core tables DDL |
| 1.5 | — | Newbie village + Grandma mode |
| 2 | Feeding + sleep recording | Voice input |
| 2.5 | — | Sprout Diary + What I Did Today |
| 3 | Dashboard + timeline | Dad Snapshot + handover voice |
| 3.5 | — | Dad Duty + Interruption notice |
| 4 | Growth curves | Battery meter + Time guardian |
| 5 | Reminders + subscription msg | Voice companions + Clinic card |
| 6 | Photo pairing + KB articles | Anomaly log + beta package |

## MVP Acceptance Criteria (17 items)

- ✅ 3-step registration → family → baby flow
- ✅ Feeding record ≤2 taps (voice input optional), recording always free
- ✅ Both babies' feeding/sleep viewable on same page
- ✅ Growth curves: record, compare, WHO standard overlay
- ✅ Sprout Diary: twin interaction events recordable
- ✅ Dad exclusive entry: Snapshot + What I Did + Duty Mode
- ✅ Mama/Papa Battery Meter + One-on-One Time Guardian
- ✅ Caregiver Interruption Notification (graded reminders)
- ✅ Newbie Village Day 0-7 complete chain
- ✅ Knowledge base searchable by age
- ✅ Feeding/vaccine reminders with disclaimer
- ✅ 20+ twin-specific articles online
- ✅ 7 voice companion recordings ready
- ✅ Clinic Quick Card exports twin comparison summary (color ≠ diagnosis)
- ✅ Anomaly event log (plain text notepad, no AI analysis)
- ✅ Grandma mode: large font + TTS + 小苗苗 widget
- ✅ Growth curve: no LMS comparison <14 days; premature = corrected age

## Stop Decision Points

**After Phase 1 (3 months post-launch), evaluate:**
```
├─ DAU < 50 families?        → 🛑 Pause
├─ Month-2 retention < 30%?  → 🛑 Pause
├─ Leon exhausted?           → 🛑 Pause
└─ All three OK              → ✅ Continue to Phase 2
```

> Pausing ≠ failure. It means "we learned something, now do something else."

## Burnout Protection (6 rules)

1. **Stop standard**: 3 consecutive days <6h sleep → mandatory 2-day rest
2. **Weekly cap**: ≤20 hours coding per week
3. **Family first**: Partner complaints >2/month → decelerate or pause
4. **External buffer**: Public timeline says "est. 14 weeks", not 12
5. **Sprint-done-no-chase**: If sprint expires with unfinished work → cut features, don't chase
6. **1 full rest day/week**: At least one day per week completely away from computer

## Revenue Model

- **Free tier**: Unlimited dual-track recording + basic growth curves + basic reminders + 5 articles/day
- **Premium**: ¥79/6 months (≈¥13/month) → +AI schedule engine + unlimited KB + deep analysis + 5-family sharing + data export

## Project Documentation

All project docs live in: `知识库/项目/私活/双生星球/`

Key files:
- `双生星球-项目建设方案.md` — V3.2 build plan (this document's source)
- `双生星球-十角色终局论证.md` — Final 10-role cross-argumentation
- `双生星球-Phase0-执行手册.md` — Phase 0 execution handbook
