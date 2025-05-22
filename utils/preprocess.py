import pandas as pd

def clean_object_datetime(df):
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]) or pd.api.types.is_object_dtype(df[col]):
            df[col] = df[col].fillna('').astype(str)
    return df

def handle_missing_values(df, method="均值填充"):
    if method == "删除含缺失值的行":
        return df.dropna()
    elif method == "用均值填充":
        return df.fillna(df.mean(numeric_only=True))
    elif method == "用中位数填充":
        return df.fillna(df.median(numeric_only=True))
    elif method == "用众数填充":
        for col in df.columns:
            df[col] = df[col].fillna(df[col].mode()[0])
    return df
