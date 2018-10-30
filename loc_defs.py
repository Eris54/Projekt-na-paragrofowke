from game_maths import *
from location import *
from val_defs import *
import game_state
from random import randint


# Action definitions

def trapAction():
    print(long_descriptions['pulapka_aktywowana'])
    game_state.hero.hp -= settings['trap_damage']

trap_action = Action("visit", 1, trapAction)


def eatAction():
    cur_loc = game_state.getPlayerLocation()
    cur_loc.long_desc_keys.remove('sala_obiadowa_jedzenie')
    cur_loc.long_desc_keys.append('sala_obiadowa_brak_jedzenia')
    cur_loc.same_room_short_desc_key = 'dalsza_jadalnia'

    hero = game_state.hero
    if randomDecision(settings['food_poison_chance']):
        hero.hp -= randint(settings['food_poison_pts_min'], settings['food_poison_pts_max'])
    else:
        hero.hp += randint(settings['food_heal_pts_min'], settings['food_heal_pts_max'])

eat_action = PlayerAction(1, "e", "Zjedz ze stołu", eatAction)


def LeaveAfterThirdVisit():
    cur_loc = game_state.getPlayerLocation()
    cur_loc.short_desc_key = 'drzwi_slady_magii'
    cur_loc.long_desc_keys.remove('pulapka_duch')
    cur_loc.long_desc_keys.append('pokoj_czarnoksieznika')

def ThirdVisitAfterTakingAmulet():
    game_state.hero.hp -= settings['ghost_damage']
    game_state.getPlayerLocation().addAction(Action("leave", 1, LeaveAfterThirdVisit))

def leaveAfterSecondVisit():
    cur_loc = game_state.getPlayerLocation()
    cur_loc.short_desc_key = 'ciemne_drzwi_cos_przyciaga'
    cur_loc.long_desc_keys.remove('cos_zlego')
    cur_loc.long_desc_keys.append('pulapka_duch')
    game_state.getPlayerLocation().addAction(Action("visit", 1, ThirdVisitAfterTakingAmulet))

def leaveAfterTakingAmulet():
    cur_loc = game_state.getPlayerLocation()
    cur_loc.short_desc_key = 'ciemne_drzwi_cos_w_srodku'
    cur_loc.addAction(Action("leave", 1, leaveAfterSecondVisit))

def takeAmuletAction():
    cur_loc = game_state.getPlayerLocation()
    game_state.hero.hp += settings['amulet_heal_pts']
    cur_loc.long_desc_keys.remove('amulet')
    cur_loc.long_desc_keys.append('cos_zlego')
    cur_loc.addAction(Action("leave", 1, leaveAfterTakingAmulet))

take_amulet_action = PlayerAction(1, "q", "Zabierz amulet", takeAmuletAction)


def testAction():
    game_state.hero.hp -= 1

test_action = Action("visit", 10, testAction)


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
    room.addAction(take_amulet_action)
    return room


def neutralRoom():
    return Location(
            'drzwi_slady_magii',
            ['pokoj_czarnoksieznika'])


def exitLocation():
    return Location(
            'wyjscie',
            ['wyjscie'])

def testRoom():
    room = Location(
            'wyjscie',
            ['wyjscie'])
    room.addAction(test_action)
    return room


