
import math
import matplotlib.pyplot as plt
import numpy as np




# En este se saca la probabilidad de anotar x goles en un partido con un lambda especifico



xG1 = 2.71 # Lambda

# def calculateProbability(xG1, goals):

#     probability = math.exp(-xG1)*(xG1**goals)/math.factorial(goals)

#     return probability




# probabilities = []




# for i in range(9):

#     result = calculateProbability(xG1, i+1)

#     probabilities.append(result)






print(np.random.poisson(lam=xG1))


