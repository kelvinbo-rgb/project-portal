import streamlit as st
from utils import QRGenerator
import os
import base64
import io

# Helper to convert PIL image to base64 for HTML embedding
def pil_to_base64(img):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# --- LINK PREVIEW (SEO/OG TAGS) ---
TITLE = "BO-LAB: AI Hub | 个人智选应用空间"
DESCRIPTION = "Premium Intelligence Workspace | พื้นที่แอปพลิเคชันอัจฉริยะ"

st.set_page_config(
    page_title=TITLE,
    page_icon="🔮",
    layout="wide",
)

# Meta Tag Hack for Scrapers (LINE/FB/WeChat)
# This raw HTML is placed as early as possible in the body.
st.markdown(f"""
    <div style="display:none;">
        <title>{TITLE}</title>
        <meta name="description" content="{DESCRIPTION}">
        <meta property="og:title" content="{TITLE}">
        <meta property="og:description" content="{DESCRIPTION}">
        <meta property="og:type" content="website">
    </div>
""", unsafe_allow_html=True)

# Custom Styling (The WOW Factor)
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&display=swap');

    /* Hide Streamlit Stuff */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Premium Dark Gradient Background */
    .stApp {{
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        font-family: 'Outfit', sans-serif;
    }}
    
    /* Floating Particles Effect */
    .stApp::before {{
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(circle at 20% 80%, rgba(233, 69, 96, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(243, 148, 34, 0.1) 0%, transparent 40%),
            radial-gradient(circle at 40% 40%, rgba(52, 152, 219, 0.08) 0%, transparent 30%);
        pointer-events: none;
        z-index: 0;
    }}
    
    /* Responsive Hero Title - Light on Dark */
    .hero-title {{
        background: linear-gradient(90deg, #e94560, #f39422, #e94560);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: clamp(2.5rem, 8vw, 4rem);
        text-align: center;
        margin-top: 30px;
        letter-spacing: -1.5px;
        animation: shine 3s linear infinite;
    }}
    @keyframes shine {{
        to {{ background-position: 200% center; }}
    }}
    
    .hero-subtitle {{
        text-align: center; 
        color: rgba(255,255,255,0.7); 
        margin-bottom: 50px; 
        font-size: 1.1em;
        font-weight: 400;
    }}

    /* Glassmorphism Card - Normal Size */
    .html-card {{
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        margin-bottom: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        position: relative;
        overflow: hidden;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}
    .html-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.12);
        background: rgba(255, 255, 255, 0.75);
    }}
    
    /* Background watermark effect */
    .bg-image-watermark {{
        position: absolute;
        top: -10px;
        right: -10px;
        width: 140px;
        opacity: 0.15;
        transform: rotate(15deg);
        pointer-events: none;
        z-index: 0;
    }}
    .bg-icon-watermark {{
        position: absolute;
        top: -10px;
        right: -10px;
        font-size: 6em;
        opacity: 0.08;
        transform: rotate(15deg);
        pointer-events: none;
    }}

    .card-header {{
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 20px;
        position: relative;
        z-index: 2;
    }}
    
    .qr-container {{
        flex: 0 0 100px; 
        width: 100px;
        background: white;
        padding: 5px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03);
    }}
    .qr-img {{ width: 100%; border-radius: 8px; }}
    
    .info-container {{ flex: 1; min-width: 0; }}
    
    .launch-btn {{
        display: block;
        padding: 12px 0;
        color: white !important;
        text-decoration: none !important;
        border-radius: 14px;
        font-weight: 700;
        text-align: center;
        width: 100%;
        margin-top: 20px;
        font-size: 1em;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: all 0.2s ease;
        position: relative;
        z-index: 3;
    }}
    .launch-btn:hover {{
        opacity: 0.9;
        filter: brightness(1.05);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }}

    .desc-box {{
        background-color: rgba(245, 245, 245, 0.8);
        border-radius: 12px;
        padding: 12px;
        margin-top: 12px;
        font-size: 0.85em;
        color: #444;
        line-height: 1.5;
        border-left: 3px solid #ddd;
        position: relative;
        z-index: 2;
    }}

    /* Contact Section Premium */
    .contact-card {{
        background: rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 30px;
        margin-top: 40px;
        border: 1px solid rgba(255,255,255,0.15);
    }}
    
    .contact-title {{
        background: linear-gradient(90deg, #7dd3fc, #38bdf8, #7dd3fc);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: clamp(1.3rem, 4vw, 2rem); 
        margin-bottom: 5px;
        animation: shine 3s linear infinite;
    }}
    .contact-subtitle {{
        font-size: 1em;
        color: #ffffff;
        margin-bottom: 20px;
        letter-spacing: 1px;
    }}
    
    /* Section Headers on Dark BG - Vibrant Gradient */
    .section-header {{
        background: linear-gradient(90deg, #e94560, #f39422, #e94560);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        animation: shine 3s linear infinite;
    }}
    .section-subheader {{
        color: #ffffff;
        font-size: 1em;
    }}
    
    /* Contact Labels - Bright on Dark */
    .contact-label {{
        color: #fff !important;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }}
    .email-link {{
        color: #7dd3fc !important;
        text-decoration: none;
        font-weight: bold;
    }}
    .email-link:hover {{
        color: #38bdf8 !important;
        text-decoration: underline;
    }}
</style>
""", unsafe_allow_html=True)

# Hero Header
st.markdown("<h1 class='hero-title'>BO-LAB: AI HUB</h1>", unsafe_allow_html=True)
st.markdown(f"<p class='hero-subtitle'>{DESCRIPTION}</p>", unsafe_allow_html=True)

# Local Disclaimer Note
st.markdown("""
<div style="background: rgba(233,69,96,0.1); border-left: 5px solid #e94560; padding: 15px; border-radius: 10px; margin-bottom: 30px; text-align: center;">
    <p style="color: #fff; margin: 0; font-size: 0.95em;">
        🛡️ <b>NOTICE:</b> Some applications are currently running on <b>Private Local Servers</b> for demonstration only.<br>
        <b>注意：</b>部分标记为“私有运行”的应用目前仅在本地环境演示。如需使用或单独部署，请通过下方联系方式与我取得联系。<br>
        หากคุณสนใจหรือต้องการติดตั้งแอปพลิเคชันส่วนตัวเหล่านี้ กรุณาติดต่อผ่านช่องทางด้านล่าง
    </p>
</div>
""", unsafe_allow_html=True)

# Projects Data
projects = [
    {
        "t_en": "Antigravity Command Center", "t_cn": "战情指挥大屏", "t_th": "แดชบอร์ดควบคุม Antigravity",
        "desc_en": "Unified real-time dashboard monitoring Crypto, Forex, and ETF bots. Features cyber radar charts, concentric cockpit health gauges, automated Yahoo Finance fetching, and multi-currency ledger tracking.",
        "desc_cn": "独立的智能机器人战情大屏。统一监控加密货币、外汇与 ETF 机器人，提供炫酷赛博雷达图、同心圆环健康仪表盘、自适应汇率及出入金账本管理。",
        "desc_th": "แดชบอร์ดศูนย์ควบคุมบอทเทรดรวมแบบเรียลไทม์ ติดตามพอร์ตคริปโต, Forex และ ETF พร้อมแสดงผลแผนภูมิต้นไม้, เกจวัดสุขภาพ 3 มิติ และระบบบันทึกบัญชีอัตโนมัติ",
        "url": "#", "is_local": True,
        "icon": "📡", "color": "#e056fd", "bg": "#FDF2F9"
    },
    {
        "t_en": "SET Grid Bot", "t_cn": "证券网格交易 Bot", "t_th": "บอทแจ้งเตือนซื้อขายแบบ Grid",
        "desc_en": "Telegram bot for grid-style price monitoring on SET securities. Auto alerts for buy/sell/take-profit with pyramid sizing. Supports custom budget, trade recording & Excel import.",
        "desc_cn": "基于 Telegram 的证券网格交易监控机器人。自动推送买入/卖出/止盈信号，支持金字塔仓位管理、自定义预算、交易记录与 Excel 导入。",
        "desc_th": "บอท Telegram สำหรับติดตามราคาหลักทรัพย์ในตลาด SET แบบ Grid แจ้งเตือนซื้อ/ขาย/ทำกำไรอัตโนมัติ พร้อมระบบจัดการกระสุน, บันทึกการซื้อขาย และนำเข้า从 Excel",
        "url": "#", "is_local": True,
        "icon": "📈", "color": "#0984e3", "bg": "#EBF5FB"
    },
    {
        "t_en": "cTrader AI Grid Bot", "t_cn": "cTrader AI 智能外汇网格机器人", "t_th": "บอทเทรด Forex cTrader AI",
        "desc_en": "Bi-directional intelligent grid hedging for Forex (EUR/USD) with micro-lot support (0.01 lot) and leverage up to 1:500. Designed for small-capital robust arbitrage.",
        "desc_cn": "专为外汇市场（EUR/USD等）设计的智能双向对冲与轻量杠杆交易系统。支持0.01微型手起步，支持1:500高杠杆，低保证金稳健套利。",
        "desc_th": "ระบบเทรด Forex (EUR/USD) แบบ Grid อัจฉริยะสองทิศทาง รองรับ Micro-lots (0.01) เลเวอเรจสูงสุด 1:500 สำหรับทำกำไรส่วนต่างด้วยเงินทุนต่ำอย่างมั่นคง",
        "url": "#", "is_local": True,
        "icon": "💹", "color": "#2ecc71", "bg": "#EAF2F8"
    },
    {
        "t_en": "Base Flash-Strike V7", "t_cn": "Base 闪电对冲套利 V7", "t_th": "บอทจำลองทำกำไร Base Flash-Strike V7",
        "desc_en": "High-velocity multi-DEX concentrated liquidity arbitrage engine on Base Mainnet. Integrates Aerodrome Slipstream, dynamic token discovery, and optimized smart contracts.",
        "desc_cn": "部署于 Base 主网的高性能多DEX集中流动性套利系统。支持 Aerodrome Slipstream、动态 Token 发现机制与定制的 Solidity 闪电贷智能合约。",
        "desc_th": "บอทจำลองและเทรด Arbitrage บนเครือข่าย Base V7 ตรวจจับราคาส่วนต่างแบบ Real-time ระหว่าง Slipstream, Uniswap V3 และ V2 พร้อมยิงผ่านสัญญาอัจฉริยะ",
        "url": "#", "is_local": True,
        "icon": "🏹", "color": "#e74c3c", "bg": "#FDEDEC"
    },
    {
        "t_en": "Crypto Auto-Bot", "t_cn": "加密货币自动交易 Bot", "t_th": "บอทเทรดคริปโตอัตโนมัติ",
        "desc_en": "Automated trading engine for Binance TH (BTC/THB). Real-time price tracking via WebSockets, AI evaluation, and automated order execution. Features Telegram alerts and position management.",
        "desc_cn": "高效的加密货币自动交易引擎。通过 WebSockets 实时追踪价格，内置 AI 策略评估与订单执行，支持 Telegram 通知与仓位管理。",
        "desc_th": "เครื่องมือเทรดคริปโตอัตโนมัติสำหรับ Binance TH ติดตามราคาผ่าน WebSocket, ประเมินด้วย AI และส่งคำสั่งซื้อขายอัตโนมัติ พร้อมแจ้งเตือนผ่าน Telegram",
        "url": "#", "is_local": True,
        "icon": "⚡", "color": "#f39c12", "bg": "#FEF5E7"
    },
    {
        "t_en": "cTrader AI Indices Grid Bot", "t_cn": "cTrader AI 智能股指网格机器人", "t_th": "บอทเทรดดัชนี cTrader AI",
        "desc_en": "cTrader-based index grid trading engine targeting US and European stock indices (NAS100, SPX500, US30). Implements ATR-based dynamic spacing, asymmetric hedge ratios, and spread protection.",
        "desc_cn": "基于 cTrader 的股指网格交易系统。专门针对纳指 (NAS100)、标普 (SPX500) 等主流指数，支持自适应 ATR 间距、动态对冲机制及暴跌断路保护。",
        "desc_th": "บอทเทรดดัชนี cTrader แบบ Grid มุ่งเน้นดัชนีหุ้นหลัก (NAS100, SPX500, US30) พร้อมระบบปรับระยะกริดอัตโนมัติตามความผันผวน (ATR) และการป้องกันค่าสเปรด",
        "url": "#", "is_local": True,
        "icon": "🏛️", "color": "#0abde3", "bg": "#EAF9FD"
    },
    {
        "t_en": "cTrader AI Precious Metals Grid Bot", "t_cn": "cTrader AI 智能贵金属网格机器人", "t_th": "บอทเทรดโลหะมีค่า cTrader AI",
        "desc_en": "cTrader-based precious metals trading system optimized for XAUUSD (Gold). Employs micro-lot precision, symmetry indicators, and a counter-hedge riposte engine to withstand high volatility.",
        "desc_cn": "基于 cTrader 的贵金属网格交易系统。针对黄金 (XAUUSD) 的高波动特性进行深度优化，利用微型仓位控制与双向对冲利刃引擎进行稳健套利。",
        "desc_th": "บอทเทรดโลหะมีค่า (ทองคำ XAUUSD) บน cTrader ออกแบบมาสำหรับรับมือกับความผันผวนสูง ด้วยการจัดการความเสี่ยงแบบ Micro-lots และบอทคู่อะล็อกสองทิศทาง",
        "url": "#", "is_local": True,
        "icon": "🪙", "color": "#e1b12c", "bg": "#FCF8E9"
    },
    {
        "t_en": "TalkMate", "t_cn": "智能外语对话", "t_th": "TalkMate (ทอล์คเมท)",
        "desc_en": "AI-powered language learning platform. Practice Thai, Chinese, and English with an AI tutor. Connect with language exchange partners.",
        "desc_cn": "基于 AI 的外语学习平台：与 AI 导师练习泰语、汉语和英语。支持真人老师对接与语伴交流，即时沉浸式练习。",
        "desc_th": "แพลตฟอร์มเรียนภาษาด้วย AI ฝึกภาษาไทย จีน และอังกฤษกับติวเตอร์อัจฉริยะ พร้อมระบบจับคู่แลกเปลี่ยนภาษาแบบเรียลไทม์",
        "url": "https://talkmate.bolab.online",
        "icon": "🗣️", "color": "#6c5ce7", "bg": "#F5F3FF"
    },
    {
        "t_en": "Grade 2 Writing I", "t_cn": "二年级上册写字表", "t_th": "ฝึกเขียนไทย เทอม 1",
        "desc_en": "Supportive digital writing practice for school students.",
        "desc_cn": "小学语文二年级上册电子写字表，随时随地练习笔画与发音。",
        "desc_th": "ตารางฝึกเขียนแบบดิจิทัลสำหรับนักเรียนประถม ฝึกฝนได้ทุกที่ทุกเวลา",
        "url": "https://kelvinbo-rgb.github.io/Year2.1-Chinese/",
        "icon": "✍️", "color": "#1abc9c", "bg": "#F0FFFE"
    },
    {
        "t_en": "Grade 2 Writing II", "t_cn": "二年级下册写字表", "t_th": "ฝึกเขียนไทย เทอม 2",
        "desc_en": "Digital writing practice for Grade 2 (Term 2) students. Features stroke animation, pronunciation guide, and interactive quizzes.",
        "desc_cn": "小学语文二年级下册电子生字小助手，支持动态笔顺展示、标准朗读及课后小测试。",
        "desc_th": "ตารางฝึกเขียนอักษรจีนดิจิทัลสำหรับนักเรียนประถมปีที่ 2 (เทอม 2) พร้อมตัวอย่างการขีด, การออกเสียง และแบบทดสอบ",
        "url": "https://kelvinbo-rgb.github.io/Year2.2-Chinese/",
        "icon": "📖", "color": "#10ac84", "bg": "#EBFDF9"
    },
    {
        "t_en": "PEP PDF Print Helper", "t_cn": "人教版 PDF 2合1排版打印助手", "t_th": "เครื่องมือจัดหน้าหนังสือเรียนแบบ 2-in-1",
        "desc_en": "Custom Python utility to rearrange vertical standard PDF textbook pages side-by-side onto landscape A4 sheets, perfect for convenient double-page printing.",
        "desc_cn": "基于 Python 的 PDF 页面拼版排版工具。自动将竖版 PDF 课本拼接为双面 A4 横向排版，极大地节省纸张，便于家庭及移动设备直接打印。",
        "desc_th": "โปรแกรม Python สำหรับจัดหน้าไฟล์ PDF หนังสือเรียนภาษาจีนแนวตั้งให้รวมเป็น 2 หน้าบน A4 แนวนอน ช่วยให้สั่งพิมพ์สองหน้าได้ง่ายและประหยัดกระดาษ",
        "url": "#", "is_local": True,
        "icon": "🖨️", "color": "#34495e", "bg": "#F2F4F4"
    },
    {
        "t_en": "AI Store Manager", "t_cn": "AI 连锁店长 (KDS)", "t_th": "ผู้จัดการร้าน AI",
        "desc_en": "Independent AI shop manager with KDS tablet UI, AI polish & finance stats.",
        "desc_cn": "独立的 AI 门店管理助手：KDS 看板、AI 润色指令、实时 50/50 营收核算。",
        "desc_th": "ระบบจัดการร้านค้า AI อัจฉริยะ พร้อมหน้าจอ KDS, การขัดเกลาคำสั่ง และสรุปรายได้",
        "url": "https://manager.bolab.online",
        "icon": "👨‍🍳", "color": "#6c5ce7", "bg": "#F5F3FF"
    },
    {
        "t_en": "Thai Gold", "t_cn": "泰国黄金 (私有)", "t_th": "ทองคำไทย",
        "desc_en": "Professional monitoring of Thai gold market and FOREX rates. [Private Only]",
        "desc_cn": "实时监控泰国金价与汇率。该项目目前仅提供私有化部署测试。",
        "desc_th": "ติดตามราคาทองคำและอัตราแลกเปลี่ยน [สำหรับการติดตั้งส่วนตัวเท่านั้น]",
        "url": "#", "is_local": True,
        "icon": "🥇", "color": "#f1c40f", "bg": "#FFFDF0"
    },
    {
        "t_en": "Thai Lottery", "t_cn": "泰国彩票 (私有)", "t_th": "หวยไทย",
        "desc_en": "Advanced AI statistical model for lottery predictions. [Private]",
        "desc_cn": "基于历史大数据和 AI 算法的彩票预测工具。目前仅提供私有化部署。",
        "desc_th": "เครื่องมือทำนายเลขหวยด้วย AI [สำหรับการติดตั้งส่วนตัวเท่านั้น]",
        "url": "#", "is_local": True,
        "icon": "🎰", "color": "#e74c3c", "bg": "#FFF0F0"
    },
    {
        "t_en": "Tarot Spreads", "t_cn": "塔罗牌阵", "t_th": "ไพ่ยิปซี",
        "desc_en": "Spiritual guidance via card spreads with live interpretation. [Commercial Project]",
        "desc_cn": "【付费项目】每日塔罗指引，真人解析，帮助您探索内心。先免费体验吧。",
        "desc_th": "เริ่มต้นวันใหม่ด้วยคำทำนาย ไพ่ยิปซีเพื่อค้นหาคำตอบและแนวทางชีวิต",
        "url": "https://kelvinbo-rgb.github.io/hong-tarot/TAROT.html",
        "icon": "🔮", "color": "#9b59b6", "bg": "#FAF5FF"
    },
    {
        "t_en": "Thai FX Assistant", "t_cn": "泰铢汇率助手", "t_th": "ผู้ช่วยอัตราแลกเปลี่ยน",
        "desc_en": "Intelligent LINE assistant for exchange rates. Command 'Rate'.",
        "desc_cn": "泰铢汇率 AI 智导。在 LINE 中发送指令“汇率”即可获取实时兑换行情。",
        "desc_th": "ผู้ช่วยอัจฉริยะด้านอัตราแลกเปลี่ยน พิมพ์คำสั่ง 'Rate' เพื่อตรวจสอบราคาแบบทันที",
        "url": "https://line.me/R/ti/p/%40282yqodu",
        "icon": "🤖", "color": "#2980b9", "bg": "#F0F8FF"
    },
    {
        "t_en": "PP-Pay Business", "t_cn": "PromptPay 商业收银", "t_th": "ระบบ PromptPay รับชำระ",
        "desc_en": "Custom amount collection tool with automatic slip verification.",
        "desc_cn": "【付费项目】支持自定义金额的 PromptPay 收款工具，内置回执自动核验功能。",
        "desc_th": "เครื่องมือรับชำระเงินที่กำหนดราคาได้เอง พร้อมระบบตรวจสอบสลิปอัตโนมัติ",
        "url": "https://pay.bolab.online",
        "icon": "💳", "color": "#27ae60", "bg": "#F4FFF8",
        "local_icon": "PromptPay.png"
    },
    {
        "t_en": "Visa Butler", "t_cn": "智能签证管家", "t_th": "ผู้ช่วยขอวีซ่าอัจฉริยะ",
        "desc_en": "Smart alerts for Passport expiry, Visa renewals, and 90-day reporting.",
        "desc_cn": "签证与护照管家：提供护照过期、签证续签及 90 天报到自动预警提醒。",
        "desc_th": "ระบบแจ้งเตือนอัจฉริยะสำหรับพาสปอร์ต, ต่ออายุวีซ่า และรายงานตัว 90 วัน",
        "url": "https://visa.bolab.online",
        "icon": "🛂", "color": "#8e44ad", "bg": "#F5EEF8"
    },
    {
        "t_en": "Form Wizard", "t_cn": "智能表单向导 (私有)", "t_th": "ตัวช่วยสร้างแบบฟอร์ม",
        "desc_en": "Smart form generator for any purpose. [Private Only]",
        "desc_cn": "万能智能表单生成器。该项目目前仅提供私有化部署测试。",
        "desc_th": "เครื่องมือสร้างแบบฟอร์มอัจฉริยะ [สำหรับการติดตั้งส่วนตัวเท่านั้น]",
        "url": "#", "is_local": True,
        "icon": "📝", "color": "#16a085", "bg": "#E8F8F5"
    },
    {
        "t_en": "Amulet Monitor Pro", "t_cn": "佛牌监控 (AI 专业版)", "t_th": "Amulet Monitor Pro (AI)",
        "desc_en": "Advanced AI tracking with Gemini Pro. Professional dashboard & Telegram alerts.",
        "desc_cn": "基于 Gemini Pro AI 的专业佛牌监控系统。提供个人专属面板与实时推送。",
        "desc_th": "ระบบติดตามพระเครื่องอัจฉริยะด้วย AI Gemini Pro พร้อมแดชบอร์ดส่วนตัวและแจ้งเตือนผ่าน Telegram",
        "url": "http://amulet.bolab.online/",
        "icon": "🛡️", "color": "#d35400", "bg": "#FDF2E9"
    },
    {
        "t_en": "PP-Pay Global", "t_cn": "全球聚合支付 (私有)", "t_th": "ระบบรวมการชำระเงินทั่วโลก",
        "desc_en": "Enterprise payment gateway middleware. [Private Only]",
        "desc_cn": "企业级聚合支付中台。该项目目前暂停公共访问，仅供私有测试。",
        "desc_th": "ระบบรวมการชำระเงินระดับองค์กร [สำหรับการติดตั้งส่วนตัวเท่านั้น]",
        "url": "#", "is_local": True,
        "icon": "🌐", "color": "#2c3e50", "bg": "#ECF0F1"
    },
    {
        "t_en": "MyAI Local Chat", "t_cn": "本地 AI 聊天机器人", "t_th": "แชทบอท AI ท้องถิ่น",
        "desc_en": "Private AI assistant using LM Studio models and local Whisper voice transcription.",
        "desc_cn": "私有化 AI 助手，基于 LM Studio 本地模型，支持语音转文字与多语种交互。",
        "desc_th": "ผู้ช่วย AI ส่วนตัวโดยใช้โมเดล LM Studio และการถอดเสียง Whisper ท้องถิ่น",
        "url": "#", "is_local": True,
        "icon": "🛸", "color": "#6c5ce7", "bg": "#EBEDEF"
    },
    {
        "t_en": "LINE Accounting Bot", "t_cn": "LINE 记账机器人 (私有)", "t_th": "บอทบัญชี LINE",
        "desc_en": "Private accounting bot for groups with Google Sheets sync. [Private Only]",
        "desc_cn": "基于 LINE 群组的私有记账机器人。该项目目前仅供私有化演示。",
        "desc_th": "บอทบัญชีส่วนตัวในกลุ่ม LINE [สำหรับการติดตั้งส่วนตัวเท่านั้น]",
        "url": "#", "is_local": True,
        "icon": "📊", "color": "#00b900", "bg": "#ECF0F1"
    },
    {
        "t_en": "QR Menu", "t_cn": "扫码点单系统 (私有)", "t_th": "ระบบสั่งอาหาร QR",
        "desc_en": "Digital QR code menu and ordering system for restaurants. [Private Only]",
        "desc_cn": "专业餐饮扫码点单系统。目前仅供私有化部署演示。",
        "desc_th": "ระบบสั่งอาหารผ่าน QR Code [สำหรับการติดตั้งส่วนตัวเท่านั้น]",
        "url": "#", "is_local": True,
        "icon": "🍴", "color": "#e67e22", "bg": "#FBEEE6"
    }
]

# Grid Layout
cols = st.columns(2)

for i, p in enumerate(projects):
    col = cols[i % 2]
    with col:
        qr_b64 = pil_to_base64(QRGenerator.generate(p['url']))
        
        # Watermark logic - Use local image if available
        watermark_html = f'<div class="bg-icon-watermark">{p["icon"]}</div>'
        if "local_icon" in p and os.path.exists(p["local_icon"]):
            with open(p["local_icon"], "rb") as img_file:
                icon_b64 = base64.b64encode(img_file.read()).decode()
            watermark_html = f'<img src="data:image/png;base64,{icon_b64}" class="bg-image-watermark">'

        # Status Badge logic
        is_local = p.get("is_local", False)
        status_html = ""
        btn_text = "LAUNCH / 立即启动 / เริ่มต้น"
        btn_link = p['url']
        btn_style = f"background-color: {p['color']};"
        
        if is_local:
            status_html = '<div style="background: #e94560; color: white; padding: 2px 10px; border-radius: 20px; font-size: 0.7em; font-weight: 700; position: absolute; top: 20px; right: 20px; z-index: 10;">LOCAL ONLY / 私有运行</div>'
            btn_text = "CONTACT TO DEPLOY / 联系部署 / ติดต่อเรา"
            btn_link = "#contact-footer"
            btn_style = "background-color: #555; cursor: default;"

        html_content = (
            f'<div class="html-card" style="background: rgba(255,255,255,0.82);">{watermark_html}{status_html}'
            f'<div class="card-header">'
            f'<div class="qr-container"><img src="data:image/png;base64,{qr_b64}" class="qr-img"></div>'
            f'<div class="info-container">'
            f'<div style="font-size: 1.8em; margin-bottom: 2px;">{p["icon"]}</div>'
            f'<div style="color:{p["color"]}; font-weight:900; font-size:1.4em; line-height:1.2;">{p["t_en"]}</div>'
            f'<div style="color:#222; font-weight:700; font-size:1.1em; line-height:1.3;">{p["t_cn"]}</div>'
            f'<div style="color:#666; font-weight:400; font-size:0.9em;">{p["t_th"]}</div>'
            f'</div></div>'
            f'<a href="{btn_link}" target="_self" class="launch-btn" style="{btn_style}">'
            f'{btn_text}</a>'
            f'<div class="desc-box" style="border-left-color: {p["color"]};">'
            f'<b>{p["desc_en"]}</b><br>'
            f'<span style="font-size:0.95em; opacity:0.9;">{p["desc_cn"]}</span><br>'
            f'<span style="font-size:0.9em; opacity:0.8;">{p["desc_th"]}</span>'
            f'</div></div>'
        )
        st.markdown(html_content, unsafe_allow_html=True)

st.divider()

# --- SPONSORSHIP SECTION ---
st.markdown("""
<div style="text-align: center; margin-bottom: 30px; padding: 20px;">
    <h1 class="section-header">☕ BUY ME A COFFEE</h1>
    <p class="section-subheader" style="max-width: 600px; margin: 0 auto; line-height: 1.8;">
        <b>All projects here are open-source and free.</b> If they've helped you, consider buying me a coffee!<br>
        <b>本站所有工具均为开源免费。</b>如果对您有帮助，请赞赏一杯咖啡，支持我的创作！<br>
        <b>โปรเจกต์ทั้งหมดเป็น Open-Source ฟรี</b> หากชอบใจ ช่วยสนับสนุนผมสักแก้วกาแฟได้เลยครับ!
    </p>
</div>
""", unsafe_allow_html=True)

s1, s2 = st.columns(2)
with s1:
    st.markdown("<div style='text-align: center; font-weight: bold; color: #ffffff; margin-bottom: 15px;'>Alipay (支付宝)</div>", unsafe_allow_html=True)
    if os.path.exists("qr_alipay.jpg"):
        st.image("qr_alipay.jpg", width=200, use_container_width=False)
    else:
        st.image("https://via.placeholder.com/200?text=Alipay", width=200)

with s2:
    st.markdown("<div style='text-align: center; font-weight: bold; color: #ffffff; margin-bottom: 15px;'>PromptPay (Thailand)</div>", unsafe_allow_html=True)
    if os.path.exists("qr_promptpay.jpg"):
        st.image("qr_promptpay.jpg", width=200, use_container_width=False)
    else:
        st.image("https://via.placeholder.com/200?text=PromptPay", width=200)

# --- CONTACT FOOTER ---
st.markdown('<div id="contact-footer"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="contact-card">
    <div style="text-align: center; line-height: 1.5;">
        <h2 class="contact-title">READY TO CONNECT?</h2>
        <p class="contact-subtitle">联系方式 / ติดต่อเรา</p>
    </div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1.2, 1.2, 1])

with c1:
    st.markdown("<div class='contact-label'>💬 WeChat</div>", unsafe_allow_html=True)
    if os.path.exists("WeChat.jpg"):
        st.image("WeChat.jpg", width=180, use_container_width=False)
    else:
        st.markdown("<div style='text-align: center; color:#fff; font-size:0.9em;'>ID: kelvinbo</div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div class='contact-label'>💚 Line</div>", unsafe_allow_html=True)
    if os.path.exists("Line.jpg"):
        st.image("Line.jpg", width=180, use_container_width=False)
    else:
        st.markdown("<div style='text-align: center; color:#fff; font-size:0.9em;'>ID: kelvinbo</div>", unsafe_allow_html=True)

with c3:
    st.markdown("<div class='contact-label'>📧 Email</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; margin-top: 30px;'><a href='mailto:kelvinbo@gmail.com' class='email-link'>kelvinbo@gmail.com</a><br><a href='mailto:kelvinbo@outlook.com' class='email-link'>kelvinbo@outlook.com</a></div>", unsafe_allow_html=True)

st.markdown("""
<br><br>
<div style="text-align: center; color: rgba(255,255,255,0.5); font-size: 0.8em; font-weight: 400; letter-spacing: 1px;">
    DESIGNED WITH AI BY BO LAB © 2025<br>
    MAY YOUR DREAMS COME TRUE.
</div>
""", unsafe_allow_html=True)
