import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)

fig, ax = plt.subplots(figsize=(8,6))
# alterar linha; linewidth == lw ; linestyle = ls
ax.plot(x,x**2, color="purple", lw=10, alpha=0.5, ls='-.')
ax.plot(x,x**3, 'b', lw=1, ls='--', marker='o', markerfacecolor='red')
# limitar eixo x e y
ax.set_xlim([0,3])
ax.set_ylim([0,10])
plt.show()

y = np.linspace(1,31,31)
p = np.random.randint(1,80,31)
n = np.random.randint(1,88,31)

fig, ax2 = plt.subplots(figsize=(20,20))
ax2.plot(y,p, 'g', lw=2, label='Positivo')
ax2.plot(y,n, 'r--', lw=2, marker='o', markerfacecolor='blue', label='Negativo')
ax2.set_xlim(1,31,1)
ax2.legend()
plt.show()