import pandas as pd
from app.utils import clean_columns

def test_clean_columns():
    df = pd.DataFrame(columns=[" A Column ", "B Value"])
    cleaned = clean_columns(df)

    assert "a_column" in cleaned.columns
    assert "b_value" in cleaned.columns
