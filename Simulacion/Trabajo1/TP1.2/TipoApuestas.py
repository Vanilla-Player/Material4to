

from audioop import mul
from email.mime import multipart
import faulthandler
from itertools import count




def pares(numeros):
    multiplicador = 2    
    for par in range(1,36):
        if par % 2 != 0:
            numeros.append(par)
    return multiplicador


def impares(numeros):

    for impar in range(1,37):
        if impar % 2 == 0:
            numeros.append(impar)


def columnas(numeros, columna):

    while len(numeros) < 12:
        numeros.append(columna)
        columna +=3


def pasa(numeros):
    numero=1
    while len(numeros) < 18:
        numeros.append(numero)
        numero+=1

def falta(numeros):
    numero=19
    while len(numeros) < 18:
        numeros.append(numero)
        numero+=1

def docenas(numeros, docena):
    numero = 0
    if(docena == 1):
        numero = 1
    elif(docena == 2):
        numero = 13
    elif(docena == 3):
        numero = 26
    
    while len(numeros) < 12:
        numeros.append(numero)
        numero += 1


#Falta
#color
#Fila
#Cuadro 
#Caballo
#Plena



        
