import numpy as np


# criar array
minha_lista = [1,2,3]

print(np.array(minha_lista))

minha_matriz = [[1,2,3], [4,5,6], [7,8,9]]
print(np.array(minha_matriz))

# arange
lista1 = np.arange(1, 10)
print(lista1)

lista2 = np.arange(0, 10, 2)
print(lista2)

# matriz de zeros e uns 
array0 = np.zeros((5,5))
print(array0)

array1 = np.ones((5,5))
print(array1)

# matriz identidade
matriz_identidade = np.eye(4)
print(matriz_identidade)

# linspace
m1 = np.linspace(0, 10, 3)
print(m1)

# random rand - cria números aleatórios entre 0 e 1. entre 1 e 100 multiplique por 100
    # distribuição uniforme
m2 = np.random.rand(5)
print(m2)

# matriz 4x4
m3 = np.random.rand(4, 4)
print(m3)

# random randn - distribuição Gaussiana
m4 = np.random.randn(5)
print(m4)

# random randint - distribuição de inteiros
m5 = np.random.randint(1, 61, 6)
print(m5)

# reshape

l1 = np.random.rand(25)
print(l1)
m6 = l1.reshape((5,5))
print(m6)

# maior e menor valor
print(m6.max())
print(m6.min())

# indice maior e menor elemento
print(m6.argmax())
print(m6.argmin())