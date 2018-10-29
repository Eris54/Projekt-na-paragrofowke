#!/usr/bin/python3
from random import randint
import os
from classes import *

mapp = [[1, 2, 1, 0, 2, 4, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 4],
        [0, 1, 1, 0, 0, 1, 1, 1, 4, 0, 1],
        [1, 4, 0, 2, 0, 5, 4, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1],
        [1, 2, 1, 4, 0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 1, 0, 4, 0, 0,'E',0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1],
        [5, 0, 1, 5, 1, 0, 1, 1, 1, 1, 0]]

world = World(mapp)
hero = Character(0, 0, 20)
ended = False
wrongAction = False

keys = {
    'w': "Północ:",
    's': "Południe:",
    'a': "Zachód:",
    'd': "Wschód:",
    'q': "Zabrać amulet?",
    'e': "Zjeść ze stołu?"
}

##Funkcje
def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def mainLoop():
    global wrongAction, ended
    clearScreen()

    if hero.hp <= 0:
        print('Twój bohater zginął.\nPrzegrałeś!')
        ended = 1
        return 0

    if wrongAction:
        print("Nie możesz tego zrobić!\n")
        wrongAction = 0

    printCurrentLocation()
    printMenu()
    player_choice = input("Wybierz kierunek: ")
    dir_x, dir_y = checkinput(player_choice)
    changeRooms()
    moveHero(dir_x, dir_y)
    if world.data[hero.y][hero.x] == 'E':
        ended = 1
        print("Udało się ukończyć grę!\n gratulacje!")
        input("Naciśnij enter by zakończyć przygodę!")


def addTraps(where):
    for i in range(12):  ##Dodawanie losowych pułapek
        x = randint(0, where.width)
        y = randint(0, where.height)
        if str(where.data[y-1][x-1]) == '1':
            where.data[y-1][x-1] = '1_1'
    return where.data

def findEnd(where):
    counterx, countery = 0, 0
    for i in where.data:
        for j in i:
            if j == 'E':
                return [counterx, countery]
            counterx += 1
        countery +=1
        counterx = 0

def endDirection():
    String = ""
    if hero.y > endCoordinates[1] + 1:
        String += "północny "
    elif hero.y < endCoordinates[1] - 1:
        String += "południowy "
    if hero.x > endCoordinates[0] + 1:
        String += "zachód."
    elif hero.x < endCoordinates[0] - 1:
        String += "wschód."
    if String == "południowy " or(hero.y > endCoordinates[1] -1 and hero.y < endCoordinates[1] +1):
        String = "południe."
    elif String == "północny " or(hero.x > endCoordinates[0] -1 and hero.x < endCoordinates[1] +1):
        String = "północ."
    return String

def getFullOptionName(key_name):
    return f"[{key_name}] {keys[key_name]}"

def printChoice(x, y, key_name):
    if x == None and y == None:
        print(getFullOptionName(key_name))
    elif world.exist(x, y):
        loc = world.getAt(x, y)
        if world.data[hero.y][hero.x] != world.data[y][x]:
            print(getFullOptionName(key_name), loc.short_desc)
        elif world.data[hero.y][hero.x] == world.data[y][x]:
            print(getFullOptionName(key_name), loc.same_room)

def printMenu():
    print(f"Twoja lokalizacja to: {hero.x}, {hero.y}")
    print("\nKompas wskazuje:", endDirection())
    print("Twoje zdrowie to:", hero.hp, '\n')
    printChoice(hero.x - 1, hero.y, "a")
    printChoice(hero.x + 1, hero.y, "d")
    printChoice(hero.x, hero.y + 1, "s")
    printChoice(hero.x, hero.y - 1, "w")
    if str(world.data[hero.y][hero.x]) == '2':
        printChoice(None, None, 'e')
    elif str(world.data[hero.y][hero.x]) == '4':
        printChoice(None, None, 'q')

def printCurrentLocation():
    print(f"{world.getAt(hero.x, hero.y).long_desc}")

def moveHero(direction_x, direction_y):
    global wrongAction
    next_pos_x = hero.x + direction_x
    next_pos_y = hero.y + direction_y
    if world.exist(next_pos_x, next_pos_y):
        hero.x = next_pos_x
        hero.y = next_pos_y
    else:
        wrongAction = True
        
def changeRooms():
    if str(world.data[hero.y][hero.x]) == '1_1':  ##Zmienianie odwiedzonych pokoi
        hero.hp -= 2
        world.data[hero.y][hero.x] = '1'
    
    elif str(world.data[hero.y][hero.x]) == '4':
        world.data[hero.y][hero.x] = '4_1'
    elif str(world.data[hero.y][hero.x]) == '4_1':
        world.data[hero.y][hero.x] = '4_2'
    elif str(world.data[hero.y][hero.x]) == '4_2':
        hero.hp -= 6
        world.data[hero.y][hero.x] = '5'
        
def checkinput(player_choice):
    player_choice.lower()
    direction_x = 0
    direction_y = 0

    if player_choice == 'w':
        direction_y = -1
    elif player_choice == 'd':
        direction_x = 1
    elif player_choice == 's':
        direction_y = 1
    elif player_choice == 'a':
        direction_x = -1

    elif player_choice == 'q' and str(world.data[hero.y][hero.x]) == '4':
        hero.hp += 4

    elif player_choice == 'e' and str(world.data[hero.y][hero.x]) == '2':
        chance = randint(0,5)
        if chance <= 1:
            hero.hp += randint(2, 6)
        else:
            hero.hp -= randint(1, 3)
        world.data[hero.y][hero.x] = '2_1'

    return direction_x, direction_y

world.data = addTraps(world)
endCoordinates = findEnd(world)
print("Uciekając przed bandytami, postanowiłeś się ukryć w pewnej jaskinii.\nNiestety potknąłeś się wpadając do lochów.\nTwój magiczny kompas wskazuje wyjście.")
input("Naciśnij Enter by zacząć grę!")

while not ended:
    mainLoop()
