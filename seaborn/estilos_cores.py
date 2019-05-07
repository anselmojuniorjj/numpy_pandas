import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# 'darkgrid', 'ticks', 'whitegrid', 'dark', sns.despine(), plt.figure(figsize=(12,8))
sns.set_style('ticks')

plt.show(sns.countplot(x='sex', data=tips))

#------------------

plt.show(sns.lmplot(x='total_bill', y='tip', data=tips, size=5, aspect=2))

#- set_context('poster') noteboock, paper, talk
sns.set_context('notebook', font_scale=1)
plt.show(sns.lmplot(x='total_bill', y='tip', data=tips))

# setando cores; palette='coolwarm'
sns.set_context('notebook', font_scale=1)
plt.show(sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette='GnBu'))