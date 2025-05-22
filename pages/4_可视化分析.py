import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import io

st.header("📈 可视化分析与导出")
df = st.session_state.get("df")
if df is not None:
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    cat_cols = df.select_dtypes(include='object').columns.tolist()
    st.subheader("自动图表推荐")
    col = st.selectbox("选择字段", df.columns)
    if col in numeric_cols:
        fig = px.histogram(df, x=col, nbins=30, title=f"{col} 分布图")
    elif col in cat_cols:
        vc = df[col].value_counts().reset_index()
        vc.columns = [col, 'count']
        fig = px.bar(vc, x=col, y='count', title=f"{col} 分类频数")
    else:
        fig = px.histogram(df, x=col, title=f"{col} 分布图")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("图表导出")
    fig_bytes = fig.to_image(format="png")
    st.download_button("📤 下载图表为 PNG", data=fig_bytes, file_name="chart.png")
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📤 下载数据为 CSV", data=csv, file_name="data.csv")
    excel_buf = io.BytesIO()
    max_rows = 1048575  # Excel最大行数-1，防止header+数据超限
    if len(df) > max_rows:
        st.warning(f"数据行数超出Excel单表最大限制（1048576行），仅导出前{max_rows}行。")
        df.iloc[:max_rows].to_excel(excel_buf, index=False, engine='openpyxl')
    else:
        df.to_excel(excel_buf, index=False, engine='openpyxl')
    excel_buf.seek(0)
    st.download_button("📤 下载数据为 Excel", data=excel_buf, file_name="data.xlsx")
else:
    st.warning("请先上传数据")
