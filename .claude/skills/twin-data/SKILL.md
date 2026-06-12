---
name: twin-data
description: |
  Twin Planet (并蒂星球) data layer reference — WHO growth standards, database schema, API format, 
  and all data-related constants for the twins parenting mini-program.
  Use this skill whenever working on database design, API endpoints, growth curve calculations, 
  WHO LMS parameters, SQL queries, data validation, or data visualization for the 并蒂星球 project.
  Trigger on: twin database, twin schema, WHO growth, baby growth curve, z-score calculation, 
  twin API, baby records table, feeding data, sleep data, growth percentile.
---

# 并蒂星球 · Twin Data

## WHO LMS Growth Standards

### Z-Score Formula

```
When L ≠ 0:  Z = ((X/M)^L - 1) / (L × S)
When L = 0:  Z = ln(X/M) / S
```

Percentile = Φ(Z) × 100 (standard normal CDF)

### Weight-for-Age (0-24 months)

Girls weight (kg): L/M/S parameters from WHO standards — data available in project docs.
Boys weight (kg): L/M/S parameters from WHO standards — data available in project docs.

### Length-for-Age (0-24 months)

Girls length (cm): L/M/S parameters. Note: before 24 months use recumbent *length*, not standing height.
Boys length (cm): L/M/S parameters. After 24 months switch to standing *height* standard.

### Implementation

```typescript
// utils/whoGrowth.ts
interface LMSRecord { L: number; M: number; S: number; }
const WHO_DATA: Record<string, Record<string, LMSRecord[]>> = { /* static JSON */ };

export function getLMS(gender: 'male'|'female', ageMonths: number): LMSRecord;
export function calcZScore(value: number, L: number, M: number, S: number): number;
export function zScoreToPercentile(z: number): number;
export function getPercentileCurve(gender: string, indicator: string, p: number): Array<{x:number; y:number}>;
```

## Difference Rate Thresholds

| Twins Type | Green (<) | Yellow | Red (>) |
|------|:---:|:---:|:---:|
| Same gender | 10% | 10–20% | 20% |
| Different gender | 15% | 15–30% | 30% |

Different-gender twins have naturally wider growth gaps — higher thresholds prevent false alarms.

## Newborn & Premature Constraints

- **First 14 days after birth**: No LMS comparison. Show 14-day rolling average only. Physiological weight loss (up to 10%) is normal.
- **Premature babies (<37 weeks)**: Use corrected age for all LMS comparisons until corrected age reaches 24 months.
- **Vaccine reminder**: Must include fixed disclaimer: "疫苗接种前请确认宝宝近7天无发热、腹泻等症状，如有疑问请咨询医生"

## Database Schema

### Core Tables

```sql
CREATE TABLE users (
  id UUID PRIMARY KEY,
  openid VARCHAR(64) UNIQUE NOT NULL,
  nickname VARCHAR(64), avatar VARCHAR(512),
  phone VARCHAR(20) ENCRYPTED,
  role VARCHAR(20) DEFAULT 'mom',
  preferred_ui_mode VARCHAR(10) DEFAULT 'normal', -- 'normal' | 'large'
  ui_config JSONB DEFAULT '{}',
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE twin_groups (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  name VARCHAR(64),
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE babies (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  twin_group_id UUID REFERENCES twin_groups(id),
  name VARCHAR(32), nickname VARCHAR(32),
  gender VARCHAR(8),
  birth_date DATE, birth_order INT,
  color VARCHAR(7), avatar VARCHAR(512),
  birth_weight DECIMAL(5,2), birth_height DECIMAL(5,2),
  is_active BOOLEAN DEFAULT true
);
```

### Record Tables

```sql
CREATE TABLE feeding_records (
  id UUID PRIMARY KEY,
  baby_id UUID REFERENCES babies(id),
  type VARCHAR(20), -- 'breast'|'bottle'|'solids'
  side VARCHAR(10), amount_ml INT, duration_min INT,
  started_at TIMESTAMP, ended_at TIMESTAMP, note TEXT
);

CREATE TABLE sleep_records (
  id UUID PRIMARY KEY,
  baby_id UUID REFERENCES babies(id),
  type VARCHAR(10), -- 'nap'|'night'
  started_at TIMESTAMP, ended_at TIMESTAMP,
  quality_score INT, -- 1-5
  auto_inferred BOOLEAN DEFAULT false
);

CREATE TABLE growth_records (
  id UUID PRIMARY KEY,
  baby_id UUID REFERENCES babies(id),
  age_days INT, -- redundant for fast time-alignment joins
  weight DECIMAL(5,2), height DECIMAL(5,2), head_circumference DECIMAL(5,2),
  z_score_weight DECIMAL(6,3), z_score_height DECIMAL(6,3),
  measured_at TIMESTAMP
);
```

### Derived & Interaction Tables

```sql
CREATE TABLE daily_summaries (
  id UUID PRIMARY KEY,
  baby_id UUID REFERENCES babies(id), date DATE,
  total_sleep_min INT, feed_count INT, diaper_count INT, avg_weight DECIMAL(5,2)
);

CREATE TABLE sibling_interactions (       -- 萌芽日记
  id UUID PRIMARY KEY,
  twin_group_id UUID REFERENCES twin_groups(id),
  baby_ids UUID[],
  type VARCHAR(30), -- 'share'|'fight'|'imitate'|'comfort'|'compete'|'cooperate'|'first'
  note TEXT, recorded_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE parent_contributions (       -- 今天我做了什么
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  family_id UUID,
  category VARCHAR(30), -- 'night_feed'|'diaper'|'bath'|'play'|'cook'|'clean'|'errand'|'other'
  note TEXT, recorded_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE anomaly_events (             -- 异常事件日志
  id UUID PRIMARY KEY,
  baby_id UUID REFERENCES babies(id),
  user_id UUID REFERENCES users(id),
  severity VARCHAR(20), -- 'concerned'|'worried'|'very_worried'
  description TEXT, photo_url VARCHAR(512),
  shared_with_doctor_at TIMESTAMP,
  recorded_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE shift_handover_notes (       -- 交接班语音
  id UUID PRIMARY KEY,
  family_id UUID, from_user_id UUID REFERENCES users(id),
  audio_url VARCHAR(512),
  listened_by UUID[] DEFAULT '{}',
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE knowledge_articles (
  id UUID PRIMARY KEY,
  title VARCHAR(256), category VARCHAR(64),
  target_age_min INT, target_age_max INT,
  content TEXT, tags TEXT[], source VARCHAR(256),
  published_at TIMESTAMP, view_count INT DEFAULT 0
);

CREATE TABLE newbie_states (              -- 新手村
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  day_number INT, task_completed BOOLEAN,
  first_record_at TIMESTAMP, streak_days INT,
  week_report_sent_at TIMESTAMP
);
```

## API Response Format

All API responses follow this envelope:

```json
{
  "success": true,
  "data": { /* payload */ },
  "error": null,
  "meta": { "page": 1, "limit": 20, "total": 142 }
}
```

On error:
```json
{
  "success": false,
  "data": null,
  "error": { "code": "RECORD_NOT_FOUND", "message": "..." },
  "meta": null
}
```

## Tech Stack

- **Frontend**: uni-app (Vue3) → 微信小程序
- **Backend**: 腾讯云 CloudBase (TCB) Node.js 云函数
- **Database**: PostgreSQL (TCB 云数据库) + Redis (缓存+队列)
- **Storage**: 腾讯云 COS (SSE-COS加密)
- **AI**: DeepSeek / 腾讯混元
