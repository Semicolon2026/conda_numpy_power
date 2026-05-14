import pandas as pd
from app.processor import handle_missing

def test_handle_missing():
    df = pd.DataFrame({"a": [1, None, 3]})
    result = handle_missing(df, 0)

    assert result.isnull().sum().sum() == 0
