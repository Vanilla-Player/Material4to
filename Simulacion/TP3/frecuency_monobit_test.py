
# Input del metodo => Numero binario 
# Salida del metodo => P-value, sirve para validar si el valor es random o no P-value >= 0.01 para ser random
from cmath import sqrt
import math
import numpy as np



def convertidorBinario(decimal):
    binario = 0
    i = 0
    while (decimal>0):
        digito  = decimal%2
        decimal = int(decimal//2)
        binario = binario+digito*(10**i)
        i = i+1
    return binario



# math.erfc(x) => Funcion de error complementaria
# math.erf(x)

def frecuency_monobit_test(numero):

    binarioString = str(convertidorBinario(numero))
    n = len(binarioString)
    observaciones = 0 # +1 cuando el bit es 1 y -1 cuando es 0

    for char in range(n):
        if(binarioString[char] == "1"):
            observaciones +=1
        else:
            observaciones -=1

    abs_observaciones =abs(observaciones)

    
    if(abs_observaciones == 0):
        return 0


    z = (abs_observaciones)/sqrt(n)
    

    valor_real =  np.real((z)/(sqrt(abs_observaciones)))
    

    Pvalue = math.erfc(valor_real)

    return Pvalue

