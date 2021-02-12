#%%
import pandas as pd
import sys
#%%
from supporting_files.data_loader import load_excel

df = load_excel('supporting_files/SaleData.xlsx')

#%%
xl = "C:/Users/Tim/Desktop/lighthouse/w4/d5/assessment-exam-student-python/supporting_files/SaleData.xlsx"
df1 = pd.read_excel(xl)


"""
Write a function to count the manager wise sale (sale_cnt)
and mean value of sale amount (sale_mean). 
Order the output dataframe by sale_cnt, starting with the highest.
Output should be DataFrame with 3 columns (order is important):
    - Manager
    - sale_cnt
    - sale_mean
and numeric index starting with 0 (after sorting).
"""
#%%
def compute_agg_stats(df):
    df1 = pd.DataFrame(df.groupby(['Manager'])['Sale_amt'].count())
    df1['sale_mean'] = df.groupby(['Manager'])['Sale_amt'].mean()
    df1 = df1.rename(columns={'Sale_amt':'sale_cnt'})
    df1 = df1.sort_values('sale_cnt',ascending=False)
    df1 = df1.reset_index()
    return df1