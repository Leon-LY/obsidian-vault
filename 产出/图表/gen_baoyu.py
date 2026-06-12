# -*- coding: utf-8 -*-
import os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
OUT = 'E:/ly/Obsidian/work/产出/图表'

STYLE = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">
  <defs>
    {defs}
  </defs>
  <rect width="{w}" height="{h}" fill="#f4f6f9" rx="8"/>
  {title}
  {content}
  <text x="{cx}" y="{h}-20" font-family="'Microsoft YaHei',sans-serif" font-size="9" fill="#95a5a6" text-anchor="middle">数字荣成治理提升项目</text>
</svg>'''

DEFS = '''<marker id="arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="#1a5276"/></marker>
    <filter id="sh"><feDropShadow dx="1" dy="1" stdDeviation="1.5" flood-opacity="0.12"/></filter>
    <linearGradient id="gdb" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#1a5276"/><stop offset="100%" stop-color="#2980b9"/></linearGradient>
    <linearGradient id="gmb" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#2471a3"/><stop offset="100%" stop-color="#2e86c1"/></linearGradient>
    <linearGradient id="gte" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#1abc9c"/><stop offset="100%" stop-color="#16a085"/></linearGradient>
    <linearGradient id="gdk" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#2c3e50"/><stop offset="100%" stop-color="#1a252f"/></linearGradient>
    <linearGradient id="gor" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#f39c12"/><stop offset="100%" stop-color="#e67e22"/></linearGradient>
    <linearGradient id="grd" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#e74c3c"/><stop offset="100%" stop-color="#c0392b"/></linearGradient>
    <linearGradient id="ggr" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#27ae60"/><stop offset="100%" stop-color="#229954"/></linearGradient>
    <linearGradient id="gpr" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#8e44ad"/><stop offset="100%" stop-color="#6c3483"/></linearGradient>'''

def make_title(text):
    return f'<text x="{{cx}}" y="40" font-family="\'Microsoft YaHei\',sans-serif" font-size="20" font-weight="700" fill="#1a5276" text-anchor="middle">{text}</text>'

def box_text(cx, cy, text1, text2='', grad='gdb', w=210, h=78, fs1=12, fs2=9):
    s = f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="8" fill="url(#{grad})" filter="url(#sh)"/>\n'
    s += f'<text x="{cx}" y="{cy-8}" font-family="\'Microsoft YaHei\',sans-serif" font-size="{fs1}" font-weight="600" fill="white" text-anchor="middle">{text1}</text>\n'
    if text2:
        s += f'<text x="{cx}" y="{cy+16}" font-family="\'Microsoft YaHei\',sans-serif" font-size="{fs2}" fill="#bdc3c7" text-anchor="middle">{text2}</text>\n'
    return s

def arrow_y(x, y1, y2):
    return f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="#1a5276" stroke-width="2" marker-end="url(#arr)"/>\n'

