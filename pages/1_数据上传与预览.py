import streamlit as st
from utils.data_loader import load_data
from utils.preprocess import clean_object_datetime

st.header("📁 数据上传与预览")
uploaded_file = st.file_uploader("请上传CSV文件", type=["csv"])
if uploaded_file:
    df = load_data(uploaded_file)
    df = clean_object_datetime(df)
    st.session_state['df'] = df
    st.success(f"成功加载数据，共 {df.shape[0]} 行, {df.shape[1]} 列")
    st.write("字段名：", list(df.columns))
    st.dataframe(df.head(50), use_container_width=True)
else:
    st.info("请上传CSV文件以开始分析")
