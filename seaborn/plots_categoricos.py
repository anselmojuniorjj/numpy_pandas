import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset('tips')
print(tips.head())

# dados categoricos, contém textos e poucos valores

# barplot; valor médio; |desvio padrão
plt.show(sns.barplot(x='sex', y='total_bill', data=tips))
# barplot; desvio padrão
plt.show(sns.barplot(x='sex', y='total_bill', data=tips, estimator=np.std))

# countplot
plt.show(sns.countplot(x='sex', data=tips))

# boxplot: quartil; pallete='muda cor'; hue='sex'->mostra duas categorias: masc e fem
plt.show(sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker'))

# mostrar na horizontal: orient='h'
plt.show(sns.barplot(data=tips, orient='h'))

# violinplot: modelo não paramétrico, estima o kde, mostra distribuição
    #  hue='sex', split=True->mostra duas categorias: masc e fem
plt.show(sns.violinplot(x='day', y='tip', data=tips, hue='sex', split=True))

# stripplot. jitter=True, hue='sex, split=True: dados ficam amontoados
plt.show(sns.stripplot(x='day', y='total_bill', data=tips, jitter=True))

# swarmplot: distribui melhor os pontos , mas pode sobrepor a coluna ao lado
plt.show(sns.swarmplot(x='day', y='total_bill', data=tips))

# swarmplot com violinplot
plt.show([sns.swarmplot(x='day', y='total_bill', data=tips, color='black'), sns.violinplot(x='day', y='total_bill', data=tips)]) 

# factorplot: kind='tipo do plot'
plt.show(sns.factorplot(x='sex', y='total_bill', data=tips, kind='bar'))