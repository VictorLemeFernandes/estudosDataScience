import numpy as np

a = np.array([1,2,3,4,5])

print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[:-2])

a[2] = 10
print(a)

print(20*'*')

matriz = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(f"Matriz:\n{matriz}")
print(f"Linha 0, coluna 2: {matriz[0, 2]}")

print(f"Dimensão da matriz: {matriz.shape}") # 3x3
print(f"Quantidade de elementos: {matriz.size}")
