import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

print(iris.head(20))
print(iris['species'].value_counts())

# Pair Grid

g = sns.PairGrid(iris)

# gráfico de dispersão com tds variáveis possíveis
plt.show(g.map(plt.scatter))

# diagonal com histograma, superior e inferior diferentes
plt.show(sns.pairplot(iris, hue='species'))

# dados categóricos
tips = sns.load_dataset('tips')
g2 = sns.FacetGrid(tips, col='time', row='smoker')
plt.show(g2.map(plt.hist, 'total_bill'))
