import pandas as pd

# lendo arq csv
ecom = pd.read_csv('./arq_csv/Ecommerce')

#exibindo 5 primeiros valores
print(ecom.head())

# exibindo informações
print(ecom.info())

# qtd linhas e colunas
print(ecom.shape)

# preço de compra médio
print(ecom['Purchase Price'].mean())

# preço de compra mais alto
print(ecom['Purchase Price'].max())

# preço de compra mais baixo
print(ecom['Purchase Price'].min())

# qts pessoas escolheram inglês como lingua no site
print(sum(ecom['Language'] == 'en'))
    #print(ecom[ecom['Language'] == 'en'].count())

# qtos advogados
print(sum(ecom['Job'] == 'Lawyer'))

# compras no período AM PM
print(ecom.columns)
print(ecom['AM or PM'].value_counts())

# 5 cargos mais comuns
print(ecom['Job'].value_counts().head())

# valor da compra do lot 90 WT
print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])

# email pesso cujo cartão é 4926535242672853
print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])

# qts pessoas tem American Express e compras acima de 95
print(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count())

# qts cc expiram em 2025
print(sum(ecom['CC Exp Date'].apply(lambda x: x[3:] == '25')))

# 5 maiores provedores de email
print(ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head())