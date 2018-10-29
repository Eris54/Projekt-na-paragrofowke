class World:
    def __init__(self, mapa):
        self.data = mapa
        self.width = len(self.data[0])
        self.height = len(self.data)

    def exist(self, x, y):
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False
        return self.data[y][x] != 0

    def getAt(self, x, y):
        return self.descriptions[str(self.data[y][x])]


class Hero:
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp


class GameState:
    world = World([[]]) 
    hero = Hero(0, 0, 50)

    def getPlayerLocation():
        return world.getAt(hero.x, hero.y)

gameState = GameState()
