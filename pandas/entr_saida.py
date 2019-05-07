import numpy as np
import pandas as pd

# ler arq csv
df = pd.read_csv('./arq_csv/exemplo1', sep=',')
print(df)

# somar a tds os campos
df = df + 1
print(df)


df2 = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df2)

# salvar arq csv
df.to_csv('./arq_csv/mais_um.csv', sep=';', decimal=',')
df2.to_csv('./arq_csv/exemp_salvar.csv', sep=';', decimal=',')

# salvar arq excel (sheetname='nome da aba')
    #df3 = pd.read_excel('./arq_excel/exemplo3.xlsx', sheetname='sheet1')

# salvar arq excel
    #df.to_excel('./arq_excel/exemplo3.xlsx', sheet_name='sheet1')

df4 = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
#print(df4[0])
print(df4[0]['Bank Name'])