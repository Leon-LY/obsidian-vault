---
graph_visible: true
---

# 并蒂星球 · 设计需求文档

> **用途**：将本文档喂给 Google Stitch / Canva / Claude Design / 人类设计师，产出高保真原型。
> **版本**：V1.0 · 2026-06-12
> **编制**：Leon + 六角色论证

---

## 一、品牌身份

| 项 | 值 |
|------|------|
| **产品名** | 并蒂星球 (Twin Planet) |
| **Slogan** | 并蒂而生，同步成长 |
| **一句话** | 中国首款双胞胎育儿伴侣（0-6 岁） |
| **产品哲学** | 看见每一个人 (See Every Person) |
| **意象来源** | 并蒂莲—— 一茎两花，同根共生、各自独立 |
| **平台** | 微信小程序 (375-414px 宽) |
| **设备** | iPhone / Android 手机，竖屏 |

---

## 二、用户画像

### 核心用户

| 角色 | 年龄 | 使用频率 | 典型场景 |
|------|:--:|:--:|------|
| 👩 双胞胎妈妈 | 28-38 | 每天 5-10 次 | 凌晨 3 点单手喂奶记录；白天对比两个孩子的数据；儿保体检后录入 |
| 👨 双胞胎爸爸 | 28-40 | 每天 2-3 次 | 下班后快速浏览快照；周末独自值班时照着清单操作 |
| 👵 奶奶/外婆 | 55-70 | 每天 1-2 次 | 白天独自带娃时需要大字版、怕按错按钮、记不住操作 |

### 覆盖家庭类型

- 两个男孩 ≈ 33%
- 两个女孩 ≈ 33%
- 龙凤胎 ≈ 33%

> **关键约束**：产品在任何地方都不能给用户"蓝=男、粉=女"的性别暗示。

---

## 三、色彩系统

### 主色调

| 角色 | 色值 | 说明 |
|------|------|------|
| 大宝（先出生） | `#A45C40` | 深陶土——温暖、沉稳、像烘焙咖啡豆 |
| 二宝（后出生） | `#C7866A` | 浅陶土——同一色系、更柔和的明度 |
| 页面背景 | `#F5EFE7` | 暖奶油色——像未漂白的纸张 |
| 卡片背景 | `#FFFCF8` | 带极微暖调的白色 |
| 主文字 | `#241E1A` | 深褐——对比度 > 12:1 |
| 副文字 | `#6B635B` | 暖灰——对比度 > 5:1 |
| 强调色 | `#7BA882` | 鼠尾草绿——健康、成长、正面 |
| 警告色 | `#D4956B` | 暖杏——温和的提醒，不制造焦虑 |

### 颜色分配铁律

```
颜色按出生顺序分配，不按性别。

大宝(先出生) = #A45C40 深陶土
二宝(后出生) = #C7866A 浅陶土

适用于：两个男孩 / 两个女孩 / 一男一女
禁止：将任何颜色与性别关联
```

### 夜间模式

22:00-06:00 自动切换。色彩向烘焙咖啡/暖炭过渡：

| 元素 | 日间 | 夜间 |
|------|------|------|
| 背景 | `#F5EFE7` | `#1E1915` |
| 卡片 | `#FFFCF8` | `#2A2420` |
| 文字 | `#241E1A` | `#E8E0D6` |
| 大宝 | `#A45C40` | `#D4A088` |
| 二宝 | `#C7866A` | `#E8C5B4` |

---

## 四、字型与排版

### 字体

| 场景 | 字体 | 理由 |
|------|------|------|
| 中文展示标题 | Noto Serif SC (衬线体) | 有温度、有文学感——不是冰冷的工具 |
| 正文/数字/标签 | PingFang SC / -apple-system | 保证小字清晰可读 |
| 等宽数字 | SF Mono / Menlo | 计时器和数字需要对齐 |

### 字阶

| 等级 | 字号 | 用途 |
|:--:|------|------|
| 超大 | 52px, weight 300 | 首页体重数字、计时器 |
| 标题 | 22px, weight 800 | 页面标题 |
| 正文 | 15px, weight 400 | 卡片内文字 |
| 标签 | 11px, weight 600, uppercase | section 标签 |

---

## 五、必须遵守的设计规则

### ✅ 必须做到

1. 双宝数据永远并排（左右分列），不让用户切来切去
2. 记录页面按钮在屏幕下半部（单手抱娃时拇指可达）
3. 所有文字对比度 ≥ 4.5:1（WCAG AA）
4. 大数字配叙事语义（"比上月 +0.4kg"，不只有数字）
5. 衬线体只用于标题——正文永远用系统字体保证可读性

### ❌ 绝对禁止

1. 紫蓝渐变（AI slop #1）
2. Emoji 作为图标
3. 侧边彩色竖线装饰（border-left accent）
4. 完全相同的卡片网格（要有视觉主次）
5. 毛玻璃效果作为默认风格
6. 将蓝色用于"男宝"或将粉色用于"女宝"

---

## 六、4 个核心页面

### 页面1：首页

