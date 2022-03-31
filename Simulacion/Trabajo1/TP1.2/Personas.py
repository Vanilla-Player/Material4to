


class Persona:
  
    def __init__(self, b):
        self.billetera = b
        self.apuestas = []
    
    def sumarApuesta(self, apuesta):
        self.apuestas.append(apuesta)
    
    def tipoEstrategia(self, tipo):
        self.estrategia = tipo

