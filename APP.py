import streamlit as st

st.set_page_config(page_title="增强版数据分析仪表盘", layout="wide", page_icon="📊")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.sidebar.image("https://img.icons8.com/color/96/000000/combo-chart--v2.png", width=80)
st.sidebar.title("📊 数据分析仪表盘")
st.sidebar.markdown("---")
st.sidebar.caption("© 2025 QXY")

st.markdown("""
# 欢迎使用增强版数据分析仪表盘

请通过左侧菜单选择功能页面进行数据分析。
""")
# 不再手动添加 page_link，避免和 Streamlit 自动导航重复
