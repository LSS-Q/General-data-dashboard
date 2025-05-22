import streamlit as st
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score, classification_report
import pandas as pd
from utils.preprocess import clean_object_datetime

st.header("🤖 模型训练与预测")
df = st.session_state.get('df')
if df is not None:
    df = clean_object_datetime(df)
    all_cols = df.select_dtypes(include=['number', 'object']).columns.tolist()
    target = st.selectbox("选择目标变量", all_cols)
    features = st.multiselect("选择特征变量", [col for col in all_cols if col != target])
    task_type = st.radio("任务类型", ["回归", "分类"])
    model_type = st.selectbox("选择模型", ["多元线性回归", "逻辑回归", "随机森林", "KNN"])

    if st.button("训练模型"):
        if target and features:
            X = df[features].copy()
            y = df[target]

            for col in X.select_dtypes(include='object').columns:
                X[col] = X[col].astype('category').cat.codes
            if y.dtype == 'object':
                y = y.astype('category').cat.codes

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            if task_type == "回归":
                model_class = {
                    "多元线性回归": LinearRegression,
                    "随机森林": RandomForestRegressor,
                    "KNN": KNeighborsRegressor
                }.get(model_type)
            else:
                model_class = {
                    "逻辑回归": LogisticRegression,
                    "随机森林": RandomForestClassifier,
                    "KNN": KNeighborsClassifier
                }.get(model_type)

            if model_class is None:
                st.error("未选择有效的模型类型，请重新选择。")
            else:
                model = model_class(max_iter=1000) if model_type == "逻辑回归" else model_class()
                model.fit(X_train, y_train)
                pred = model.predict(X_test)

                if task_type == "回归":
                    st.write(f"R²分数: {r2_score(y_test, pred):.4f}")
                    st.write(f"MSE: {mean_squared_error(y_test, pred):.4f}")
                else:
                    st.write(f"准确率: {accuracy_score(y_test, pred):.4f}")
                    st.text(classification_report(y_test, pred))

                st.subheader("特征解释：")
                if hasattr(model, "coef_"):
                    coef = model.coef_
                    if hasattr(coef, "ndim") and coef.ndim > 1:
                        coef = coef[0]
                    st.write("特征系数:")
                    st.write(pd.DataFrame({'特征': features, '系数': coef}))
                elif hasattr(model, "feature_importances_"):
                    st.write("特征重要性:")
                    st.write(pd.DataFrame({'特征': features, '重要性': model.feature_importances_}))
                else:
                    st.info("该模型不支持特征系数或特征重要性解释。")

                st.subheader("📥 批量预测上传")
                batch_file = st.file_uploader("上传CSV进行预测", type=["csv"])
                if batch_file:
                    batch_df = pd.read_csv(batch_file)
                    for col in batch_df.select_dtypes(include='object').columns:
                        batch_df[col] = batch_df[col].astype('category').cat.codes
                    pred_batch = model.predict(batch_df[features])
                    batch_df["预测值"] = pred_batch
                    st.write(batch_df.head())
                    st.download_button("📥 下载预测结果", batch_df.to_csv(index=False).encode("utf-8"), "prediction.csv", "text/csv")
else:
    st.warning("请先上传数据")

