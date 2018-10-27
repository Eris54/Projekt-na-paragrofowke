import os

from classes import *

game_running = True
world = World()
hero = Character(0, 0)

keys = {
    "polnoc": "w",
    "poludnie": "s",
    "zachod": "a",
    "wschod": "d",
}

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def getFullOptionName(option_name):
    return f"[{keys[option_name]}] {option_name}"

def printChoice(x, y, option_name):
    if world.exist(x, y):
        loc = world.getAt(x, y)
        print(f"{getFullOptionName(option_name)}: {loc.short_desc}")

def printChoices():
    printChoice(hero.x - 1, hero.y, "zachod")
    printChoice(hero.x + 1, hero.y, "wschod")
    printChoice(hero.x, hero.y + 1, "poludnie")
    printChoice(hero.x, hero.y - 1, "polnoc")

def printCurrentLocation():
    print(f"{world.getAt(hero.x, hero.y).long_desc}")

def moveHero(direction_x, direction_y):
    next_pos_x = hero.x + direction_x
    next_pos_y = hero.y + direction_y
    if world.exist(next_pos_x, next_pos_y):
        hero.x = next_pos_x
        hero.y = next_pos_y

def checkinput(player_choice):
    direction_x = 0
    direction_y = 0

    if player_choice == keys["polnoc"]:
        direction_y = -1
    elif player_choice == keys["wschod"]:
        direction_x = 1
    elif player_choice == keys["poludnie"]:
        direction_y = 1
    elif player_choice == keys["zachod"]:
        direction_x = -1

    return direction_x, direction_y

def gameOver():
    global game_running 
    game_running = False
    print("Ukonczyles gre.")
    print("Nacisnij dowolny klawisz, aby kontynuowac.")
    input()

def loop():
    printCurrentLocation()
    printChoices()
    player_choice = input("Wybierz kierunek: ")
    dir_x, dir_y = checkinput(player_choice)
    moveHero(dir_x, dir_y)
    if world.isExit(hero.x, hero.y):
        gameOver()

while game_running:
    clearScreen()
    loop()
