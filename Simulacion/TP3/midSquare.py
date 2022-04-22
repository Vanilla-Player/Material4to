import matplotlib.pyplot as plt
import numpy as np

from frecuency_monobit_test import frecuency_monobit_test as fmt





def mid_square (seed):

    squareSeed = str(seed*seed)
    result = int(squareSeed.zfill(8)[2:6])  
       
    return result





contador = 0
#numero = int(input("Introduzca 4 Numeros: ")) # Input de 4 o menos digitos 6854, 9999, 2312
numero = 9999
numeros = []
while contador < 110:

    numero = mid_square(numero)
    resultado_test = fmt(numero)
    print(resultado_test)
    numeros.append(resultado_test)
    #numeros.append(numero)
    contador +=1


plt.figure(num='Mitad del cuadrado')

plt.xlabel('Cantidad de Numeros')
plt.ylabel('Valores')


plt.scatter(x=range(contador), y=numeros)


plt.show()