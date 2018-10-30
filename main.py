import os
from classes import *

mapp =  [[1, 2, 1, 0, 2, 4, 1, 1, 1, 1, 1],
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
endCoordinates = world.findEnd()
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
def mainLoop():
    global wrongAction
    clearScreen()
    WrongActionPopUp()
    if hero.isDead(): return 1
    printCurrentLocation()
    printMenu()
    player_choice = input("Wybierz kierunek: ")
    dir_x, dir_y = checkinput(player_choice)
    changeRooms(player_choice)
    moveHero(dir_x, dir_y)
    if GameEnded(): return 1

def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def endDirection():
    String = ""
    if hero.y > endCoordinates[1]:
        String += "północny "
    elif hero.y < endCoordinates[1]:
        String += "południowy "
    if hero.x > endCoordinates[0]:
        String += "zachód."
    elif hero.x < endCoordinates[0]:
        String += "wschód."
    if String == "południowy ":
        String = "południe."
    elif String == "północny ":
        String = "północ."
    return String

def WrongActionPopUp():
    global wrongAction
    if wrongAction:
        print("Nie możesz tego zrobić!\n")
        wrongAction = 0

##Następne funkcje są do wyświetlanie menu
def getFullOptionName(key_name):
    return f"[{key_name}] {keys[key_name]}"

def printCurrentLocation():
    print(f"{world.getAt(hero.x, hero.y).long_desc}")

def printMenu():
    print(f"Najwyraźniej, twoja lokalizacja to: {hero.x}, {hero.y}")
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

def printChoice(x, y, key_name):
    if x == None and y == None:
        print(getFullOptionName(key_name))
    elif world.exist(x, y):
        loc = world.getAt(x, y)
        if world.data[hero.y][hero.x] != world.data[y][x]:
            print(getFullOptionName(key_name), loc.short_desc)
        elif world.data[hero.y][hero.x] == world.data[y][x]:
            print(getFullOptionName(key_name), loc.same_room)

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
            hero.hp += randint(1, 5)
        else:
            hero.hp -= randint(3, 6)
        world.data[hero.y][hero.x] = '2_1'

    return direction_x, direction_y

def changeRooms(a):
    if str(world.data[hero.y][hero.x]) == '1_1':
        hero.hp -= 2
        world.data[hero.y][hero.x] = '1'
    elif str(world.data[hero.y][hero.x]) == '4' and a == 'q':
        world.data[hero.y][hero.x] = '4_1'
    elif str(world.data[hero.y][hero.x]) == '4_1':
        world.data[hero.y][hero.x] = '4_2'
    elif str(world.data[hero.y][hero.x]) == '4_2':
        hero.hp -= 7
        world.data[hero.y][hero.x] = '5'

def moveHero(direction_x, direction_y):
    global wrongAction
    next_pos_x = hero.x + direction_x
    next_pos_y = hero.y + direction_y
    if world.exist(next_pos_x, next_pos_y):
        hero.x = next_pos_x
        hero.y = next_pos_y
    else:
        wrongAction = True



def GameEnded():
    if world.data[hero.y][hero.x] == 'E':
        input("Gratulacje!\nTwojemu bohaterowi udało się znaleźć wyjście.\n Naciśnij enter by zakończyć przygodę!")
        return 1

##Początek gry
print("Uciekając przed bandytami, postanowiłeś się ukryć w pewnej jaskinii.\nNiestety potknąłeś się wpadając do lochów.\nTwój magiczny kompas wskazuje wyjście.")
input("Naciśnij Enter by zacząć grę!")

while not ended:
    ended = mainLoop()
