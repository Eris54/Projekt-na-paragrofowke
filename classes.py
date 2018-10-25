class Location:
    def __init__(self, short_desc, long_desc):
        self.short_desc = short_desc
        self.long_desc = long_desc

class World:
    data = [
        [ 1, 2, 3, 0, 0, 0 ],
        [ 0, 0, 2, 1, 1, 2 ],
        [ 0, 0, 0, 2, 0, 3 ],
        [ 0, 0, 0, 3, 2, 1 ],
        [ 0, 0, 0, 0, 0, 1 ],
        [ 0, 0, 0, 0, 0, 2 ],
    ]

    descriptions = {
        1: Location("maly pokoj", "Jestes w malym pokoju."),
        2: Location("duzy pokoj", "Jestes w duzym pokoju."),
        3: Location("pokoj", "Jestes w pokoju."),
    }

    def __init__(self):
        self.width = 6
        self.height = 6

    def exist(self, x, y):
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False
        return not self.data[y][x] == 0

    def getAt(self, x, y):
        return self.descriptions[self.data[y][x]]

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
