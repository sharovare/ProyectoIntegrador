from readchar import readkey, key
import os

maze = '''
..###################
........#.....#.#...#
#.#.#######.###.#.###
#.#.....#.#.........#
#.#######.###.#####.#
#.....#...#...#.....#
###.#.#.###.#####.#.#
#.#.#.....#...#...#.#
#.#.###.###.#.#.#.#.#
#...#.......#.#.#.#.#
###.#.#############.#
#.#.#.....#.#...#.#.#
#.#.#####.#.#.###.###
#.....#...#.#.......#
#####.###.#.#.#####.#
#...#...#.....#.....#
###.#######.#####.#.#
#.#.#.......#.#...#.#
#.#.###.#.#.#.#.#####
#.......#.#...#......
###################.. 
'''
initialposition = (0, 0)
finalposition = (20, 20)

def mapalab(laberinto):
    return list(map(list,laberinto.strip().split("\n")))

l = mapalab(maze)

def limpiarpantalla(laberinto1):
    os.system('cls' if os.name=='nt' else 'clear')
    for i in laberinto1:
        print("".join(i))

def mainloop(laberinto2, initpos, finpos):
    py, px = initpos
    while (py, px) != finpos:
        laberinto2[py][px] = "P"
        limpiarpantalla(laberinto2)
        while True:
            k = readkey()
            if (k == key.UP and (py - 1) >= 0 and laberinto2[py - 1][px] != "#"):
                laberinto2[py][px] = "."
                py -= 1
                break
            elif (k == key.DOWN and (py + 1) <= len(laberinto2) and laberinto2[py + 1][px] != "#"):
                laberinto2[py][px] = "."
                py += 1
                break
            elif (k == key.LEFT and (px - 1) >= 0 and laberinto2[py][px - 1] != "#"):
                laberinto2[py][px] = "."
                px -= 1
                break
            elif (k == key.RIGHT and (px + 1) >= 0 and laberinto2[py][px + 1] != "#"):
                laberinto2[py][px] = "."
                px += 1
                break
            

mainloop(l, initialposition, finalposition)

