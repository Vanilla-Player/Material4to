from db.equipos import equipos
from db.grupos import grupos
from funciones.partidos import SimularPartidos

CANT_PARTIDOS = 1000000




print("Ingrese Pais 1")

pais1 = input()
equipo1 = equipos[pais1]


print("Ingrese Pais 2")

pais2 = input()
equipo2 = equipos[pais2]



resultadoPartidos = SimularPartidos(equipo1, equipo2, CANT_PARTIDOS)


print()

print("Porcentaje de " + pais1)

print("Victoria")

print(resultadoPartidos[0]*100/CANT_PARTIDOS)

print("Empate")
print(resultadoPartidos[1]*100/CANT_PARTIDOS)

print("Derrota")
print(resultadoPartidos[2]*100/CANT_PARTIDOS)

    
print()
print("Goles promedio de " + pais1)
print(resultadoPartidos[3]/CANT_PARTIDOS)
print()
print("Goles promedio de" + pais2)
print(resultadoPartidos[4]/CANT_PARTIDOS)

