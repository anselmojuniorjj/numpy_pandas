import numpy as np

# operaçoes arrays com numpy
a1 = np.arange(0, 15, 2)
print(a1 + a1)
print(a1 + 100)
print(a1 * 3)

# raiz quadrada com numpy
r2 = np.sqrt(a1)
print(r2)

# expoente
e1 = np.exp(a1)
print(e1)

# média
m1 = np.mean(a1)
print(m1)

# desvio padrão
d1 = np.std(a1)
print(d1)

# seno
s1 = np.sin(a1)
print(s1)

# max min : np.max(a1) ou a1.max() ; np.min(a1) ou a1.min()
print(a1.max())
print(a1.min())