# -*- coding: utf-8 -*-
"""Assignment_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aWqhkVA1HUMnJ87bpk2QQB97yvcdjNul

# Basic Python

## 1. Split this string
"""

s = "Hi there Sam!"

s=s.split(" ")
s

"""## 2. Use .format() to print the following string. 

### Output should be: The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742

print("The diametr of Earth is {}kilometer.".format(diameter))

"""## 3. In this nest dictionary grab the word "hello"
"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

a=d.keys()
a

"""# Numpy"""

import numpy as np

"""## 4.1 Create an array of 10 zeros? 
## 4.2 Create an array of 10 fives?
"""

np.zeros(10)

np.ones(10)*5

"""## 5. Create an array of all the even integers from 20 to 35"""

array=np.arange(20,35,2)
print(array)

"""## 6. Create a 3x3 matrix with values ranging from 0 to 8"""

a=np.ones((0,9,3))
a

"""## 7. Concatenate a and b 
## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
"""

b=np.array([4,5,6,])
list=a+b
list

"""# Pandas

## 8. Create a dataframe with 3 rows and 2 columns
"""

import pandas as pd

d={"Name":["viji","jk"],
   "Age":[20,24],
   "Genter":["F","M"]}
df=pd.DataFrame(d)
d

"""## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023"""



"""## 10. Create 2D list to DataFrame

lists = [[1, 'aaa', 22],
         [2, 'bbb', 25],
         [3, 'ccc', 24]]
"""

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]

p=pd.date_range(start='1-1-2023',end='10-2023')
for val in p:
  print(val)