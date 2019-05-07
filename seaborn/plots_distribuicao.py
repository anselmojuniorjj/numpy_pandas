import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips.head())

# displot: histograma, curva KDE, bins=50

plt.show(sns.distplot(tips['total_bill'], kde=False))

# jointplot duas variáveis, gráfico de distribuição conjunta. kind='reg','hex'
plt.show(sns.jointplot(x='total_bill', y='tip', data=tips))

# pairplot pega tds váriaveis e faz joinplot de cada uma delas
    # hue='sex'
plt.show(sns.pairplot(tips, hue='sex'))

# rugplot
plt.show(sns.rugplot(tips['total_bill']))

# kdeplot
plt.show([sns.kdeplot(tips['total_bill']),sns.rugplot(tips['total_bill'])])