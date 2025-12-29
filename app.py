import streamlit as st
from utils import QRGenerator

# Page Config
st.set_page_config(
    page_title="Kelvin's App Collection",
    page_icon="🚀",
    layout="wide"
)

import streamlit as st
from utils import QRGenerator

# Page Config
st.set_page_config(
    page_title="Kelvin's App Collection",
    page_icon="🚀",
    layout="wide"
)

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

# Page Config
st.set_page_config(
    page_title="Kelvin's AI Hub",
    page_icon="🔮",
    layout="wide"
)

# Custom Styling (The WOW Factor)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&display=swap');

    /* Hide Streamlit Stuff */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Premium Dark Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        font-family: 'Outfit', sans-serif;
    }
    
    /* Floating Particles Effect */
    .stApp::before {
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
    }
    
    /* Responsive Hero Title - Light on Dark */
    .hero-title {
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
    }
    @keyframes shine {
        to { background-position: 200% center; }
    }
    
    .hero-subtitle {
        text-align: center; 
        color: rgba(255,255,255,0.7); 
        margin-bottom: 50px; 
        font-size: 1.1em;
        font-weight: 400;
    }

    /* Glassmorphism Card - Normal Size */
    .html-card {
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
    }
    .html-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.12);
        background: rgba(255, 255, 255, 0.75);
    }
    
    /* Background watermark effect */
    .bg-image-watermark {
        position: absolute;
        top: -10px;
        right: -10px;
        width: 140px;
        opacity: 0.15;
        transform: rotate(15deg);
        pointer-events: none;
        z-index: 0;
    }
    .bg-icon-watermark {
        position: absolute;
        top: -10px;
        right: -10px;
        font-size: 6em;
        opacity: 0.08;
        transform: rotate(15deg);
        pointer-events: none;
    }

    .card-header {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 20px;
        position: relative;
        z-index: 2;
    }
    
    .qr-container {
        flex: 0 0 100px; 
        width: 100px;
        background: white;
        padding: 5px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03);
    }
    .qr-img { width: 100%; border-radius: 8px; }
    
    .info-container { flex: 1; min-width: 0; }
    
    .launch-btn {
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
    }
    .launch-btn:hover {
        opacity: 0.9;
        filter: brightness(1.05);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }

    .desc-box {
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
    }

    /* Contact Section Premium */
    .contact-card {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 30px;
        margin-top: 40px;
        border: 1px solid rgba(255,255,255,0.15);
    }
    
    .contact-title {
        font-weight: 900;
        font-size: clamp(1.3rem, 4vw, 2rem); 
        margin-bottom: 5px;
        color: #ffffff;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }
    .contact-subtitle {
        font-size: 0.9em;
        color: #e0e0e0;
        margin-bottom: 20px;
        letter-spacing: 1px;
    }
    
    /* Section Headers on Dark BG - Bright White */
    .section-header {
        color: #ffffff;
        font-weight: 900;
        text-shadow: 0 2px 10px rgba(0,0,0,0.3);
    }
    .section-subheader {
        color: #e0e0e0;
    }
    
    /* Contact Labels - Bright on Dark */
    .contact-label {
        color: #fff !important;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .email-link {
        color: #7dd3fc !important;
        text-decoration: none;
        font-weight: bold;
    }
    .email-link:hover {
        color: #38bdf8 !important;
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# Hero Header
st.markdown("<h1 class='hero-title'>BO-LAB: AI HUB</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-subtitle'>Premium Intelligence Workspace / 个人智选应用空间 / พื้นที่แอปพลิเคชันอัจฉริยะ</p>", unsafe_allow_html=True)

# Projects Data
projects = [
    {
        "t_en": "Thai Gold", "t_cn": "泰国黄金", "t_th": "ทองคำไทย",
        "desc_en": "Professional monitoring of Thai gold market and FOREX rates.",
        "desc_cn": "实时监控泰国金价与汇率，内置专业的投资盈亏计算器。",
        "desc_th": "ติดตามราคาทองคำและอัตราแลกเปลี่ยน พร้อมคำนวณกำไร/ขาดทุน",
        "url": "https://thai-gold-marjfazaj6s7kkvvbqrj6g.streamlit.app/",
        "icon": "🥇", "color": "#f1c40f", "bg": "#FFFDF0"
    },
    {
        "t_en": "Thai Lottery", "t_cn": "泰国彩票", "t_th": "หวยไทย",
        "desc_en": "Advanced AI statistical model for lottery number predictions.",
        "desc_cn": "基于历史大数据的 AI 彩票预测工具，可视化分析中奖趋势。",
        "desc_th": "เครื่องมือทำนายเลขหวยด้วย AI จากสถิติย้อนหลังและวิเคราะห์แนวโน้ม",
        "url": "https://thai-lottery-predictor-pbh3eacsmrwe9n73mew8w2.streamlit.app/",
        "icon": "🎰", "color": "#e74c3c", "bg": "#FFF0F0"
    },
    {
        "t_en": "Grade 2 Writing", "t_cn": "二年级写字表", "t_th": "ฝึกเขียนไทย",
        "desc_en": "Supportive digital writing practice for school students.",
        "desc_cn": "小学语文二年级上册电子写字表，随时随地练习笔画与发音。",
        "desc_th": "ตารางฝึกเขียนแบบดิจิทัลสำหรับนักเรียนประถม ฝึกฝนได้ทุกที่ทุกเวลา",
        "url": "https://kelvinbo-rgb.github.io/Year2.1-Chinese/",
        "icon": "✍️", "color": "#1abc9c", "bg": "#F0FFFE"
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
        "desc_en": "Enterprise PromptPay cashier system with slip verification. [Paid Project]",
        "desc_cn": "【付费项目】商业级 PromptPay 收银与回执核验系统。点击启动按钮免费体验。",
        "desc_th": "ระบบ PromptPay รับชำระและตรวจสลิปอัตโนมัติ [โปรเจกต์เชิงพาณิชย์ - มีตัวอย่างให้ลอง]",
        "url": "https://pp-pay-production.up.railway.app/?mid=DEMO",
        "icon": "💳", "color": "#27ae60", "bg": "#F4FFF8",
        "local_icon": "PromptPay.png"
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
            import base64 as b64lib
            with open(p["local_icon"], "rb") as img_file:
                icon_b64 = b64lib.b64encode(img_file.read()).decode()
            watermark_html = f'<img src="data:image/png;base64,{icon_b64}" class="bg-image-watermark">'

        html_content = (
            f'<div class="html-card" style="background: rgba(255,255,255,0.82);">{watermark_html}'
            f'<div class="card-header">'
            f'<div class="qr-container"><img src="data:image/png;base64,{qr_b64}" class="qr-img"></div>'
            f'<div class="info-container">'
            f'<div style="font-size: 1.8em; margin-bottom: 2px;">{p["icon"]}</div>'
            f'<div style="color:{p["color"]}; font-weight:900; font-size:1.4em; line-height:1.2;">{p["t_en"]}</div>'
            f'<div style="color:#222; font-weight:700; font-size:1.1em; line-height:1.3;">{p["t_cn"]}</div>'
            f'<div style="color:#666; font-weight:400; font-size:0.9em;">{p["t_th"]}</div>'
            f'</div></div>'
            f'<a href="{p["url"]}" target="_blank" class="launch-btn" style="background-color: {p["color"]};">'
            f'LAUNCH / 立即启动 / เริ่มต้น</a>'
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
<div style="text-align: center; margin-bottom: 30px;">
    <h1 class="section-header">☕ COFFEE BREAK</h1>
    <p class="section-subheader">Your support keeps these free tools alive! / 您的支持是我持续更新的最大的动力。</p>
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
