#%%
"""
Create a function that performs an even-odd transform to a list, n times. 
Each even-odd transformation:
    - Adds 2(+2) to each odd integer.
    - Subtracts 2 (-2) to each even integer.

Example:
    even_odd_transform([3, 4, 9], 3) ➞ [9, -2, 15]
    # Since [3, 4, 9] => [5, 2, 11] => [7, 0, 13] => [9, -2, 15]

    even_odd_transform([0, 0, 0], 10) ➞ [-20, -20, -20]

    even_odd_transform([1, 2, 3], 1) ➞ [3, 0, 5]

"""

def even_odd_transform(lst,repeat):
    i=0
    # for i in range(repeat+1):
    #     for j in lst:
    #         if j % 2 == 0:
    #             j-=2
    #         else:
    #             j+=2
    #         return lst
    # for j in lst:
    #     while i < repeat:
    #         if j % 2 == 0:
    #             j-2
    #             i+=1
    #         else:
    #             j+2
    #             i+=1
    # return lst
    while i < repeat:
        for j,k in enumerate(lst):
            if k % 2 == 0:
                lst[j] -= 2
            else:
                lst[j] += 2
        i += 1
    return lst
            

#%%
even_odd_transform([1, 2, 3], 1)
# %%
even_odd_transform([0, 0, 0], 10)
# %%
even_odd_transform([3, 4, 9], 3)
# %%
