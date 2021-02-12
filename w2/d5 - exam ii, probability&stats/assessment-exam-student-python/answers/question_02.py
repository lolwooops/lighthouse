#%%
"""
Write a function that takes a string and calculates the number of letters and digits within it. Return the result in a dictionary.

Examples:
    count_all("Hello World") ➞ { "LETTERS":  10, "DIGITS": 0 }

    count_all("H3ll0 Wor1d") ➞ { "LETTERS":  7, "DIGITS": 3 }

    count_all("149990") ➞ { "LETTERS": 0, "DIGITS": 6 }

Notes:
    - Tests contain only alphanumeric characters.
    - Spaces are not letters.
    - All tests contain valid strings.
    - The function should return dictionary

"""
from collections import Counter
def count_all(string):
        y = list(str(string))
        #y = [int(i) if i.isdigit() else i for i in y]
        x = {}
        nletters = 0
        ndigits = 0
        for i in y:
            if i.isalpha() == True:
                nletters += 1
            if i.isdigit() == True:
                ndigits += 1
        x['LETTERS'] = nletters
        x['DIGITS'] = ndigits
        return x

# %%
count_all("H3ll0 Wor1d")
# %%
count_all("")
# %%
