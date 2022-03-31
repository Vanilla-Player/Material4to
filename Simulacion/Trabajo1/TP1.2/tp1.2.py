import matplotlib.pyplot as plt
import random
import numpy as np 

CANT_REPETICIONES = 10000
CANT_CORRIDAS = 10
APUESTA_INICIAL = 1
CAPITAL_INICIAL = 50

frecuencias = []
gananciasMartingala = []
gananciasFibonacci = []
gananciasDAlembert = []

def Fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


posibilidades = []
for i in range(37):
    posibilidades.append(i)


for i in range(CANT_CORRIDAS):

    corrida = []
    cantApuestasFavorables = 0
    frecuentaRelativaAF = []

    capitalDAlembert = [CAPITAL_INICIAL]
    gananciaDAlembert = [0]
    apuestaDAlembert = [APUESTA_INICIAL]

    capitalMartingala = [CAPITAL_INICIAL]
    gananciaMartingala = [0]
    apuestaMartingala = [APUESTA_INICIAL]

    capitalFibonacci = [CAPITAL_INICIAL]
    gananciaFibonacci = [0]
    apuestaFibonacci = [APUESTA_INICIAL]
    posicionFibonacci = 2

    for i in range(CANT_REPETICIONES):
        corrida.append(random.choice(posibilidades))
        if (corrida[i] % 2 == 1):

            cantApuestasFavorables += 1

            #MARTINGALA
            gananciaMartingala.append(gananciaMartingala[i] + apuestaMartingala[i])
            capitalMartingala.append(capitalMartingala[i] + apuestaMartingala[i])
            apuestaMartingala.append(APUESTA_INICIAL)

            #FIBONACCI
            gananciaFibonacci.append(gananciaFibonacci[i] + apuestaFibonacci[i])
            capitalFibonacci.append(capitalFibonacci[i] + apuestaFibonacci[i])
            posicionFibonacci -= 2
            if posicionFibonacci < 2:
                posicionFibonacci = 2
            apuestaFibonacci.append(Fibonacci(posicionFibonacci))
            
            #DALAMBERT
            gananciaDAlembert.append(gananciaDAlembert[i] + apuestaDAlembert[i])
            capitalDAlembert.append(capitalDAlembert[i] + apuestaDAlembert[i])
            if apuestaDAlembert[i] == 1:    
                apuestaDAlembert.append(apuestaDAlembert[i])
            else:
                apuestaDAlembert.append(apuestaDAlembert[i]-1)

        else:

            #MARTINGALA
            gananciaMartingala.append(gananciaMartingala[i] - apuestaMartingala[i])
            capitalMartingala.append(capitalMartingala[i] - apuestaMartingala[i])
            apuestaMartingala.append(apuestaMartingala[i]*2)

            #FIBONACCI
            gananciaFibonacci.append(gananciaFibonacci[i] - apuestaFibonacci[i])
            capitalFibonacci.append(capitalFibonacci[i] - apuestaFibonacci[i])
            posicionFibonacci += 1
            apuestaFibonacci.append(Fibonacci(posicionFibonacci))
            
            #DALAMBERT
            gananciaDAlembert.append(gananciaDAlembert[i] - apuestaDAlembert[i])
            capitalDAlembert.append(capitalDAlembert[i] - apuestaDAlembert[i])
            apuestaDAlembert.append(apuestaDAlembert[i]+1)

        frecuentaRelativaAF.append(cantApuestasFavorables / (i+1))

    frecuencias.append(frecuentaRelativaAF)
    gananciasMartingala.append(gananciaMartingala)
    gananciasFibonacci.append(gananciaFibonacci)
    gananciasDAlembert.append(gananciaDAlembert)
        

figGanancias, axGanancias = plt.subplots(ncols = 3)
figGanancias.tight_layout()
axGanancias[0].set_title("Martingala")
axGanancias[1].set_title("Fibonacci")
axGanancias[2].set_title("D'Alembert")
for i in range(CANT_CORRIDAS):
    axGanancias[0].plot(gananciasMartingala[i])
    axGanancias[1].plot(gananciasFibonacci[i])
    axGanancias[2].plot(gananciasDAlembert[i])

figfrecuencia, axfrecuencia = plt.subplots()
for i in range(CANT_CORRIDAS):
    axfrecuencia.plot(frecuencias[i])



#MARTINGALA
plt.figure(num='Capital')
plt.xlabel('N')
plt.ylabel('Capital')
plt.plot(capitalMartingala)
plt.axhline(CAPITAL_INICIAL,color='red',ls='solid')

plt.figure(num='Ganancia')
plt.xlabel('N')
plt.ylabel('Ganancia')
plt.plot(gananciaMartingala)
plt.axhline(0,color='red',ls='solid')

plt.figure(num='Apuesta')
plt.xlabel('N')
plt.ylabel('Apuesta')
plt.plot(apuestaMartingala)


#FIBONACCI
plt.figure(num='Capital')
plt.xlabel('N')
plt.ylabel('Capital')
plt.plot(capitalFibonacci)
plt.axhline(CAPITAL_INICIAL,color='red',ls='solid')

plt.figure(num='Ganancia')
plt.xlabel('N')
plt.ylabel('Ganancia')
plt.plot(gananciaFibonacci)
plt.axhline(0,color='red',ls='solid')

plt.figure(num='Apuesta')
plt.xlabel('N')
plt.ylabel('Apuesta')
plt.plot(apuestaFibonacci)


#DALEMERT
plt.figure(num='Capital')
plt.xlabel('N')
plt.ylabel('Capital')
plt.plot(capitalDAlembert)
plt.axhline(CAPITAL_INICIAL,color='red',ls='solid')

plt.figure(num='Ganancia')
plt.xlabel('N')
plt.ylabel('Ganancia')
plt.plot(gananciaDAlembert)
plt.axhline(0,color='red',ls='solid')

plt.figure(num='Apuesta')
plt.xlabel('N')
plt.ylabel('Apuesta')
plt.plot(apuestaDAlembert)



plt.figure(num='Frecuencia relativa')
plt.xlabel('N')
plt.ylabel('Frecuencia relativa')
plt.bar(range(len(frecuentaRelativaAF)),frecuentaRelativaAF)



plt.show()