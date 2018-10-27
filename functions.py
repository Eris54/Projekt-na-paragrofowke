from random import randint
import os

def clearScreen():              ##Wieloplatformowość
    os.system('cls' if os.name=='nt' else 'clear')

def mainLoop():
    global wrongAction
    clearScreen()

    if hero.hp <= 0:
        print('Twój bohater zginął.\nPrzegrałeś!')
        Ended = 1
        return 0

    if wrongAction:
        print("Nie możesz tego zrobić!\n")
        wrongAction = 0

    printCurrentLocation()
    printChoices()
    player_choice = input("Wybierz kierunek: ")
    dir_x, dir_y = checkinput(player_choice)
    moveHero(dir_x, dir_y)
    if world.data[hero.y][hero.x] == 'E':
        Ended = 1
        input("Naciśnij enter by zakończyć przygodę!")


def AddTraps(where):
    for i in range(20):  ##Dodawanie losowych pułapek
        x = randint(0, where.width)
        y = randint(0, where.height)
        if str(where.data[y][x]) == '1':
            where.data[y][x] = '1_1'
    return where.data

def FindEnd(where):
    counterx, countery = 0, 0
    for i in where.data:
        for j in i:
            if j == 'E':
                return [counterx, countery]
            counterx += 1
        countery +=1
        counterx = 0

def EndDirection():
    String = ""
    if hero.y > EndCoordinates[1] + 1:
        String += "północny "
    elif hero.y < EndCoordinates[1] - 1:
        String += "południowy "
    if hero.x > EndCoordinates[0] + 1:
        String += "zachód."
    elif hero.x < EndCoordinates[0] - 1:
        String += "wschód."
    if String == "południowy ":
        String = "południe."
    elif String == "północny ":
        String = "północ."
    return String

def getFullOptionName(option_name):
    return f"[{option_name}] {keys[option_name]}"

def printChoice(x, y, option_name):
    if x == None and y == None:
        print(getFullOptionName(option_name))
    elif world.exist(x, y):
        loc = world.getAt(x, y)
        if world.data[hero.y][hero.x] != world.data[y][x]:
            print(getFullOptionName(option_name), loc.short_desc)
        elif world.data[hero.y][hero.x] == world.data[y][x]:
            print(getFullOptionName(option_name), loc.same_room)

def printChoices():
    print(f"Najwyraźniej, twoja lokalizacja to: {hero.x}, {hero.y}")
    print("\nKompas wskazuje:", EndDirection())
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

def checkinput(player_choice):
    player_choice.lower()
    direction_x = 0
    direction_y = 0

    if str(world.data[hero.y][hero.x]) == '1_1':  ##Zmienianie odwiedzonych pokoi
        hero.hp -= 2
        world.data[hero.y][hero.x] = '1'
    elif str(world.data[hero.y][hero.x]) == '4_1':
        world.data[hero.y][hero.x] = '4_2'
    elif str(world.data[hero.y][hero.x]) == '4_2':
        hero.hp = 4
        world.data[hero.y][hero.x] = '5'

    if player_choice == 'w':
        direction_y = -1
    elif player_choice == 'd':
        direction_x = 1
    elif player_choice == 's':
        direction_y = 1
    elif player_choice == 'a':
        direction_x = -1

    elif player_choice == 'q' and str(world.data[hero.y][hero.x]) == '4':
        world.data[hero.y][hero.x] = '4_1'
        hero.hp += 4

    elif player_choice == 'e' and str(world.data[hero.y][hero.x]) == '2':
        chance = randint(0,5)
        if chance <= 1:
            hero.hp += randint(1, 5)
        else:
            hero.hp -= randint(3, 7)
        world.data[hero.y][hero.x] = '2_1'

    return direction_x, direction_y
