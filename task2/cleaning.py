import pandas as pd

def remove_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
  
    return df.dropna(how='all')