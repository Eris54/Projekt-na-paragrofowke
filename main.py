import os
import game_state

world = game_state.world
hero = game_state.hero
gameFinished = False
invalidPlayerMove = False

keys = {
    'w': "Północ:",
    's': "Południe:",
    'a': "Zachód:",
    'd': "Wschód:",
}


##Funkcje
def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def mainLoop():
    if checkIfPlayerIsDead():
        return
    checkIfInvalidPlayerMove()
    printCurrentLocation()
    printMenu()
    player_choice = input("Wybierz kierunek: ")
    dir_x, dir_y = checkInput(player_choice)
    moveHero(dir_x, dir_y)

def checkIfPlayerIsDead():
    global gameFinished
    if hero.hp > 0:
        return False
    print('Twój bohater zginął.\nPrzegrałeś!\n\nNaciśnij Enter by zakończyć przygodę.')
    gameFinished = 1
    input()
    return True

def checkIfInvalidPlayerMove():
    global invalidPlayerMove
    if invalidPlayerMove:
        print("Nie możesz tego zrobić!\n")
        invalidPlayerMove = 0

def checkIfPlayerReachedExit():
    global gameFinished
    if world.data[hero.y][hero.x] == 'E':
        gameFinished = 1
        print("Udało się ukończyć grę!\n\t\tGratulacje!")
        input("Naciśnij enter by zakończyć przygodę!")
    

"""
def endDirection():
    String = ""
    if hero.y >= endCoordinates[1]:
        String += "północny "
    elif hero.y < endCoordinates[1]:
        String += "południowy "
    if hero.x >= endCoordinates[0]:
        String += "zachód."
    elif hero.x < endCoordinates[0]:
        String += "wschód."
    if hero.y < endCoordinates[1] and hero.x == endCoordinates[0]:
        String = "południe."
    elif hero.y > endCoordinates[1] and hero.x == endCoordinates[0]:
        String = "północ."
    return String
"""

def getFullOptionName(key_name):
    return f"[{key_name}] {keys[key_name]}"

def printChoice(x, y, key_name):
    if not world.exist(x, y):
        return

    loc = game_state.world.getAt(x, y)
    cur_loc = game_state.getPlayerLocation()
    if loc.isInGroupWith(cur_loc):
        print(getFullOptionName(key_name), loc.getSameRoomDescription())
    else:
        print(getFullOptionName(key_name), loc.getShortDescription())

def printMenu():
    print(f"Twoja lokalizacja to: {hero.x}, {hero.y}")
    #print("\nKompas wskazuje:", endDirection())
    print("Twoje zdrowie to:", hero.hp, '\n')
    printChoice(hero.x - 1, hero.y, "a")
    printChoice(hero.x + 1, hero.y, "d")
    printChoice(hero.x, hero.y + 1, "s")
    printChoice(hero.x, hero.y - 1, "w")
    print(game_state.getPlayerLocation().getPlayerActionsDescription())

def printCurrentLocation():
    print(f"{world.getAt(hero.x, hero.y).getLongDescription()}")

def moveHero(direction_x, direction_y):
    global invalidPlayerMove

    if direction_x == 0 and direction_y == 0:
        return

    next_pos_x = hero.x + direction_x
    next_pos_y = hero.y + direction_y

    if world.exist(next_pos_x, next_pos_y):
        hero.x = next_pos_x
        hero.y = next_pos_y
        game_state.getPlayerLocation().triggerAction("visit")
    else:
        invalidPlayerMove = True
        
def checkInput(player_choice):
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
    else:
        game_state.getPlayerLocation().triggerPlayerAction(player_choice)

    if direction_x != 0 or direction_y != 0:
        game_state.getPlayerLocation().triggerAction("leave")

    return direction_x, direction_y

print("Uciekając przed bandytami, postanowiłeś się ukryć w pewnej jaskinii.\nNiestety potknąłeś się wpadając do lochów.\nTwój magiczny kompas wskazuje wyjście.")
input("Naciśnij Enter by zacząć grę!")

clearScreen()
game_state.getPlayerLocation().triggerAction("visit")

while not gameFinished:
    mainLoop()
    clearScreen()
