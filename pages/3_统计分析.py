import streamlit as st

st.header("📊 数据描述性统计分析")
df = st.session_state.get('df')
if df is not None:
    st.subheader("字段名")
    st.write(list(df.columns))
    st.subheader("描述性统计")
    st.write(df.describe(include='all'))
else:
    st.warning("请先上传数据")
