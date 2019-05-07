import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

print(tips.head())
print(flights.head())

crr = tips.corr()

print(crr)
# heatmap: mapa de calor; cmap='coolwarm' muda o estilo; annot=True exibe os valores
plt.show(sns.heatmap(crr, cmap='coolwarm', annot=True))

# usando pivo_table : linecolor='white', linewidths=0.8
pv = flights.pivot_table(values='passengers', index='month', columns='year')
print(pv)
plt.show(sns.heatmap(pv, cmap='magma', linecolor='gray', linewidths=0.8))

# clustermap
plt.show(sns.clustermap(pv, standard_scale=1))