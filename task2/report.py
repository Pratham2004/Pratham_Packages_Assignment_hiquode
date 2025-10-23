import pandas as pd

def print_report(df: pd.DataFrame, sales_col: str = 'sales'):
   
    total = df[sales_col].sum()
    average = df[sales_col].mean()
    print(f"Total sales : {total:,.2f}")
    print(f"Average sales: {average:,.2f}")