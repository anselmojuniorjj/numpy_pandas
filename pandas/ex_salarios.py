import pandas as pd

# lendo arq csv
sal = pd.read_csv('./arq_csv/Salaries.csv')

#exibindo 5 primeiros valores
print(sal.head())

# exibindo informações
print(sal.info())

# exibindo salário médio
print(sal['BasePay'].mean())

# exibindo maior valor de OvertimePay
print(sal['OvertimePay'].max())

# exibir cargo de JOSEPH DRISCOLL
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL'])
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])

# exibir salário (total) de JOSEPH DRISCOLL
print(sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPay'])

# exibir nome do maior salário
print(sal[sal['TotalPay'] == sal['TotalPay'].max()])

# exibir nome do menor salário
print(sal[sal['TotalPay'] == sal['TotalPay'].min()])

# exibir média salário por ano
    # dica: agrupar e depois exibir
print(sal.groupby('Year').mean())
print(sal.groupby('Year').mean()['BasePay'])

# exibe os job titles únicos
print(sal['JobTitle'].unique())
print(len(sal['JobTitle'].unique()))
# print(sal['JobTitle'].nunique())

# exibe os 5 cargos mais aparecem
# print(sal['JobTitle'].value_counts().head())
print(sal['JobTitle'].value_counts().iloc[:5])

# cargo único 2013
print(sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1))

# qts pessoas tem a palavra chefe no cargo
def chefe(title):
    if 'chief' in title.lower():
        return True
    else:
        return False

print(sum(sal['JobTitle'].apply(lambda x: chefe(x))))

# correlação salário e e comprimento do título?
sal['TamanhoString'] = sal['JobTitle'].apply(len)
print(sal[['TamanhoString', 'TotalPay']].corr())