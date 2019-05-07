import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']

lista = [10,20,30]
arr = np.array([10,20,30])
dic = {'a':10, 'b':20, 'c':30}

#s1 = pd.Series(data=lista, index=labels)
s1 = pd.Series(lista, labels)
print(s1)

s2 = pd.Series([1,2,3,4], index=(['USA','Alemanha', 'URSS', 'Japão']))
s3 = pd.Series([1,2,3,4], index=(['Alemanha','USA', 'Japão', 'Itália']))
print(s2)
print(s2 + s3)