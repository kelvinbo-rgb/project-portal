import streamlit as st
from utils import QRGenerator

# Page Config
st.set_page_config(
    page_title="Kelvin's App Collection",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for aesthetics
st.markdown("""
<style>
    /* Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Card Styling */
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 20px;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background-color: #45a049;
        transform: scale(1.05);
    }
    
    div[data-testid="stContainer"] {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border: none;
        transition: transform 0.2s;
    }
    div[data-testid="stContainer"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }

    h3 {
        color: #2c3e50;
        font-weight: 700;
    }
    
    /* Decoration */
    .hero-title {
        background: -webkit-linear-gradient(45deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 3em;
        text-align: center;
        margin-bottom: 0.2em;
    }
    
    .hero-subtitle {
        color: #555;
        text-align: center;
        font-size: 1.2em;
        margin-bottom: 50px;
        font-family: 'Helvetica', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<h1 class='hero-title'>✨ Kelvin's App Suite ✨</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-subtitle'>Explore Intelligent Tools / 探索智能工具 / สำรวจเครื่องมืออัจฉริยะ</p>", unsafe_allow_html=True)

# Projects Data
projects = [
    {
        "title": "🥇 Thai Gold / 泰国黄金 / ทองคำไทย",
        "desc": "Real-time gold monitor / 实时监控金价 / ราคาทองคำเรียลไทม์",
        "url": "https://thai-gold-marjfazaj6s7kkvvbqrj6g.streamlit.app/",
        "icon": "💰"
    },
    {
        "title": "🎰 Thai Lottery / 泰国彩票 / หวยไทย",
        "desc": "AI number predictor / AI 彩票预测 / ทำนายเลขหวย AI",
        "url": "https://thai-lottery-predictor-pbh3eacsmrwe9n73mew8w2.streamlit.app/",
        "icon": "🎲"
    },
    {
        "title": "✍️ Grade 2 Writing / 二年级写字表 / ฝึกเขียนไทย",
        "desc": "Digital writing practice / 电子写字表 / ตารางฝึกเขียน",
        "url": "https://kelvinbo-rgb.github.io/Year2.1-Chinese/",
        "icon": "📝"
    },
    {
        "title": "🔮 Tarot Spreads / 塔罗牌阵 / ไพ่ยิปซี",
        "desc": "Daily guidance / 每日指引 / ดูดวงรายวัน",
        "url": "https://kelvinbo-rgb.github.io/hong-tarot/TAROT.html",
        "icon": "🃏"
    }
]

# Grid Layout
cols = st.columns(2)

for i, p in enumerate(projects):
    col = cols[i % 2]
    with col:
        with st.container(border=True):
            st.markdown(f"### {p['icon']} {p['title']}")
            st.markdown(f"_{p['desc']}_")
            
            # QR and Button
            c1, c2 = st.columns([1, 2])
            with c1:
                st.image(QRGenerator.generate(p['url']), width=120)
            with c2:
                st.markdown("<br>", unsafe_allow_html=True)
                # Trilingual Button
                st.link_button(
                    "🚀 Launch / 启动 / เริ่มต้น", 
                    p['url'], 
                    use_container_width=True
                )
                # Removed text URL display

st.divider()

# Footer
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <h4>🌟 Powered by AI & Creativity</h4>
    <p>Free for everyone / 永久免费收藏 / ฟรีตลอดไป</p>
</div>
""", unsafe_allow_html=True)
