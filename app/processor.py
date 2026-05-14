import numpy as np

def handle_missing(df, fill_value=0):
    return df.fillna(fill_value)

def add_features(df):
    numeric_cols = df.select_dtypes(include=[np.number])

    if numeric_cols.empty:
        df["dummy_feature"] = 1
        return df

    df["row_sum"] = numeric_cols.sum(axis=1)
    df["noise"] = np.random.randn(len(df))

    return df
