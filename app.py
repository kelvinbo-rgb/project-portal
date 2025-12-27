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
    page_title="Kelvin's App Collection",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for aesthetics & Hide Streamlit Branding
st.markdown("""
<style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global Styles */
    .stApp {
        background: #f8f9fa;
    }
    
    /* Typography */
    .hero-title {
        background: -webkit-linear-gradient(45deg, #333, #666);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 2.5em;
        text-align: center;
        margin-top: 20px;
    }
    
    /* HTML Card Styles */
    .html-card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        border: 1px solid #eee;
    }
    
    /* Flex Container for QR + Info */
    .card-header {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
        gap: 15px;
    }
    
    .qr-container {
        flex: 0 0 110px; /* Fixed width for QR */
        width: 110px;
    }
    .qr-img {
        width: 100%;
        border-radius: 8px;
        border: 1px solid #f0f0f0;
    }
    
    .info-container {
        flex: 1; /* Take remaining space */
        min-width: 0; /* Prevent overflow */
    }
    
    /* Button Style */
    .launch-btn {
        display: block;
        padding: 10px 0;
        color: white !important;
        text-decoration: none;
        border-radius: 10px;
        font-weight: bold;
        text-align: center;
        width: 100%;
        margin-top: 15px;
        font-size: 0.95em;
        box-shadow: 0 3px 5px rgba(0,0,0,0.1);
    }
    .launch-btn:hover {
        opacity: 0.9;
        text-decoration: none;
    }

    /* Description Box */
    .desc-box {
        background-color: #fafafa;
        border-radius: 8px;
        padding: 12px;
        margin-top: 12px;
        font-size: 0.85em;
        color: #555;
        line-height: 1.5;
        border-left: 3px solid #ddd;
    }
</style>
""", unsafe_allow_html=True)

# Hero
st.markdown("<h1 class='hero-title'>✨ Kelvin's App Suite</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; margin-bottom: 40px;'>Explore Intelligent Tools / 探索智能工具 / สำรวจเครื่องมืออัจฉริยะ</p>", unsafe_allow_html=True)

# Projects Data
projects = [
    {
        "t_en": "Thai Gold", "t_cn": "泰国黄金", "t_th": "ทองคำไทย",
        "desc_en": "Track live Thai gold prices & exchange rates. Calculate profit/loss instantly.",
        "desc_cn": "实时监控泰国金价与汇率，内置专业的投资盈亏计算器。",
        "desc_th": "ติดตามราคาทองคำและอัตราแลกเปลี่ยนแบบเรียลไทม์ พร้อมคำนวณกำไร/ขาดทุน",
        "url": "https://thai-gold-marjfazaj6s7kkvvbqrj6g.streamlit.app/",
        "icon": "🥇", "color": "#FFD700", "bg": "#FFFDF0"
    },
    {
        "t_en": "Thai Lottery", "t_cn": "泰国彩票", "t_th": "หวยไทย",
        "desc_en": "AI-powered number predictor based on historical statistics and trend analysis.",
        "desc_cn": "基于历史大数据的 AI 彩票预测工具，可视化分析中奖趋势。",
        "desc_th": "เครื่องมือทำนายเลขหวยด้วย AI จากสถิติย้อนหลังและวิเคราะห์แนวโน้ม",
        "url": "https://thai-lottery-predictor-pbh3eacsmrwe9n73mew8w2.streamlit.app/",
        "icon": "🎰", "color": "#FF6B6B", "bg": "#FFF0F0"
    },
    {
        "t_en": "Grade 2 Writing", "t_cn": "二年级写字表", "t_th": "ฝึกเขียนไทย",
        "desc_en": "Digital interactive writing table for primary students. Practice anytime.",
        "desc_cn": "小学语文二年级上册电子写字表，随时随地练习笔画与发音。",
        "desc_th": "ตารางฝึกเขียนแบบดิจิทัลสำหรับนักเรียนชั้นประถม ฝึกฝนได้ทุกที่ทุกเวลา",
        "url": "https://kelvinbo-rgb.github.io/Year2.1-Chinese/",
        "icon": "✍️", "color": "#4ECDC4", "bg": "#F0FFFE"
    },
    {
        "t_en": "Tarot Spreads", "t_cn": "塔罗牌阵", "t_th": "ไพ่ยิปซี",
        "desc_en": "Start your day with spiritual guidance. Interactive card spreads for insights.",
        "desc_cn": "每日塔罗指引，交互式牌阵帮助您探索内心，寻找生活启示。",
        "desc_th": "เริ่มต้นวันใหม่ด้วยคำทำนาย ไพ่ยิปซีเพื่อค้นหาคำตอบและแนวทางชีวิต",
        "url": "https://kelvinbo-rgb.github.io/hong-tarot/TAROT.html",
        "icon": "🔮", "color": "#9b59b6", "bg": "#FAF5FF"
    }
]

