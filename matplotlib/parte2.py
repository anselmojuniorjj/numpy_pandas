import matplotlib.pyplot as plt
import numpy as np


# -----------------orientado a objeto-------------

# criando duas listas...
x = np.linspace(0,5,11)
y = x*x


# subplots 
fig, ax = plt.subplots()
ax.plot(x, x**3, 'b--', label='x³')
ax.plot(x, x**4, 'g-.', label='x⁴')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Título')
ax.legend()
fig.savefig('./graficos/grafico1.png')
plt.show()

# dois ou mais gráficos subplot(linha,coluna)
fig2, ax2 = plt.subplots(1, 2)
ax2[0].plot(x,y, 'r--')
ax2[0].set_title('Título Bacana I')
ax2[1].plot(y,x, 'b*-')
ax2[1].set_title('Título Bacana II')
fig2.savefig('./graficos/grafico2.png')
plt.show()

# redimencionar a 'caixa' do gráfico; exibir legenda (loc=1),(loc=2)...(loc=4): localização

fig3, ax3 = plt.subplots(figsize=(8,3))
ax3.plot(x,y, 'g', label='x²')
ax3.plot(x,y**2, 'r--', label='x⁴')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_title('Título Legal')
ax3.legend()
# salvar gráfico
fig3.savefig('./graficos/grafico3.png')
plt.show()

# plt.tight_layout() ; melhora a visualização qdo houver muitos grpaficos
