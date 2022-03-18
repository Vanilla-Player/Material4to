
import re
import matplotlib.pyplot as plt
import random

import numpy
CANT_REPETICIONES = 30
posibilidades = []

promedios = []

variancas = []
desvios = []
suma_promedios = 0
frecuenciaAbs = []

frecuenciaRelativa = []




for i in range(37):
    posibilidades.append(i)
    frecuenciaAbs.append(0)


def sumarFrecuencia():

    for index in Tirada:
        
        frecuenciaAbs[index] += 1




def crearTirada():

    for i in range(CANT_REPETICIONES):
        Tirada.append(random.choice(posibilidades))




for j in range(CANT_REPETICIONES):
    
    Tirada = []
        
    crearTirada()

    sumarFrecuencia()


    suma_promedios += random.choice(posibilidades) # => El promedio es por tirada?

    promedios.append(suma_promedios/(j+1))
    variancas.append(numpy.var(Tirada))
    desvios.append(numpy.std(Tirada))


for cantidad in frecuenciaAbs:
    frecuenciaRelativa.append(cantidad/CANT_REPETICIONES)

    
   




#plt.plot(frecuenciaRelativa)

fig, ax = plt.subplots(1, 4, figsize=(9, 3), sharey=True)



ax[0].stem(posibilidades, frecuenciaRelativa)

#ax.set(xlim=(0, 36), xticks=numpy.arange(0, 37),
       #ylim=(25, 29), yticks=numpy.arange(26, 29))

ax[1].plot(variancas)
ax[2].plot(desvios)
ax[3].plot(promedios)



plt.show()