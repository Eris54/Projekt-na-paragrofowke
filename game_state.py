import world_data


class World:
    def __init__(self, mapa):
        self.data = mapa
        self.width = len(self.data[0])
        self.height = len(self.data)
        self.generateLocations()

    def generateLocations(self):
        for i in range(self.height):
            for j, n in enumerate(self.data[i]):
                if not n == 0:
                    self.data[i][j] = world_data.loc_generators[n]()

    def exist(self, x, y):
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False
        return self.data[y][x] != 0

    def getAt(self, x, y):
        return self.data[y][x]


class Hero:
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp


world = World(world_data.mapp) 
hero = Hero(1, 2, 50)


def getPlayerLocation():
    return world.getAt(hero.x, hero.y)
