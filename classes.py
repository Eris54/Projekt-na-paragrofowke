from random import randint

class Location:
    def __init__(self, short_desc, long_desc, same_room = None):
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.same_room = same_room

class World:
    ##Opisy lokacji
    descriptions = {
        '1': Location("Małe, skromnie ozdobione drzwi prowadzące do korytarza.",
                    "Jesteś w ciasnym korytarzu, oświetlonym tylko przez wątły płomień pochodni.",
                    "Dalsza część korytarza."),
        '1_1': Location("Małe, skromnie ozdobione drzwi prowadzące do korytarza.",
                        "Aktywowałeś pułapkę!",
                        "Dalsza część korytarza."),
        '2': Location("Ogromne i ciężkie drzwi, na klamce widnieje kurz.",
                    "Sala obiadowa. Wyposażona w wiele krzeseł i dłuuugi stół. Na stole widnieją resztki jedzenia.",
                    "Dalsza część jadalni, w oddali widać taki sam podłużny stół."),
        '2_1': Location("Ogromne drzwi. Chyba ktoś już tutaj był...",
                      "Sala obiadowa. Na stole widnieją puste naczynia...\nKtoś tutaj miał zapewne niezłą ucztę.",
                      "Dalsza część jadalni."),
        '4': Location("Dziwne ciemne drzwi.",
                      "Na piedestale na środku pokoju widać mały amulet."),
        '4_1': Location("Czarne drzwi, coś strasznego kryje się w środku.",
                        "Masz przeczucie, że za niedługo może się tutaj wydarzyć coś złego."),
        '4_2': Location("W tych drzwiach jest coś co cię do nich przyciąga.",
                        "To była pułapka!\nCzarny duch który przebywał w tym pokoju, ledwo pozostawił cię przy życiu."),
        '5': Location("Drzwi na których widnieją ślady używania czarnej magii.",
                      "Prawdopodobnie, był to pokój jakiegoś czarnoksiężnika.\nWidać ślady przywoływań duchów."),
        'E': Location( "AttributeError: 'World' object has no attribute 'data[6][16]'",
                        "Hej! Czy twój pierwszy odruch, gdy widzisz Buga to wejście do niego? A co tam...\nGratulacje!\nUdało ci się wyjść z labiryntu!")
    }

    def __init__(self, mapa):
        self.data = mapa
        self.width = len(self.data[0])
        self.height = len(self.data)
        self.AddTraps(20)

    def exist(self, x, y):
        if x < 0 or x >= self.width:
            return False
        if y < 0 or y >= self.height:
            return False
        return self.data[y][x] != 0

    def getAt(self, x, y):
        return self.descriptions[str(self.data[y][x])]

    def AddTraps(self, trapNum):
        for i in range(trapNum):  ##Dodawanie losowych pułapek
            x = randint(0, self.width-1)
            y = randint(0, self.height-1)
            if str(self.data[y][x]) == '1':
                self.data[y][x] = '1_1'

    def FindEnd(self):
        counterx = 0
        countery = 0
        for i in self.data:
            for j in i:
                if j == 'E':
                    return [counterx, countery]
                counterx += 1
            countery +=1
            counterx = 0

class Character:
    def __init__(self, x, y, hp):
        self.x = x
        self.y = y
        self.hp = hp

    def IsDead(self):
        if self.hp <= 0:
            input("Twój bohater zginął.\nPrzegrałeś!")
            return 1
