import pandas as pd

df = pd.DataFrame({
    'col1': [1,2,3,4],
    'col2': [444,555,666,444],
    'col3': ['abc','def','ghi','xyz']
})

print(df)

# não repetir valores de uma mesma coluna
print(df['col2'].unique())

# qtd de valores únicos
print(len(df['col2'].unique()))

# exibe valores e qtd que cada um aparece
print(df['col2'].value_counts())

# filtrar
print(df[(df['col1'] > 2) & (df['col2'] == 444)])

# utilizar uma função criada para tds os elementos do df
def vezes2(x):
    return x*2

print(df['col1'].apply(vezes2))

print(df['col1'].apply(lambda x: x*x))

# utilizar uma função para tds os elementos do df
print(df['col3'].apply(len))

# deletar coluna
    # del df['col2']

# consultar colunas
print(df.columns)

# consultar índice
print(df.index)

# ordernar valores de uma coluna: para ser definitivo utilizar inplace=True
print(df.sort_values(by='col2'))

# verifica se tem algum valor null
print(df.isnull())

#------------------------pivot table

data = {
    'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
    'B': ['one', 'one', 'one', 'two', 'two', 'two'],
    'C': ['x', 'y', 'x', 'y', 'x', 'y'],
    'D': [1,3,2,5,4,1]
}

df2 = pd.DataFrame(data)

print(df2)

print(df2.pivot_table(values='D', index=['A', 'B'], columns=['C']))