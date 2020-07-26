numero = 2

vetor = [2,3,5]

import numpy as np

result = vetor = np.asarray(vetor)

result = vetor.max()
result = vetor.argmax()
result = vetor.min()
result = vetor.mean()
result = vetor.sum()

result = vetor2 = numero * vetor 
result = np.arange(1, 50, 0.5)
result = np.zeros(10)
result = np.ones(10)
result = np.ones((3,3))

result = np.linspace(1,20,10)

result = np.random.seed(1)
result = np.random.randint(0, 101, 4)

result = np.random.randint(0, 101, (3,3))
print(result)
