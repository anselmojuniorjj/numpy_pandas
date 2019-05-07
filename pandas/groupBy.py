import pandas as pd

data = {
    'Empresa': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'Nome': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sara'],
    'Venda': [200, 120, 340, 124, 243, 350]
}

df = pd.DataFrame(data)
print(df)


# agrupar por Empresa
group = df.groupby('Empresa')

#exibir a soma das vendas nas empresas
print(group.sum())

#exibir a média das vendas nas empresas
print(group.mean())

# método describe() exibe várias informações
print(group.describe())

# exibir soma das vendas de um determinado vendedor
vendedor = df.groupby('Nome')
print(vendedor.sum().loc['Sara'])