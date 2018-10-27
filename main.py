import os
from classes import *
from functions import *

mapp = [[1,2, 1, 0, 2, 4, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 4],
        [0, 1, 1, 0, 0, 1, 1, 1, 4, 0, 1],
        [1, 4, 0, 2, 0, 5, 4, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1],
        [1, 2, 0, 4, 0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 1, 0, 4, 0, 0,'E',0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1],
        [5, 0, 1, 5, 1, 0, 1, 1, 1, 1, 0]]

world = World(mapp)
world.data = AddTraps(world)
hero = Character(0, 0, 10)
Ended = False
EndCoordinates = FindEnd(world)
wrongAction = False

keys = {
    'w': "Północ:",
    's': "Południe:",
    'a': "Zachód:",
    'd': "Wschód:",
    'q': "Zabrać amulet?",
    'e': "Zjeść ze stołu?"
}

print("Uciekając przed bandytami, postanowiłeś się ukryć w pewnej jaskinii.\nNiestety potknąłeś się wpadając do lochów.\nTwój magiczny kompas wskazuje wyjście.")
input("Naciśnij Enter by zacząć grę!")

while not Ended:
    mainLoop()
