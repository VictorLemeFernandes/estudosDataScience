import numpy as np

vetor = np.full((2,3,4), 9)
print(vetor)
print(20*'-')

vetor = np.zeros((2,3,4))
print(vetor)
print(20*'-')

vetor = np.arange(0, 105, 5)
print(vetor)
print(20*'-')

vetor = np.linspace(0, 100, 5)
print(vetor)
print(20*'-')

#NaN and inf
print(np.nan, np.inf)