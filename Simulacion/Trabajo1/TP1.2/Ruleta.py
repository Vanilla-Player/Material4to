
import Apuestas 
import TipoApuestas
import Estrategias
import random
import Personas

CANTIDAD_REPETICIONES = 30



def dalembert(apuesta):
    apuesta.cantidad += 1



def crearPersona():
    #Aca hay se decide la cantidad de dinero que tiene la persona
    p = Personas.Persona(100)
    #Aca hay se decide la cantidad de dinero que tiene la persona
    p.tipoEstrategia(1)

    return p

def apostar():
    bandera = 0
    cantidadInsuficiente = 1
    cantidad_para_apostar = persona.billetera # Lo hago de este modo porque sino no me andaba abajo xd
    while bandera == 0 or cantidadInsuficiente == 1:
        multiplicador = 0
        numerosApostados = []
        #Elegir cantidad a apostar
        cantidad = 10
        #Elegir cantidad a apostar
        cantidadInsuficiente, cantidad_para_apostar = realizarApuesta(cantidad, numerosApostados, multiplicador, cantidad_para_apostar)
        if cantidadInsuficiente == 0:
            break
            
        bandera = int(input("Quiere realizar otra apuesta? "))



def realizarApuesta(c, n, m, cantidad_para_apostar):
    a = Apuestas.Apuesta()
    if(cantidad_para_apostar >= c):
        cantidad_para_apostar -= c
        #Elegir Apuesta
        m = TipoApuestas.pares(n)
        #Elegir Apuesta

        a.setCantidad(c)
        a.setMultiplicador(m)
        a.setNumeros(n)
        persona.sumarApuesta(a)
    else:
        print("Dinero no suficiente")
        return 0, cantidad_para_apostar
    return 1, cantidad_para_apostar




persona = crearPersona()


apostar()

dineroGANADO = 0
dineroPerdido = 0

#### Desde aca para abajo
contador= 0
while (contador < CANTIDAD_REPETICIONES):
    for apuesta in persona.apuestas:
        persona.billetera -= apuesta.cantidad
        #Puedo tener dinero negativo??? o tiro un break
        salio = random.randint(0,36)
        piso = apuesta.cantidad # Valor al cual volver, en este caso es cuando se gana por el metodo dalembert

        if salio in apuesta.numeros:
            print("Salioo!!")
            dineroGANADO += (apuesta.cantidad)
            persona.billetera += (apuesta.cantidad*apuesta.multiplicador)
            if(persona.estrategia == 1):
                apuesta.cantidad = piso
            elif(persona.estrategia == 2):
                print("falta implementar")
            elif(persona.estrategia == 3):
                print("falta Implementar")
           
        else:
            print("Suerte la proxima")
            dineroPerdido -= apuesta.cantidad
            if(persona.estrategia == 1):
                dalembert(apuesta)
            elif(persona.estrategia == 2):
                print("falta implementar")
            elif(persona.estrategia == 3):
                print("falta Implementar")
    
            
    contador+=1

            

        
print("Dinero Final")
print(persona.billetera)

print("Dinero ganado")
print(dineroGANADO)

print("Dinero perdido")
print(dineroPerdido)



















