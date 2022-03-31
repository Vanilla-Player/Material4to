import matplotlib.pyplot as plt
import random
import numpy as np 

CANT_REPETICIONES = 100
sum = 0
promedios = []
posibilidades = []
desvios = []
tirada =[]
f_relative =[]
varianzas =[]

for i in range(37):
    posibilidades.append(i)


number = random.choice(posibilidades)

for i in range(CANT_REPETICIONES):
    tirada.append(random.choice(posibilidades))
    promedios.append(np.mean(tirada)) 
    varianzas.append(np.var(tirada))
    desvios.append(np.std(tirada))  
    f_relative.append(tirada.count(number) / len(tirada)) 

plt.figure(num='Frecuencia relativa')


plt.xlabel('N')
plt.ylabel('Frecuencia Relativa')
plt.plot( f_relative )
plt.axhline(1/37,color='red',ls='solid')

plt.figure(num='Varianzas')

plt.xlabel('N')
plt.ylabel('Varianzas')
plt.plot(varianzas)
plt.axhline(114,color='red',ls='solid')

plt.figure(num='Desvios')

plt.xlabel('N')
plt.ylabel('Desvios')
plt.plot(desvios)
plt.axhline(10.6771,color='red',ls='solid')

plt.figure(num='Promedios')

plt.xlabel('N')
plt.ylabel('Promedios')
plt.plot(promedios)
plt.axhline(18,color='red',ls='solid')
plt.show()