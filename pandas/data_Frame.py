import numpy as np
import pandas as pd

rand = np.random.seed(101)

# criar tabela (valores, linhas, colunas)
df = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)

# mostrar colunas
print(df['W'])
print(df[['W', 'Z']])

# somar colunas
df['new'] = df['W'] + df['Y']
print(df)

# excluir colunas
df.drop('new', axis=1, inplace=True)
print(df)

# mostrar linha
print(df.loc['A'])

# selecionar único valor linha x coluna
print(df.loc['C', 'Y'])

# selecionar linhas x colunas
print(df.loc[['A',  'B'], ['X', 'Y', 'Z']]) 

# iloc seleciona por índice
print(df.iloc[0:2, 1:])

# exibir linha y onde w > 0
print(df[df['W']>0]['Y'])

# exibir linha onde w > 0 e y > 1
print(df[(df['W'] > 0) & (df['Y'] > 1)])

# exibir linha onde x > 0 ou y > 1
print(df[(df['X'] > 0) | (df['Y'] > 1)])

# resetar index (índice das linhas), índice vira coluna
#   df.reset_index(inplace=True)

# incluir uma coluna, utilizar uma coluna coma index (não é definitivo)
    # para tornar dfinitivo utilizar inplace=True
col = 'SP RJ RS SC AM'.split()
df['Estado'] = col
print(df)
print(df.set_index('Estado'))
print(df)

# --------------------- Índices multiníveis------------------------------------

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside))
print(hier_index)
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

df2 = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=['A', 'B'])
print(df2)

# exibir linha 1 do G1
print(df2.loc['G1'].loc[1])

# dar um nome para colunas de índice
df2.index.names = ['Grupo', 'Numero']
print(df2)

# selecionar determinda linha de todos os 'grupos'
print(df2.xs(1, level='Numero'))