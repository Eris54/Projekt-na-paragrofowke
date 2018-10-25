# [Title]




# Dla użytkownika





# Dla programisty

Program wymaga wersji 3.6+ Pythona ze względu na wykorzystanie interpolacji łańcucha znaków.

Projekt podzielony jest na dwa pliki:

- `main.py` - główna pętla i logika programu.
- `classes.py` - klasy opisujące elementy świata gry.

## `classes.py`

### Klasa `Location`

Przedstawia pojedynczą **lokację** w świecie gry. Posiada krótki opis (`short_desc`) wyświetlany, gdy gracz sąsiaduje z tą lokacją, oraz długi opis (`long_desc`) wyświetlany, gdy gracz znajduje się w tej lokacji.

#### Konstruktor `__init__(self, short_desc, long_desc)`

`short_desc` to łańcuch znaków prezentujący krótki opis lokacji.
`long_desc` to łańcuch znaków prezentujący rozbudowany opis lokacji.

### Klasa `World`

Przedstawia **świat** gry złożony z lokacji.

Pole `data` przechowuje informację na temat możliwych lokacji w postaci dwuwymiarowej tablicy liczb całkowitych. Wartość `0` reprezentuje brak lokacji. Wartości większe od zera są powiązane z obiektami klasy `Location` w sposób określony przez słownik `descriptions`.

Pola `width` i `height` określają szerokość i wysokość świata gry, w tym przypadku rozmiary tablicy `data`. Program zakłada, że te wartości nie są czytane ani modyfikowane z zewnątrz klasy.

#### Koordynaty świata

Koordynaty świata odpowiadają indeksom używanym z polem `data` obiektu klasy `World`. Pozycja (`x`, `y`) w świecie odpowiada wyrażeniu `data[y][x]`. Stąd wynika, że dozwolone wartości `x` i `y` są z przedziału odpowiednio `[0, self.width)` i `[0, self.height)`. Wyróżnia się następujące kierunki:

- malejące wartości `y` - `polnoc`
- rosnące wartości `y` - `poludnie`
- malejące wartości `x` - `zachod`
- rosnące wartości `x` - `wschod`

#### Konstruktor `__init__(self)`

Inicjalizuje obiekt.

#### `exist(self, x, y)`

Zwraca wartość typu bool. Mówi, czy na pozycji (x, y) w świecie znajduje się lokacja, do której może udać się gracz. Zakres wartości x, y jest dowolny.

#### `getAt(self, x, y)`

Zwraca obiekt klasy `Location` znajdujący się na pozycji (x, y). Metoda zakłada, że taki obiekt istnieje. Jego istnienie można sprawdzić za pomocą metody `exist`.

### Klasa `Character`

Reprezentuje **gracza** poprzez jego aktualną pozycję w świecie gry. (patrz: koordynaty świata)

#### Konstruktor `__init__(self, x, y)`

`x` i `y` to liczby całkowite określające pozycję gracza.

## `main.py`

### Zmienne globalne

`world` to instancja klasy `World`.

`hero` to instancja klasy `Character`, `hero.x` oraz `hero.y` są inicjalizowane do pozycji startowej, z której gracz rozpoczyna grę.

`keys` to słownik wiążący nazwy możliwych akcji podejmowanych przez gracza z odpowiadającymi im klawiszami.

Program rozpoczyna się od następującego kawałka kodu:

```
while True:
    clearScreen()
    loop()
```

W każdej iteracji czyszczony jest ekran, a następnie wykonywana jest kolejna iteracji pętli gry `loop`.

### Funkcje

#### `clearScreen()`

Czyści ekran konsoli w zależności od systemu operacyjnego: dla Windows wywołuje komendę `cls`, dla Linuxa i innych wywołuje `clear`.

#### `loop()`

Zawiera całą interakcję z użytkownikiem.

#### `printCurrentLocation()`

Wypisuje długi opis `long_desc` lokacji, w której obecnie znajduje się gracz.

#### `printChoices()`

Wypisuje wszystkie możliwe kierunki, w jakich gracz może się w danej sytuacji poruszyć. Innymi słowy, prezentuje krótkie opisy `short_desc` lokacji sąsiadujących do tej, w której gracz się obecnie znajduje.

#### `printChoice(x, y, option_name)`

Wypisuje wybór w formacie: `{nazwa_opcji}: {krótki_opis_lokacji}`. `x`, `y` to liczby całkowite opisujące pozycję (x, y) lokacji, a `option_name` to łańcuch znaków wskazujący na jeden z kierunków świata - `"polnoc"`, `"wschod"`, `"poludnie"`, `"zachod"`. `nazwa_opcji` jest uzyskiwana dzięki wywołaniu funkcji `getFullOptionName(option_name)`.

#### `getFullOptionName(option_name)`

Zwraca łańcuch znaków postaci `[{klawisz}] {nazwa_opcji}`, gdzie `nazwa_opcji` to przekazany do tej funkcji łańcuch znaków `option_name`, a `klawisz` to klawisz odpowiadający danej opcji, pozyskiwany ze słownika `keys` (patrz: zmienne globalne).

#### `checkInput(player_choice)`

Zwraca kierunek wybrany przez gracza reprezentowany przez dwie liczby całkowite, kolejno `direction_x` (`-1` - zachód, `1` - wschód) oraz `direction_y` (`-1` - połnóc, `1` - południe) (patrz: koordynaty świata). Gracz nie może poruszać się na ukos, stąd zawsze jedna z tych zwracanych wartości jest równa 0.

Wewnętrznie funkcja ta porównuje przekazany od gracza łańuch znaków `player_choice` z definicjami klawiszy zawartymi w słowniku `keys` (patrz: zmienne globalne) i na tej podstawie określa wartości dla `direction_x` i `direction_y`.

#### `moveHero(direction_x, direction_y)`

Zmienia pozycję gracza na `next_pos_x = hero.x + direction_x` i `next_pos_y = hero.y + direction_y`, jeśli lokacja na pozycji (`next_pos_x`, `next_pos_y`) istnieje.

`direction_x` i `direction_y` to liczby całkowite określające przesunięcie gracza w świecie. (patrz: koordynaty świata)
