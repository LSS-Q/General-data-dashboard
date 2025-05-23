# 📊 General Data Dashboard

A universal data analytics and modeling platform built with **Streamlit**. This dashboard enables users to upload datasets, perform preprocessing, explore data visually, build predictive models, and export results — all through an interactive interface.

## 🔧 Features

- 📁 Upload CSV files and automatically detect data types
- 🧹 Handle missing values and convert object/date fields
- 📊 Generate descriptive statistics for numerical and categorical variables
- 📈 Visualize correlations (heatmaps) and interactive scatter plots with regression lines
- 🤖 Build machine learning models (Linear/Logistic Regression, Random Forest, KNN)
- 🧠 Display feature importance or model coefficients
- 📤 Support batch prediction uploads and downloadable results
- 📝 Generate summary reports (HTML export included, PDF optional)

## 🚀 Live Demo

👉 [Launch App on Streamlit Cloud](https://general-data-dashboard-kgnhh7cmvmgnhbtvw7pkiq.streamlit.app/)

## ⚙️ Installation

bash
git clone https://github.com/LSS-Q/General-data-dashboard.git
cd General-data-dashboard
pip install -r requirements.txt
streamlit run app.py

📦 streamlit_dashboard/
├── app.py                     # Main entry file
├── requirements.txt
├── pages/                     # Modular page components
│   ├── 1_Upload_and_Preview.py
│   ├── 2_Preprocessing.py
│   ├── 3_Statistics.py
│   ├── 4_Visualization.py
│   ├── 5_Modeling_and_Prediction.py
│   └── 6_Report_Generation.py
├── utils/                     # Data preprocessing helpers
│   ├── data_loader.py
│   └── preprocess.py
└── assets/
    └── style.css              # Custom styling

📄 License
This project is licensed under the MIT License.
