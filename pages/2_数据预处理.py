import streamlit as st
from utils.preprocess import handle_missing_values, clean_object_datetime

st.header("🧹 数据预处理")
df = st.session_state.get('df')
if df is not None:
    st.write("缺失值统计：")
    st.write(df.isnull().sum())
    na_method = st.radio("缺失值处理方式", ["删除含缺失值的行", "用均值填充", "用中位数填充", "用众数填充"])
    if st.button("应用缺失值处理"):
        df = handle_missing_values(df, na_method)
        df = clean_object_datetime(df)
        st.session_state['df'] = df
        st.success("缺失值处理完成！")
        st.write(df.head(20))
else:
    st.warning("请先上传数据")
