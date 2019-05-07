import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




v = np.random.randint(1,88,62).reshape((2,31))

df = pd.DataFrame(v, index='P N'.split(), columns=np.arange(1,32,1))
#df = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())

#print(df)
#plt.show(sns.distplot(df.loc['P'], kde=False))
#plt.show(sns.jointplot(x=df.loc['P'], y=df.loc['N'], data=df))

v2 = np.random.randint(1,88,62).reshape((31,2))
df2 = pd.DataFrame(v2, index=np.arange(1,32,1), columns='P N'.split())  
print(df2)

plt.show(sns.distplot(df2['P'], kde=False))
plt.show([sns.kdeplot(df2['P']),sns.rugplot(df2['P'])])



#plt.show(sns.jointplot(x=p, y=n))