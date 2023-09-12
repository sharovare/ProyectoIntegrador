from readchar import readkey, key
import os

class Juego:
    
    def __init__(self, mapa, posIn, posFin):
        self.mapa = mapa
        self.posicionInicial = posIn
        self.posicionFinal = posFin

    def limpiarpantalla(self):
        os.system('cls' if os.name=='nt' else 'clear')
        for i in self.mapa:
            print("".join(i))

    def mainloop(self):
        py, px = self.posicionInicial
        while list((py, px)) != self.posicionFinal:
            self.mapa[py][px] = "P"
            self.limpiarpantalla()
            while True:
                k = readkey()
                if (k == key.UP and (py - 1) >= 0 and self.mapa[py - 1][px] != "#"):
                    self.mapa[py][px] = "."
                    py -= 1
                    break
                elif (k == key.DOWN and (py + 1) < len(self.mapa) and self.mapa[py + 1][px] != "#"):
                    self.mapa[py][px] = "."
                    py += 1
                    break
                elif (k == key.LEFT and (px - 1) >= 0 and self.mapa[py][px - 1] != "#"):
                    self.mapa[py][px] = "."
                    px -= 1
                    break
                elif (k == key.RIGHT and (px + 1) <= len(self.mapa[0]) and self.mapa[py][px + 1] != "#"):
                    self.mapa[py][px] = "."
                    px += 1
                    break