
class Apuesta:
  def __init__(self):
    self.numeros = []
    self.multiplicador = 0
    self.cantidad = 0
  
  def setMultiplicador(self, m):
    self.multiplicador = m
  def setCantidad(self, c):
    self.cantidad = c
  def setNumeros(self, n):
    self.numeros = n


