import matplotlib.pyplot as plt
import random
import numpy

CANT_REPETICIONES = 1000
CANT_MUESTRA = 1000
posibilidades = []
promedios = []
varianzas = []
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

number = random.choice(posibilidades)

for j in range(CANT_MUESTRA):    
    Tirada = []        
    crearTirada()
    sumarFrecuencia()
    promedios.append( numpy.mean(Tirada))
    varianzas.append(numpy.var(Tirada))
    desvios.append(numpy.std(Tirada))
    frecuenciaRelativa.append(Tirada.count(number) / len(Tirada)) 


plt.figure(num='Frecuencia relativa')


plt.xlabel('Numero Tiradas')
plt.ylabel('Frecuencia Relativa')
plt.bar(height= frecuenciaRelativa, x=range(CANT_MUESTRA) )
plt.axhline(1/37,color='red',ls='solid')

plt.figure(num='Varianzas')

plt.xlabel('Numero Tiradas')
plt.ylabel('Varianzas')
plt.bar(height=varianzas,x=range(CANT_MUESTRA))
plt.axhline(114,color='red',ls='solid')

plt.figure(num='Desvios')

plt.xlabel('Numero Tiradas')
plt.ylabel('Desvios')
plt.bar(height=desvios,x=range(CANT_MUESTRA))
plt.axhline(10.6771,color='red',ls='solid')

plt.figure(num='Promedios')

plt.xlabel('Numero Tiradas')
plt.ylabel('Promedios')
plt.bar(height=promedios,x=range(CANT_MUESTRA))
plt.axhline(18,color='red',ls='solid')
plt.show()