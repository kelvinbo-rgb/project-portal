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

# Custom CSS for aesthetics & Hide Streamlit Branding
st.markdown("""
<style>
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
    }
    
    /* Project Card */
    .project-card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        transition: transform 0.3s;
        height: 100%;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    
    /* Typography */
    .card-title {
        font-weight: 800;
        margin-bottom: 0.5rem;
        font-size: 1.2rem;
        line-height: 1.4;
    }
    .card-desc {
        color: #666;
        font-size: 0.9rem;
        margin-top: 10px;
        margin-bottom: 15px;
        line-height: 1.5;
    }
    
    /* Launch Button */
    .launch-btn {
        display: inline-block;
        padding: 8px 20px;
        color: white !important;
        text-decoration: none;
        border-radius: 50px;
        font-weight: bold;
        text-align: center;
        width: 100%;
        transition: opacity 0.2s;
        box-shadow: 0 2px 5px rgba(0,0,0,0.15);
    }
    .launch-btn:hover {
        opacity: 0.9;
    }

    /* Hero Section */
    .hero-title {
        background: -webkit-linear-gradient(45deg, #333, #666);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 2.5em;
        text-align: center;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Hero
st.markdown("<h1 class='hero-title'>✨ Kelvin's App Suite</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888; margin-bottom: 40px;'>Explore Intelligent Tools / 探索智能工具 / สำรวจเครื่องมืออัจฉริยะ</p>", unsafe_allow_html=True)

# Projects Data with Themes & Images
projects = [
    {
        "t_en": "Thai Gold", "t_cn": "泰国黄金", "t_th": "ทองคำไทย",
        "desc": "Real-time gold monitor / 实时监控金价 / ราคาทองคำเรียลไทม์",
        "url": "https://thai-gold-marjfazaj6s7kkvvbqrj6g.streamlit.app/",
        "icon": "🥇", "color": "#FFD700", # Gold
        "img": "https://via.placeholder.com/300x150/FFFAFA/DAA520?text=Gold+Monitor+Preview" # Placeholder
    },
    {
        "t_en": "Thai Lottery", "t_cn": "泰国彩票", "t_th": "หวยไทย",
        "desc": "AI number predictor / AI 彩票预测 / ทำนายเลขหวย AI",
        "url": "https://thai-lottery-predictor-pbh3eacsmrwe9n73mew8w2.streamlit.app/",
        "icon": "🎰", "color": "#FF6B6B", # Red
        "img": "https://via.placeholder.com/300x150/FFF0F0/FF6B6B?text=AI+Lottery+Preview"
    },
    {
        "t_en": "Grade 2 Writing", "t_cn": "二年级写字表", "t_th": "ฝึกเขียนไทย",
        "desc": "Digital writing practice / 电子写字表 / ตารางฝึกเขียน",
        "url": "https://kelvinbo-rgb.github.io/Year2.1-Chinese/",
        "icon": "✍️", "color": "#4ECDC4", # Teal
        "img": "https://via.placeholder.com/300x150/F0FFFE/4ECDC4?text=Writing+Table+Preview"
    },
    {
        "t_en": "Tarot Spreads", "t_cn": "塔罗牌阵", "t_th": "ไพ่ยิปซี",
        "desc": "Daily guidance / 每日指引 / ดูดวงรายวัน",
        "url": "https://kelvinbo-rgb.github.io/hong-tarot/TAROT.html",
        "icon": "🔮", "color": "#9b59b6", # Purple
        "img": "https://via.placeholder.com/300x150/FAF5FF/9b59b6?text=Tarot+Reading+Preview"
    }
]

# Grid Layout
cols = st.columns(2)

for i, p in enumerate(projects):
    col = cols[i % 2]
    with col:
        # Use HTML card for maximum styling control
        with st.container(border=True):
            c1, c2 = st.columns([1, 1.5])
            
            with c1:
                # QR Code on Top Left
                st.image(QRGenerator.generate(p['url']), width=130)
            
            with c2:
                # Trilingual Title (Stacked)
                st.markdown(f"""
                <div style="color:{p['color']}; margin-bottom:10px;">
                    <div style="font-weight:900; font-size:1.1em;">{p['icon']} {p['t_en']}</div>
                    <div style="font-weight:700; font-size:1em; opacity:0.9;">{p['t_cn']}</div>
                    <div style="font-weight:400; font-size:0.9em; opacity:0.8;">{p['t_th']}</div>
                </div>
                """, unsafe_allow_html=True)
                
                # Custom Colored Button
                st.markdown(f"""
                <a href="{p['url']}" target="_blank" class="launch-btn" style="background-color: {p['color']};">
                   🚀 Launch / 启动
                </a>
                """, unsafe_allow_html=True)

            # Description below
            st.markdown(f"<div class='card-desc'>{p['desc']}</div>", unsafe_allow_html=True)
            
            # Preview Image (Clickable if possible? No, just visual)
            st.image(p['img'], use_container_width=True)

st.divider()

# --- SPONSORSHIP SECTION ---
st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <h3 style="color: #666;">☕ Support Innovation / 赞助作者 / สนับสนุน</h3>
    <p style="color: #888; font-size: 0.9em;">
        If these tools help you, buy me a coffee! <br>
        您的支持是我持续更新的动力。
    </p>
</div>
""", unsafe_allow_html=True)

spam_col1, spam_col2, spam_col3 = st.columns([1,1,1])

# Placeholder QR codes for sponsorship - Users should replace these images
with spam_col2:
    st.image("https://via.placeholder.com/150?text=Sponsor+QR", width=150, caption="Scan to Support")

st.markdown("""
<div style="text-align: center; color: #aaa; font-size: 0.8em; margin-top: 30px;">
    <p>May your dreams come true. / 祝终有一日你我梦想成真</p>
    <p>© 2025 AI App Suite</p>
</div>
""", unsafe_allow_html=True)
