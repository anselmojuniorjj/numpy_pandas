import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# alterando estilo do gráfico. ggplot, bmh, dark_background
plt.style.use('dark_background')

# visualização de dados embutidos ao pandas

df1 = pd.read_csv('./arq_csv/df1', index_col=0)
df2 = pd.read_csv('./arq_csv/df2')

print(df1.head())
plt.show(df1['A'].hist())

print(df2.head())
plt.show(df2.plot.area(alpha=0.4))
plt.show(df2.plot.bar())
plt.show(df2.plot.bar(stacked=True))

plt.show(df1.plot.line(x=df1.index, y='B', figsize=(12,5), lw=1))

# muda a cor em função da coluna 'D' c='D', poderia ser fixo c='red'
plt.show(df1.plot.scatter(x='A', y='B', c='D', cmap='coolwarm'))
# muda o tamanho em função da coluna 'D', poderia ser fixo s=30
plt.show(df1.plot.scatter(x='A', y='B', s=df1['D']*15))

plt.show(df2.plot.box())

# mapa de calor hexagonal
df3 = pd.DataFrame(np.random.rand(1000,2), columns=['A','B'])
plt.show(df3.plot.hexbin(x='A', y='B', gridsize=20, cmap='summer'))

# kde
plt.show(df2.plot.kde())