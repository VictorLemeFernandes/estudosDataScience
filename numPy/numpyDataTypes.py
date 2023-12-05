import numpy as np

vetor = np.array([[1,2,3],
                 [4,"Hello", 6],
                 [7,8,9]])

print(type(vetor[1,1]))

# Não podemos misturar tipos de dados diferentes... Nesse exemplo temos uma string com números inteiros. Mas posso mudar...

vetor = np.array([[1,2,3],
                 [4,"8", 6],
                 [7,8,9]], dtype=np.int32)

print(type(vetor[1,1]))
print(vetor.dtype)

# Podemos colocar um dicionario
dicionario = {'1': 'a'}

vetor = np.array([[1,2,3],
                 [4,dicionario, 6],
                 [7,8,9]])

print(vetor.dtype)
print(type(vetor[0,2]))
