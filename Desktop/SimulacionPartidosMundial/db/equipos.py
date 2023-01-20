
#Implementar xGwc que se actualiza con los partidos del mundial
# Link: https://expectedscore.com/division/world/world-cup-2022/

equipos = {
    "Argentina":{'ranking':1773.88,'xG':1.85, 'xGA':0.88, 'xG2':1.88},
    "Arabia Saudi":{'ranking':1437.78,'xG':1.07, 'xGA':1.33, 'xG2':1.48},
    "Australia":{'ranking':1488.72,'xG':1.44, 'xGA':1.34, 'xG2':1.76},
    "Alemania":{'ranking':1650.21,'xG':2.4, 'xGA':1.18, 'xG2':1.16},
    "Belgica":{'ranking':1816.71,'xG':1.73, 'xGA':1.21, 'xG2':1.78},
    "Brasil":{'ranking':1841.3,'xG':2.29,  'xGA':0.97, 'xG2':1.84},
    "Camerun":{'ranking':1471.44,'xG':1.67, 'xGA':1.08, 'xG2':0.96},
    "Canada":{'ranking':1475,'xG':1.64, 'xGA':1.13, 'xG2':1.36},
    "Costa Rica":{'ranking':1503.59,'xG':1.08, 'xGA':1.93, 'xG2':0.77},
    "Croacia":{'ranking':1645.64,'xG':1.69, 'xGA':1.11, 'xG2':0.81},
    "Corea":{'ranking':1530.3,'xG':1.73, 'xGA':1.09, 'xG2':1.81},
    "Dinamarca":{'ranking':1666.57,'xG':1.35, 'xGA':1.43, 'xG2':1.36},
    "Espania":{'ranking':1715.22,'xG':1.57, 'xGA':0.79, 'xG2':1.14},
    "Estados Unidos":{'ranking':1627.48,'xG':1.96, 'xGA':1.19, 'xG2':1.41},
    "Ecuador":{'ranking':1464.39,'xG':1.62, 'xGA':1.26, 'xG2':0.94},
    "Francia":{'ranking':1759.78,'xG':2.22, 'xGA':0.88, 'xG2':1.40},
    "Ghana":{'ranking':1393,'xG':1.46, 'xGA':1.26, 'xG2':0.67},
    "Gales":{'ranking':1569.82,'xG':1.33, 'xGA':1.62, 'xG2':0.85},
    "Inglaterra":{'ranking':1728.47,'xG':1.97, 'xGA':1.08, 'xG2':1.13},
    "Iran":{'ranking':1564.61,'xG':1.52, 'xGA':0.95, 'xG2':2.2},
    "Japon":{'ranking':1559.54,'xG':2.05, 'xGA':0.95, 'xG2':2.17},
    "Marruecos":{'ranking':1563.5,'xG':2.08, 'xGA':1.05, 'xG2':1.18},
    "Mexico":{'ranking':1644.89,'xG':1.9, 'xGA':0.8, 'xG2':1.47},
    "Paises Bajos":{'ranking':1694.51,'xG':1.61, 'xGA':1.07, 'xG2':1.49},
    "Portugal":{'ranking':1676.56,'xG':1.86, 'xGA':1.1, 'xG2':1.86},
    "Polonia":{'ranking':1548.59,'xG':1.18, 'xGA':1.52, 'xG2':0.91},
    "Qatar":{'ranking':1439.89,'xG':1.36, 'xGA':1.33, 'xG2':1.71},
    "Suiza":{'ranking':1635.92,'xG':1.45, 'xGA':1.23, 'xG2':0.98},
    "Serbia":{'ranking':1563.62,'xG':1.47, 'xGA':1.05, 'xG2':1.79},
    "Senegal":{'ranking':1584.38,'xG':2.05, 'xGA':0.94, 'xG2':1.75},
    "Tunez":{'ranking':1597.54,'xG':1.39, 'xGA':1.23, 'xG2':0.97},
    "Uruguay":{'ranking':1638.71,'xG':1.91, 'xGA':1.02, 'xG2':0.92},
}

#print(equipos['Argentina']['xG']) 
# Salida => 2