# Grid Layout
cols = st.columns(2)

for i, p in enumerate(projects):
    col = cols[i % 2]
    with col:
        # Generate QR base64
        qr_img = QRGenerator.generate(p['url'])
        qr_b64 = pil_to_base64(qr_img)
        
        # Pure HTML Card to guarantee layout on Mobile
        # Pure HTML Card - Minified to prevent Markdown parsing issues
        # We construct a single line string to avoid any indentation or newline interpretation by Markdown
        html_content = (
            f'<div class="html-card">'
            f'<div class="card-header">'
            f'<div class="qr-container"><img src="data:image/png;base64,{qr_b64}" class="qr-img"></div>'
            f'<div class="info-container">'
            f'<div style="font-size: 2em; line-height: 1; margin-bottom: 5px;">{p["icon"]}</div>'
            f'<div style="color:{p["color"]}; font-weight:900; font-size:1.15em; line-height:1.2;">{p["t_en"]}</div>'
            f'<div style="color:#555; font-weight:700; font-size:1em; line-height:1.3;">{p["t_cn"]}</div>'
            f'<div style="color:#888; font-weight:400; font-size:0.9em;">{p["t_th"]}</div>'
            f'</div></div>'
            f'<a href="{p["url"]}" target="_blank" class="launch-btn" style="background-color: {p["color"]};">'
            f'🚀 Launch / 启动 / เริ่มต้น</a>'
            f'<div class="desc-box" style="background-color: {p["bg"]}; border-left-color: {p["color"]};">'
            f'<b>{p["desc_en"]}</b><br>'
            f'<span style="font-size:0.9em; opacity:0.9;">{p["desc_cn"]}</span><br>'
            f'<span style="font-size:0.85em; opacity:0.85;">{p["desc_th"]}</span>'
            f'</div></div>'
        )
        st.markdown(html_content, unsafe_allow_html=True)

st.divider()

# --- SPONSORSHIP SECTION ---
st.markdown("""
<div style="text-align: center; margin-bottom: 30px;">
    <h3 style="color: #666;">☕ Support Innovation / 赞助作者 / สนับสนุน</h3>
    <p style="color: #888; font-size: 0.9em;">
        Your support keeps these free tools alive! <br>
        您的支持是我持续更新的最大的动力。
    </p>
</div>
""", unsafe_allow_html=True)

s1, s2 = st.columns(2)
with s1:
    st.markdown("<div style='text-align: center; font-weight: bold; color: #00A1E9; margin-bottom: 10px;'>Alipay (支付宝)</div>", unsafe_allow_html=True)
    if os.path.exists("qr_alipay.jpg"):
        st.image("qr_alipay.jpg", width=200, use_container_width=False)
    else:
        st.image("https://via.placeholder.com/200?text=Alipay", width=200)

with s2:
    st.markdown("<div style='text-align: center; font-weight: bold; color: #153e7e; margin-bottom: 10px;'>PromptPay (Thai)</div>", unsafe_allow_html=True)
    if os.path.exists("qr_promptpay.jpg"):
        st.image("qr_promptpay.jpg", width=200, use_container_width=False)
    else:
        st.image("https://via.placeholder.com/200?text=PromptPay", width=200)

# --- CONTACT FOOTER ---
st.markdown("""
<br>
<hr>
<div style="text-align: center; color: #666; font-size: 0.9em; margin-top: 20px; line-height: 1.8;">
    <p style="margin-bottom: 15px;"><b>Contact Me / 联系方式</b></p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([1,1,1])

with c1:
    st.markdown("<div style='text-align: center;'>💬 WeChat</div>", unsafe_allow_html=True)
    if os.path.exists("WeChat.jpg"):
        st.image("WeChat.jpg", width=120, use_container_width=False)
    else:
        st.markdown("<div style='text-align: center; color:#aaa;'>WeChat: kelvinbo</div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div style='text-align: center;'>💚 Line</div>", unsafe_allow_html=True)
    if os.path.exists("Line.jpg"):
        st.image("Line.jpg", width=120, use_container_width=False)
    else:
        st.markdown("<div style='text-align: center; color:#aaa;'>Line: kelvinbo</div>", unsafe_allow_html=True)

with c3:
    st.markdown("<div style='text-align: center;'>📧 Email</div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; margin-top: 40px;'><a href='mailto:kelvinbo@gmail.com'>kelvinbo@gmail.com</a></div>", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; color: #aaa; font-size: 0.8em; margin-top: 30px;">
    <p>May your dreams come true. / 祝终有一日你我梦想成真</p>
    <p>© 2025 AI App Suite</p>
</div>
""", unsafe_allow_html=True)
