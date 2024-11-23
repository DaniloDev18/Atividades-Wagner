#Crie um array com os valores x=[0,pi/2,pi,3pi/2,2pi] e calcule o seno e o cosseno desses valores.

import numpy as np

x = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])

seno = np.sin(x)
cosseno = np.cos(x)

print("Seno:", seno)
print("Cosseno:", cosseno)