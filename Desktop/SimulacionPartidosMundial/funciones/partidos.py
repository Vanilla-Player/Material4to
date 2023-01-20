import numpy as np

PROMEDIO_XGA = 1.1112
PROMEDIO_XG = 1.552
PROMEDIO_XG2 = 1.37



def SimularPartidos(team1, team2, cant_paritdos):

    resultados = [0,0,0,0,0]


    xGH1 = team1['xG']
    xGH2 = team1['xG2']
    xGA1 = team1['xGA']
    xGAw1 = team2['xG']
    xGAw2 = team2['xG2']
    xGA2 = team2['xGA']

    rankingHome = team1['ranking']
    rankingAway = team2['ranking']


    rankDif1 = rankingHome/rankingAway
    rankDif2 = rankingAway/rankingHome

    xG1 = (xGH1/PROMEDIO_XG + xGH2/PROMEDIO_XG2)/2

    xG2 = (xGAw1/PROMEDIO_XG +xGAw2/PROMEDIO_XG2)/2 

    lambda1 = (xG1*(xGA2/PROMEDIO_XGA)*rankDif1)
    lambda2 = (xG2*(xGA1/PROMEDIO_XGA)*rankDif2)


    for i in range(cant_paritdos):
        golesEquipo1 = np.random.poisson(lam=lambda1)
        golesEquipo2 = np.random.poisson(lam=lambda2)

        resultados[3] += golesEquipo1
        resultados[4] += golesEquipo2

        if(golesEquipo1 > golesEquipo2):
            resultados[0] += 1

        if(golesEquipo1 < golesEquipo2):
            resultados[2] += 1
            
        if(golesEquipo1 == golesEquipo2):
            resultados[1] += 1


    return resultados



