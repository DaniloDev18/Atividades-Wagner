#Crie um array contendo os números inteiros de 1 a 20. Substitua todos os números que são divisiveis por 3 por -3

import numpy as np


array = np.arange(1, 21)

array[array % 3 == 0] = -3

print(array)