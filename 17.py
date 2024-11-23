#Crie uma matriz quadrada 3x3 aleatória. Calcaule o determinante e, se possível, calcule a inversa.

import numpy as np

matriz = np.random.rand(3, 3)

determinante = np.linalg.det(matriz)

if determinante != 0:
    inversa = np.linalg.inv(matriz)
    print(inversa)