def layer_bg(x, y, w, h, label, color="#2980b9", bgColor="#ebf5fb"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{bgColor}" stroke="{color}" stroke-width="1.2"/>\n'
    s += f'<text x="{x+12}" y="{y+18}" font-family="\'Microsoft YaHei\',sans-serif" font-size="11" font-weight="700" fill="{color}">{label}</text>\n'
    return s

def layered_diagram(filename, title_text, layers, w=1200, h=0):
    """layers = [(label, color, bgColor, items)] where items = [(text1, text2, grad), ...]"""
    LAYER_H = 120; GAP = 30
    n = len(layers)
    h = 80 + n*(LAYER_H+GAP) + 30
    content = ''
    cx = w//2
    y = 70
    for i, (label, color, bg, items) in enumerate(layers):
        n_items = len(items)
        spacing = (w - 60 - n_items*210) // (n_items + 1)
        content += layer_bg(30, y, w-60, LAYER_H, label, color, bg)
        for j, (t1, t2, grad) in enumerate(items):
            bx = 30 + spacing + j*(210+spacing) + 105
            content += box_text(bx, y+60, t1, t2, grad)
        if i < n-1:
            content += arrow_y(cx, y+LAYER_H, y+LAYER_H+GAP)
        y += LAYER_H + GAP

    defs = DEFS
    title = make_title(title_text).replace('{cx}', str(cx))
    svg = STYLE.format(w=w, h=h, defs=defs, title=title, content=content, cx=str(cx))
    with open(os.path.join(OUT, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f'  ✓ {filename}')

def flow_diagram(filename, title_text, steps, w=1200):
    """steps = [(text1, text2, grad), ...]"""
    n = len(steps)
    spacing = (w - 60 - n*200) // (n + 1)
    h = 180
    content = ''
    for i, (t1, t2, grad) in enumerate(steps):
        x = 30 + spacing + i*(200+spacing) + 100
        content += box_text(x, 100, t1, t2, grad, w=180, h=70, fs1=11, fs2=8)
        if i < n-1:
            content += f'<line x1="{x+90}" y1="100" x2="{x+90+spacing+20}" y2="100" stroke="#1a5276" stroke-width="2" marker-end="url(#arr)"/>\n'
    content += f'<circle cx="{steps[0][0]}" cy="100" r="0" opacity="0"/>'  # nop
    cx = w//2
    defs = DEFS
    title = make_title(title_text).replace('{cx}', str(cx))
    svg = STYLE.format(w=w, h=h, defs=defs, title=title, content=content, cx=str(cx))
    with open(os.path.join(OUT, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f'  ✓ {filename}')

def three_col(filename, title_text, left_items, center_items, right_items, w=1200, h=600):
    """Three column layout"""
    content = ''
    # Left
    lx = 80; ly = 120; lstep = 100
    for i, (t1, t2, grad) in enumerate(left_items):
        content += box_text(lx, ly + i*lstep, t1, t2, grad, w=230, h=70, fs1=11, fs2=8)
    # Center
    cty = 120 + (len(left_items)-1)*lstep//2
    content += box_text(w//2, cty, center_items[0], center_items[1] if len(center_items)>1 else '', 'gdb', w=300, h=120)
    # Right
    rx = w - 80
    for i, (t1, t2, grad) in enumerate(right_items):
        content += box_text(rx, ly + i*lstep, t1, t2, grad, w=230, h=70, fs1=11, fs2=8)
    # Arrows
    for i in range(len(left_items)):
        content += f'<line x1="{lx+115}" y1="{ly+i*lstep}" x2="{w//2-150}" y2="{cty}" stroke="#1a5276" stroke-width="1.5" marker-end="url(#arr)"/>\n'
        content += f'<line x1="{w//2+150}" y1="{cty}" x2="{rx-115}" y2="{ly+i*lstep}" stroke="#1a5276" stroke-width="1.5" marker-end="url(#arr)"/>\n'

    cx = w//2
    defs = DEFS
    title = make_title(title_text).replace('{cx}', str(cx))
    svg = STYLE.format(w=w, h=h, defs=defs, title=title, content=content, cx=str(cx))
    with open(os.path.join(OUT, filename), 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f'  ✓ {filename}')


# ═══════════════════════════
# GENERATE ALL 18 DIAGRAMS
# ═══════════════════════════
print("生成 baoyu 风格 SVG 图表\n")

# 1 — 图5-1 系统总体技术架构
layered_diagram('图5-1_baoyu.svg', '图5-1 系统总体技术架构', [
    ('展示层','#2980b9','#ebf5fb',[('PC端 Web','管理后台 · 数据看板','gdb'),('大屏展示','分辨率 3840×2160','gdb'),('移动端 App','接入山东通平台','gdb')]),
    ('应用层','#2471a3','#eaf2f8',[('社会治理','应用场景','gmb'),('应急指挥','能力提升','gmb'),('零碳大脑','建设','gmb'),('数字人','智能解说','gmb')]),
    ('服务层','#16a085','#e8f8f5',[('RESTful API','网关','gte'),('WebSocket','实时推送','gte'),('RabbitMQ','消息队列','gte'),('XXL-Job','定时任务','gte')]),
    ('数据层','#2c3e50','#f2f3f4',[('MySQL 8.0','业务库','gdk'),('Redis','缓存集群','gdk'),('Elasticsearch','搜索引擎','gdk'),('MinIO','对象存储','gdk')]),
    ('基础设施层','#e67e22','#fdf2e9',[('政务云服务器','荣成市大数据中心','gor'),('K3s 容器编排','轻量 Kubernetes','gor'),('麒麟 V10','信创操作系统','gor')]),
])

# 2 — 图5-2
layered_diagram('图5-2_baoyu.svg', '图5-2 数据流转与集成设计', [
    ('采集层','#2980b9','#ebf5fb',[('API 采集','RESTful/JSON','gdb'),('数据库同步','定时任务','gdb'),('文件导入','Excel/CSV','gdb'),('人工录入','移动端+PC','gdb'),('实时流接入','WebSocket','gdb')]),
    ('处理层','#2471a3','#eaf2f8',[('数据清洗','去重·补缺','gmb'),('格式转换','统一编码','gmb'),('数据关联','信用代码','gmb'),('质量校验','规则引擎','gmb'),('指标计算','聚合·派生','gmb')]),
    ('存储层','#16a085','#e8f8f5',[('MySQL/达梦','业务主库','gte'),('Redis','缓存+实时','gte'),('Elasticsearch','全文检索','gte'),('MinIO','文件存储','gte'),('Kafka','消息队列','gte')]),
    ('服务层','#e67e22','#fef9e7',[('RESTful API','数据查询','gor'),('WebSocket','实时推送','gor'),('XXL-Job','任务调度','gor'),('RabbitMQ','事件消息','gor'),('API Gateway','统一网关','gor')]),
    ('展示层','#27ae60','#e9f7ef',[('PC端 Web','管理后台','ggr'),('大屏展示','3840×2160','ggr'),('移动端','山东通App','ggr'),('数据报表','自动导出','ggr'),('接口开放','开发者','ggr')]),
])

# 3 — 图4.4-1
layered_diagram('图4.4-1_baoyu.svg', '图4.4-1 零碳大脑功能架构', [
    ('展示层','#2980b9','#ebf5fb',[('碳排放全景看板','','gdb'),('重点排放源监测','','gdb'),('新能源发展态势','','gdb'),('碳减排项目管理','','gdb'),('碳汇资源展示','','gdb')]),
    ('分析计算层','#16a085','#e8f8f5',[('排放核算','IPCC 方法','gte'),('趋势预测','时间序列','gte'),('行业对比','多维分析','gte'),('减排评估','效果追踪','gte'),('碳汇计量','海洋/林业','gte')]),
    ('数据采集层','#27ae60','#e9f7ef',[('统计局','能源数据','ggr'),('供电公司','电力消费','ggr'),('生态环境局','排放数据','ggr'),('企业直报','月报数据','ggr'),('卫星遥感','碳汇监测','ggr')]),
])

# 4 — 图3-3 走访管理流程
flow_diagram('图3-3_baoyu.svg', '图3-3 走访管理全流程', [
    ('1.计划生成','自动+手动','gdb'),('2.任务分配','网格到人','gmb'),('3.走访执行','移动端定位','gte'),
    ('4.结果录入','三步完成','ggr'),('5.问题流转','跨部门推送','gor'),('6.归档统计','自动汇总','gdk'),
])

# 5 — 图4.3-1 应急指挥
flow_diagram('图4.3-1_baoyu.svg', '图4.3-1 应急指挥全流程', [
    ('1.事件接收\n与定位','','grd'),('2.资源分级\n展示','','gor'),('3.处置方案\n生成','','gmb'),
    ('4.指挥调度\n执行','','gdb'),('5.处置归档\n与复盘','','ggr'),
])

# 6 — 附6.2 走访记录业务
flow_diagram('附6.2_baoyu.svg', '附6.2 走访记录业务流程', [
    ('创建走访任务','','gdb'),('分配网格员','','gmb'),('现场走访执行','','gte'),
    ('填写记录拍照','','ggr'),('提交审核','','gor'),('是否需要上报','','gpr'),('直接归档','','gdk'),
])

# 7 — 图3-6 数据共享
three_col('图3-6_baoyu.svg', '图3-6 数据共享总体架构',
    [('自然资源局','用地+坐标','gdb'),('住建局','产权+安全','gmb'),('市场监管局','信用+处罚','gte'),('综合执法局','案件+记录','gor')],
    ['荣成市大数据中心','统一认证 | 权限管理 | 全链路审计 | 数据不落地'],
    [('社会治理','应用场景','ggr'),('城市大脑','大屏展示','ggr'),('移动端','山东通','ggr'),('应急指挥','模块','ggr')])

# 8 — 图4.5-1 数字人解说
flow_diagram('图4.5-1_baoyu.svg', '图4.5-1 数字人解说系统交互架构', [
    ('1.数据提取','读取DOM/API','gdb'),('2.模板匹配','选择解说模板','gmb'),('3.内容填充','占位符替换','gte'),
    ('4.TTS合成','语音生成','ggr'),('5.驱动数字人','表情+口型','gor'),
])

# 9 — 附图10-1
layered_diagram('附图10-1_baoyu.svg', '附图10-1 系统逻辑部署架构', [
    ('DMZ 区','#e74c3c','#fdedec',[('Nginx','反向代理','grd'),('WAF','Web防火墙','grd'),('负载均衡','Keepalived','grd'),('API Gateway','统一入口','grd')]),
    ('应用服务区','#2980b9','#ebf5fb',[('Web服务器×2','Vue.js+Nginx','gdb'),('API服务器×2','SpringBoot','gdb'),('消息队列','RabbitMQ','gdb'),('定时任务','XXL-Job','gdb')]),
    ('数据存储区','#16a085','#e8f8f5',[('MySQL 8.0','主从集群','gte'),('Redis','缓存集群','gte'),('Elasticsearch','搜索引擎','gte'),('MinIO','对象存储','gte')]),
])

# 10 — 图3.4 风险评分
flow_diagram('图3-4-风险_baoyu.svg', '风险评分模型', [
    ('信用分','0~100 / W=40%','gdb'),('违规分','0~-30 / W=25%','grd'),
    ('安全分','0~-20 / W=20%','gor'),('走访分','0~-10 / W=15%','gte'),
])

# 11 — 图3-7 视频关联算法
flow_diagram('图3-7_baoyu.svg', '图3-7 视频与商户智能关联算法', [
    ('1.候选筛选','200m半径','gdb'),('2.视角判断','|theta|<=V/2','gmb'),
    ('3.关联评分','1/distance','gte'),('4.排序','取最优3个','ggr'),('5.反向索引','商户↔摄像头','gor'),
])

# 12 — 图3-6 数据安全
layered_diagram('图3-6_安全_baoyu.svg', '数据安全管控体系', [
    ('安全措施','#e74c3c','#fdedec',[('最小必要原则','仅开放必需字段','grd'),('脱敏展示','手机138****1234','grd'),('全链路审计','>=180天日志','grd'),('分级权限','四级角色控制','grd'),('数据不落地','按需查询 不持久化','grd')]),
])

# 13 — 技术选型
flow_diagram('技术选型_baoyu.svg', '项目技术选型总览', [
    ('前端','Vue.js/React','gdb'),('可视化','ECharts/D3','gmb'),('地图','天地图·山东','gte'),
    ('后端','SpringBoot','ggr'),('数据库','MySQL/达梦','gor'),('移动端','uni-app','gpr'),
])

# 14 — 图3-4 三步流程
flow_diagram('图3-4_baoyu.svg', '图3-4 走访录入三步流程', [
    ('第1步\n选择商户','扫码/地图/搜索','gdb'),('第2步\n填写结果','检查/拍照/录入','gte'),('第3步\n提交完成','上传/更新/返回','ggr'),
])

# 15 — 图3-1 商户全景
three_col('图3-1_baoyu.svg', '图3-1 商户全景信息图谱',
    [('张记餐馆 AAA·蓝','餐饮服务','ggr'),('李氏五金 B·黄','五金零售','gor'),('顺发超市 A·蓝','批发零售','ggr'),('便民药店 C·红','药品销售','grd')],
    ['商户详情卡片\n信用代码: 371082****0001\n地址: 荣成市XX路XX号\n信用等级: AAA | 风险: 低'],
    [('数据来源','市监局·住建局','gdb'),('经营状态','正常营业','ggr'),('最近走访','2026-06-10','gmb'),('视频监控','3个关联摄像头','gte')])

# 16 — 图3-2 数据结构
three_col('图3-2_baoyu.svg', '图3-2 商户全景信息图谱数据结构',
    [('自然资源局','用地信息','gdb'),('住建局','房屋信息','gmb'),('市场监管局','信用信息','gte'),('综合执法局','执法信息','gor')],
    ['商户基础信息表\nmerchant_base\n主键: 统一社会信用代码'],
    [('merchant_land','用地信息','gte'),('merchant_house','房屋信息','gte'),('merchant_credit','信用信息','gte'),('merchant_enforce','执法信息','gte')])

# 17 — 图3-5 移动端
flow_diagram('图3-5_baoyu.svg', '图3-5 走访录入页面布局 移动端', [
    ('选择商户','扫码/地图/列表','gdb'),('填写结果','检查/拍照/语音','gte'),('提交确认','自动上传/任务更新','ggr'),
])

# 18 — 附图9-1 零碳大脑驾驶舱
layered_diagram('附图9-1_baoyu.svg', '附图9-1 零碳大脑驾驶舱界面示意', [
    ('核心指标区','#2980b9','#ebf5fb',[('碳排放总量','XX 万吨','gdb'),('单位GDP碳排','X.XX t/万元','gdb'),('清洁能源占比','XX%','gdb'),('减排目标完成','XX%','gdb')]),
    ('分析区','#16a085','#e8f8f5',[('碳排放趋势','近5年','gte'),('结构分解','饼图','gte'),('重点排放源','TOP5','gte'),('碳汇资源','海洋/林业','gte')]),
    ('项目区','#27ae60','#e9f7ef',[('减排项目','台账管理','ggr'),('新能源态势','光伏/风电','ggr'),('碳汇计量','核算体系','ggr'),('数据校验','采集网络','ggr')]),
])

print("\n✅ 18个SVG文件生成完成")