**页面目的**：每天打开看一眼关键数据，快速导航到其他功能。

**核心内容**：
- 品牌区：产品名 + slogan（顶栏下方居中）
- 双宝体重卡片（左右并排，各显示最新体重 + 测量日期）
- 生长差异提示条（显示差异数值 + "比上月缩小/扩大 0.Xkg" + 正常范围徽标）
- 4 个功能入口网格（生长曲线 / 双轨记录 / 萌芽日记 / 守护中心）
- 底部 TabBar（首页 / 生长 / 记录 / 守护）

**设计要点**：
- 两个宝宝的卡片等大等权重
- 差异提示条用微暖色背景（不是红色）——"正常范围"的绿色徽标让人安心
- 功能入口中有 2 个用暖陶土色图标背景（生长曲线/记录），2 个用中性灰——有主次节奏

**Google Stitch Prompt**：
```
A mobile app home screen for a twin parenting app called "并蒂星球". 
Warm terracotta brand color #A45C40. Cream background #F5EFE7.
Top: app name centered in serif font.
Two baby weight cards side by side: left "大宝 16.8 kg" right "二宝 14.2 kg", each showing last measurement date.
A difference card below: "生长差异 2.6 kg · 比上月缩小 0.3kg" with a green "正常范围" badge.
4 function cards in a 2x2 grid: 生长曲线, 双轨记录, 萌芽日记, 守护中心.
Bottom tab bar with 4 tabs: 首页/生长/记录/守护.
iPhone 15 Pro size. Clean, warm, editorial feel. No purple, no pink gradient, no blue/pink gender coding.
Reference aesthetic: Apple Health meets Headspace.
```

---

### 页面2：生长曲线

**页面目的**：对比两个宝宝的生长数据，对标 WHO 国际标准。

**核心内容**：
- 页面标题："生长曲线" + 副标题"WHO 国际标准 · 并蒂对比"
- 曲线图区域：一个 SVG 折线图，两条折线（深陶土=大宝，浅陶土=二宝），浅灰虚线参考线
- 图例 + 差异率徽标（"差异 2.3%"，绿色背景）
- 免责声明："生长差异在正常范围。每个宝宝有自己的成长节奏。"
- 双宝数据卡片（左右并排，显示体重/百分位/比上月变化）

**设计要点**：
- 两条曲线颜色有足够对比（不在图上加性别标签）
- 参考线极淡（不主次不分）
- 免责声明不是可有可无的脚注——它在视觉上有分量
- 每个数据卡显示"比上月 +0.4kg"（叙事，不只有数字）

**Google Stitch Prompt**：
```
A growth chart screen for the "并蒂星球" twin parenting app.
Warm terracotta #A45C40 and lighter terracotta #C7866A for the two babies' data.
iPhone 15 Pro size.
Header: "生长曲线" in serif, sublabel "WHO 国际标准 · 并蒂对比".
An SVG line chart area with two colored lines (no gender labels), light grey dashed reference lines.
Legend shows colors for 大宝 and 二宝. A green badge "差异 2.3%".
Disclaimer at bottom: "生长差异在正常范围。每个宝宝有自己的成长节奏。"
Two data cards below: each shows baby name, weight with unit, percentile, and monthly change.
Clean, data-visualization-forward. Reference: Apple Health app.
```

---

### 页面3：双轨记录

**页面目的**：单手完成喂养/睡眠/换尿布记录。≤2 次点击。

**核心内容**：
- 页面标题："双轨记录" + 副标题"两次点击 · 单手完成"
- 双宝状态条（左右并排，显示最近一次记录时间）
- 两个大按钮（深陶土=大宝，浅陶土=二宝）——在屏幕下半部
- 4 个快捷标签行（喂奶 / 睡觉 / 尿布 / 快记）
- 最近记录列表（圆点标记区分宝宝，显示动作+时长+时间）

**设计要点**：
- 两个主按钮必须在拇指可达区（屏幕下半部）
- 按钮足够大（≥ 90px 高），凌晨摸黑也能点中
- 快捷标签行是次级操作，视觉上退后
- 最近记录列表用 8px 圆点替代侧边色条区分宝宝

**Google Stitch Prompt**：
```
A recording screen for the "并蒂星球" twin parenting app.
iPhone 15 Pro size. Warm terracotta #A45C40 brand.
Header: "双轨记录" in serif, "两次点击 · 单手完成" subtitle.
Two baby status bars at top showing last record time.
Two large buttons (half-screen height each, warm terracotta background) 
positioned in the LOWER half of the screen for one-handed use: 
left "大宝" right "二宝", each reading "点击记录 · 喂养 · 睡眠 · 尿布".
Four small quick-action tags below: 喂奶 睡觉 尿布 快记.
A recent records list below with colored dot markers (not side stripes) 
distinguishing which baby each entry belongs to.
Design for one-handed night use by sleep-deprived parents.
```

---

### 页面4：守护中心

**页面目的**：展示妈妈/爸爸电量 + 一人时光守护。

