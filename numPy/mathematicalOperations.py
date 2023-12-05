import numpy as np

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]

a1 = np.array(l1)
a2 = np.array(l2)

print(l1 * 5)
print(a1 * 5)

print(a1, a2)
print(a1 + a2)

# Com numpy arrays podemos fazer operações com vetores, diferentemente de listas.
print(30*'-*')

a1 = np.array([1,2,3])
a2 = np.array([[1],
               [2]])

print(a1 + a2)
print(30*'-*')

# Funções
vetor = np.array([[1,2,3],
                  [4,5,6]])
print(np.sqrt(vetor))