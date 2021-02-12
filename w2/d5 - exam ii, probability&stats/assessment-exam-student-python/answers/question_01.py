#%%
"""
Create a function that returns the mean of all digits.

Example:
    mean(42) ➞ 3.0

    mean(12345) ➞ 3.0

    mean(666) ➞ 6.0

Notes:
    - Function should always return float
"""


def mean(digits):
    y = list(str(digits))
    y = list(map(int,y))
    return sum(y)/len(y)

#%%
mean(42)
# %%
mean(12345)
# %%
mean(666)
# %%
