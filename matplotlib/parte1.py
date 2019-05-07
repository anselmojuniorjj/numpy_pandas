import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x*x

# Funcional, o mais simples
plt.plot(x,y, color='r')
plt.title('first matplot')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
#plt.show()

# dois ou mais gráficos subplot(linha,coluna,qual gráfico vai receber info)
plt.subplot(1,2,1)
plt.plot(x,y,'r--')
plt.subplot(1,2,2)
plt.plot(y,x,'g*-')
#plt.show()

# orientada a objetos
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes1.plot(x,y)
axes1.set_xlabel('Eixo x')
axes1.set_title('Título')
axes2 = fig.add_axes([0.2,0.5,0.3,0.3])
axes2.plot(y,x, 'r--')
axes2.set_xlabel('Eixo x')
axes2.set_title('Gráfico menor')
plt.show()