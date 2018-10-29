from game_state import *
from game_maths import *
from location import *
from val_defs import *


# Action definitions

def trapAction():
    print(long_descriptions['pulapka_aktywowana'])
    gameState.hero.hp -= settings['trap_damage']

trap_action = Action("visit", 1, trapAction)

def eatAction():
    cur_loc = gameState.getPlayerLocation()
    cur_loc.long_desc_keys.pop('sala_obiadowa_jedzenie')
    cur_loc.long_desc_keys.append('sala_obiadowa_brak_jedzenia')
    cur_loc.same_room.short_desc_key = 'dalsza_jadalnia'

    hero = gameState.hero
    if randomDecision(settings['food_poison_chance']):
        hero.hp -= randint(settings['food_poison_pts_min'], settings['food_poison_pts_max'])
    else:
        hero.hp += randint(settings['food_heal_pts_min'], settings['food_heal_pts_max'])

eat_action = PlayerAction(1, "e", "Zjedz ze stołu", eatAction)


def secondVisitAfterTakingAmulet():
    cur_loc = gameState.getPlayerLocation()
    cur_loc.short_desc = 'drzwi_slady_magii'
    cur_loc.long_desc_keys.pop('pulapka_duch')
    cur_loc.long_desc_keys.append('pokoj_czarnoksieznika')
    gameState.hero.hp -= settings['ghost_damage']

def firstVistAfterTakingAmulet():
    cur_loc = gameState.getPlayerLocation()
    cur_loc.short_desc = 'ciemne_drzwi_cos_przyciaga'
    cur_loc.long_desc_keys.pop('cos_zlego')
    cur_loc.long_desc_keys.append('pulapka_duch')
    cur_loc.addAction(Action("visit", 1, secondVisitAfterTakingAmulet))

def takeAmuletAction():
    cur_loc = gameState.getPlayerLocation()
    cur_loc.short_desc = 'ciemne_drzwi_cos_w_srodku'
    cur_loc.long_desc_keys.pop('amulet')
    cur_loc.long_desc_keys.append('cos_zlego')
    gameState.hero.hp += settings['amulet_heal_pts']
    cur_loc.addAction(Action("visit", 1, firstVisitAfterTakingAmulet))

take_amulet_action = PlayerAction(1, "q", "Zabierz amulet", takeAmuletAction)



# Location definitions

def trapRoom():
    room = Location(
            'male_drzwi',
            ['ciasny_korytarz'],
            'dalszy_korytarz')

    if randomDecision(settings['trap_chance']):
        room.addAction(trap_action)

    return room


def diningRoom():
    room = Location(
            'ciezkie_drzwi',
            ['sala_obiadowa_jedzenie'],
            'dalsza_jadalnia_stol')
    room.addAction(eat_action)
    return room


def scaryRoom():
    room = Location(
            'ciemne_drzwi',
            ['amulet'])
    room.addAction(take_amulet_acion)
    return room


def neutralRoom():
    return Location(
            'drzwi_slady_magii',
            ['pokoj_czarnoksieznika'])


def exit():
    return Location(
            'wyjscie',
            ['wyjscie'])


loc_generators: {
    1: trapRoom,
    2: diningRoom,
    3: scaryRoom,
    4: neutralRoom,
    5: exit,
}


