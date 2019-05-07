import numpy as np
import pandas as pd

d = {'A': [1,2,np.nan], 'B': [5,np.nan,np.nan], 'C': [1,2,3]}

df = pd.DataFrame(d)
print(df)

# excluir valores fantantes, por padrão exclui linha (axis=0), td a linha
print(df.dropna())

# excluir coluna axis=1, td a coluna
print(df.dropna(axis=1))

# para excluir qdo houver 2 falores ausentes
print(df.dropna(thresh=2))

# substituir valor ausente; método fillna()
print(df.fillna(value='ausente'))

# substituir pela média
print(df.fillna(value=df.mean()))

# preencher com valor anterior
print(df.fillna(method='ffill'))