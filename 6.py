#Crie um array de números inteiros aleatórios entre 1 e 100 (tamanho 20).
#Substitua todos os valores maiores que 50 por 0.

import numpy as np

array = np.random.randint(1, 100, 20)

array[array > 50] = 0

print(array)

