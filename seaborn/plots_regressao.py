import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

# lmplot - gráfico de dispersão; hue='sex'; alterar marcador markers=['o','v']
# alterar tamanhos, médias... scatter_kws=['s':100]
plt.show(sns.lmplot(x='total_bill', y='tip', data=tips, hue='smoker', markers=['o','v']))
    # separar em duas colunas hue='sex', col='sex'
plt.show(sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', col='sex'))
    # separar em duas colunas e linhas hue='sex', col='sex', row='time
plt.show(sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', col='sex', row='time'))

# alterando tamanhos
plt.show(sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', col='day', aspect=0.7, size=8))