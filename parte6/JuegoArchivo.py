import os, random
from Juego import *

class JuegoArchivo(Juego):
    def __init__(self, path_mapas):       
        self.path = f"{path_mapas}/{random.choice(os.listdir(path_mapas))}" 
        mapa, posIn, posFin = self.leer()
        super().__init__(mapa, posIn, posFin)

    def leer(self):
        with open(self.path, 'r') as leerArchivo:
            lineas = leerArchivo.readlines()
            posiciones = list(map(int, lineas[0].strip().split()))
            mapas = list(map(lambda x: list(x.strip()), lineas[1:]))
            return mapas, posiciones[0:2], posiciones[2:]
        
'''prueba = JuegoArchivo('parte5\Maps')
print(prueba.leer())'''
        