**核心内容**：
- 页面标题："守护中心" + 副标题"看见每一个人的状态"
- 一人时光卡片（highlight 暖色背景）——显示大宝/二宝今天各陪伴了多少分钟 + "开始陪伴计时"按钮
- 妈妈电量 + 爸爸电量（左右并排，数字+状态文字）

**设计要点**：
- "一人时光"是核心功能——给它最显眼的视觉权重
- 电量用大数字+简短状态文字（"需要充电"/"电量充足"），不画复杂的环形图
- 按钮使用强调色（鼠尾草绿），暗示"这是一件好事"

**Google Stitch Prompt**：
```
A guardian/wellness screen for the "并蒂星球" twin parenting app.
iPhone 15 Pro size. Warm terracotta #A45C40 brand, sage green #7BA882 accent.
Header: "守护中心" in serif, "看见每一个人的状态" subtitle.
Highlighted card section "一人时光": two columns showing "大宝 45 min 今天" and "二宝 32 min 今天", 
with a prominent green "开始陪伴计时" button below.
Two side-by-side cards for parent energy: "妈妈电量 4 · 需要充电" and "爸爸电量 7 · 电量充足".
Clean typography, generous whitespace. Not a dashboard - more like a wellness check-in.
```

---

## 七、设计参考（Mood Board）

### 美学参考

| 产品 | 借鉴什么 |
|------|------|
| **Apple Health** | 极简数据可视化、大数字、克制配色、信息层级清晰 |
| **Headspace** | 温暖治愈不幼稚、高留白、圆形元素带来的安全感 |
| **Stripe** | 精致微阴影、玻璃效果、专业信任感 |
| **Notion** | 简洁的信息层级、柔和的色彩分区、emoji icon 体系 |

### 反参考（不要做成这样）

- 传统母婴 App（粉色圆角卡通、暖色渐变、过度装饰）
- AI 生成的"SaaS 落地页"（紫色渐变+Inter 字体+三列卡片+hero metric）
- Material Design 模板（侧边彩色 accent 条+相同大小的卡片网格）

---

## 八、Logo 需求

> 在 Claude 中设计 Logo 效果差。建议交给人类设计师或 Looka/Canva。

### Logo 设计简报

| 项 | 要求 |
|------|------|
| **核心意象** | 并蒂莲——一茎两花，同根共生 |
| **风格** | 极简几何（App 图标优先）+ 并蒂花变体（品牌物料） |
| **颜色** | 深陶土 `#A45C40` + 浅陶土 `#C7866A` |
| **格式** | 小程序 144px 圆形裁切后仍可识别 |
| **禁忌** | 不用蓝色、不用粉色、不用婴儿/奶瓶等母婴陈词滥调 |

---

## 九、交互约束（给开发者的）

| 约束 | 说明 |
|------|------|
| 单手操作 | 核心按钮在屏幕下半部，≥ 44×44px 触摸区 |
| ≤2 tap 记录 | 点宝宝 → 点停止，两步完成 |
| 夜间自动暗色 | 22:00-06:00 自动切换，状态栏可手动覆盖 |
| 大字模式 | 奶奶/爷爷角色自动启用 ≥ 18px 字体 |
| 防误触间距 | 关键操作间距 ≥ 40rpx |
| 对比度底线 | 所有文字 WCAG AA (≥ 4.5:1) |

---

## 十、图标系统

- 不使用 Emoji 作为功能图标
- 使用线性 SVG 图标，笔画 1.5px
- 颜色可随主题切换（日间深褐 / 夜间暖沙）
- 功能入口用 10px 圆角小方块内嵌白色图标做区分

---

## 附录：完整色值参考（复制粘贴给设计师）

```css
:root {
  /* 品牌 */
  --accent:       #A45C40;  /* 大宝 · 深陶土 */
  --accent-dim:   #834831;  /* 深变体 */
  --accent-light: #C7866A;  /* 二宝 · 浅陶土 */
  --accent-lt:    #E8C5B4;  /* 极浅 · 夜间用 */

  /* 背景 */
  --base:         #F5EFE7;  /* 暖奶油底 */
  --base-alt:     #EEE6DB;  /* 暖奶油变体 */
  --surface:      #FFFCF8;  /* 卡片白 */
  --surface-hl:   #FFF5ED;  /* 高亮卡片 */

  /* 文字 */
  --ink:          #241E1A;  /* 主文字 · 13:1 对比度 */
  --ink2:         #6B635B;  /* 副文字 · 5:1 对比度 */
  --ink3:         #A09991;  /* 标签文字 */

  /* 语义 */
  --good:         #7BA882;  /* 鼠尾草绿 · 正面 */
  --good-bg:      #ECF5EF;  /* 绿底 */
  --warn:         #D4956B;  /* 暖杏 · 提醒 */
  --warn-bg:      #FFF5ED;  /* 杏底 */

  /* 夜间 */
  /* 背景: #1E1915 → #2A2420 → #302925 */
  /* 文字: #E8E0D6 → #A09890 → #7A726A */
  /* 大宝: #D4A088 · 二宝: #E8C5B4 */
  /* 绿: #7DC08A · 杏: #E0A878 */
}
```
