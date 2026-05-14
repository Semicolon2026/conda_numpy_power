import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df
