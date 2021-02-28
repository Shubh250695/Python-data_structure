# Q5  Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary

# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output: ac ad bc bd

from itertools import product

data ={'1':['a','b'], '2':['c','d']}
print (data)

for x in data['1']:
    for y in data['2']:
        print(x + y)