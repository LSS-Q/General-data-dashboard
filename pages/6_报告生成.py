import streamlit as st
from jinja2 import Template
import datetime

st.header("📝 自动生成 HTML 报告")
df = st.session_state.get("df")
if df is not None:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    html_template = Template("""
    <html>
    <head><title>数据分析报告</title></head>
    <body style="font-family:sans-serif;">
        <h1>数据分析报告</h1>
        <p>生成时间：{{ time }}</p>
        <h2>字段列表</h2>
        <ul>
        {% for col in columns %}
            <li>{{ col }}</li>
        {% endfor %}
        </ul>
        <h2>描述性统计</h2>
        {{ summary }}
    </body>
    </html>
    """)
    html = html_template.render(time=now, columns=df.columns.tolist(), summary=df.describe().to_html(classes="table"))
    st.download_button("📄 下载 HTML 报告", data=html, file_name="report.html", mime="text/html")
    import streamlit.components.v1 as components
    components.html(html, height=400, scrolling=True)
else:
    st.warning("请先上传数据")
