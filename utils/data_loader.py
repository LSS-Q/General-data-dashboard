import pandas as pd

def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file, low_memory=False)
    for col in df.columns:
        if any(x in col.lower() for x in ['date', '时间', 'recorded', 'day', 'dt']):
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            except Exception:
                continue
    return df
