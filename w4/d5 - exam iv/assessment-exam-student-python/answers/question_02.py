#%%
import pandas as pd
import sys
#%%
from supporting_files.data_loader import load_excel

#%%
df = load_excel('supporting_files/SaleData.xlsx')
#%%
xl = "C:/Users/Tim/Desktop/lighthouse/w4/d5/assessment-exam-student-python/supporting_files/SaleData.xlsx"
df1 = pd.read_excel(xl)

#%%
"""
Write a Pandas program to find the total sale amount (Sale_amt) region and manager wise. 
Order the dataframe by Sale_amt, starting with the highest.
Output should be DataFrame with 3 columns (order is important):
    - Region
    - Manager
    - Sale_amt
and numeric index starting with 0 (after sorting).
"""

def compute_total_sale(df):
    col = [
        "Region",
        "Manager",
        "Sale_amt"
    ]
    df2 = df[col]
    df2 = pd.DataFrame(df2.groupby(['Region','Manager'])['Sale_amt'].sum())
    # df_agg = df2['Sale_amt'].groupby('Region',group_keys=False)
    # df_agg = pd.DataFrame(df_agg.apply(lambda x: x.sort_values(ascending=False)))
    # df_agg = df_agg.reset_index()

    # return df_agg
    df3 = df2.sort_values('Sale_amt',ascending=False)
    df3 = df3.reset_index()
    return df3
# %%
compute_total_sale(df1)
# %%
