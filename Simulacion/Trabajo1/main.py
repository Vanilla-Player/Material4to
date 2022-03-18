# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import matplotlib.pyplot as plt
import random
CANT_REPETICIONES = 100
posibilidades = []
for i in range(37):
    posibilidades.append(i)

sum = 0
promedios = []
for i in range(CANT_REPETICIONES):
    sum += random.choice(posibilidades)
    promedios.append(sum/(i+1))

print(sum/CANT_REPETICIONES)

print(promedios)
plt.plot(promedios)
plt.show()