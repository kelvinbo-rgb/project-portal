import streamlit as st
from utils import QRGenerator

# Page Config
st.set_page_config(
    page_title="Kelvin's App Collection",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS for cards
st.markdown("""
<style>
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
        border: 1px solid #f0f0f0;
        transition: transform 0.2s;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }
    .title {
        color: #333;
        font-size: 1.2em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .desc {
        color: #666;
        font-size: 0.9em;
        margin-bottom: 15px;
        height: 60px;
        overflow: hidden;
    }
</style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<h1 style='text-align: center; color: #333;'>🚀 AI-Powered App Collection</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; margin-bottom: 50px;'>Explore our suite of intelligent tools designed for daily life.</p>", unsafe_allow_html=True)

# Projects Data
projects = [
    {
        "title": "🥇 Thai Gold / 泰国黄金",
        "desc": "Real-time gold prices and exchange rate monitoring tool. / 实时监控泰国金价与汇率。",
        "url": "https://thai-gold-marjfazaj6s7kkvvbqrj6g.streamlit.app/",
        "icon": "💰"
    },
    {
        "title": "🎰 Thai Lottery / 泰国彩票",
        "desc": "AI-powered lottery number predictor and historical analysis. / AI 驱动的泰国彩票预测工具。",
        "url": "https://thai-lottery-predictor-pbh3eacsmrwe9n73mew8w2.streamlit.app/",
        "icon": "🎲"
    },
    {
        "title": "✍️ Grade 2 Chinese / 二年级写字表",
        "desc": "Digital writing practice table for primary school students. / 小学语文二年级上册电子写字表。",
        "url": "https://kelvinbo-rgb.github.io/Year2.1-Chinese/",
        "icon": "📝"
    },
    {
        "title": "🔮 Tarot Spreads / 塔罗牌阵",
        "desc": "Interactive Tarot card spreads for daily guidance. / 每日塔罗牌阵指引。",
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
            st.markdown(f"*{p['desc']}*")
            
            # QR Code
            c1, c2 = st.columns([1, 2])
            with c1:
                st.image(QRGenerator.generate(p['url']), width=120)
            with c2:
                st.markdown("<br>", unsafe_allow_html=True)
                st.link_button("🚀 Launch App", p['url'], use_container_width=True)
                st.code(p['url'], language=None)

st.divider()

# Footer
st.markdown("""
<div style="text-align: center; color: #888; padding: 20px;">
    <h4>💡 Created with AI Power</h4>
    <p>Free forever & Open for everyone</p>
    <p>永久免费 · 欢迎收藏</p>
</div>
""", unsafe_allow_html=True)
