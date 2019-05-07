import numpy as np

a1 = np.arange(0, 30, 3)

# exibri array
print(a1[3])
print(a1[2:5])
print(a1[2:])
print(a1[:15])

# altera tds elementos apartir de determinado indice
a1[5:] = 0
print(a1)

# array bidimencional (matriz bidimencional)

a2 = np.arange(50).reshape((5, 10))
print(a2)

# 3xibir a1[:linhas, :colunas]
print(a2[:3, :5])


# a3 = a2[:3] cria uma referência(ponteiro)
# para copiar utilizar .copy
a3 = a2[:3, :5].copy()
print(a3)
a3[:] = 33
print(a3)
print(a2)

# utiliar bolean p/ filtrar array

bol = a2 > 25
print(a2[bol])
par = a2 % 2 == 0
print(a2[par])

# pegar primeira coluna
print(a2[:, 0])

# pegar quarta coluna
print(a2[:, 3])

# somar colunas: axis=0
print(a2)
soma_colunas = a2.sum(axis=0)
print(soma_colunas)

# somar linhas: axis=1
print(a2)
soma_linhas = a2.sum(axis=1)
print(soma_linhas)