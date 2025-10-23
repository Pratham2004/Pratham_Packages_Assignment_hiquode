import pandas as pd
from task2.cleaning import remove_empty_rows
from task2.report import print_report


df = pd.DataFrame({
    "region": ["North", "South", None, "East"],
    "sales" : [1000, 2500, None, 3000]
})

df_clean = remove_empty_rows(df)
print("Cleaned DataFrame:")
print(df_clean, "\n")
print_report(df_clean)