import random
from ngram_score import ngram_score
import file_manager

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabet_lista = list(alfabet)
ns = ngram_score("data/english_bigrams.txt")

n = 0 #ilość kół
gears = [] #ilość zębów w każdym kole

def usun_znaki(txt):
    znaki_do_zamiany = [',', ':', '(', ')', '.', '/', '-', " "]

    wynik = ''.join(['' if char in znaki_do_zamiany else char for char in txt])
    return wynik
def usun_liczby(txt):
    wynik = ''.join([char for char in txt if not char.isdigit()])
    return wynik


def wczytanie_tekstu(file_path):
    tekst = file_manager.read_file(file_path)
    tekst = usun_liczby(tekst)
    tekst = usun_znaki(tekst)
    return tekst.upper()

normal_text = wczytanie_tekstu('./data/normal.txt')

# Ręczne wczytanie ilości kół i zębów
def inputKey():
    n = int(input("Podaj ilość kół: ")) #długość klucza, czyli ilość kół
    alph = 26 #długość alfabetu
    for i in range(0,n-1):
        if (alph > 0):
            gear_length = int(input("Podaj ilość zębów na kole nr {0}: ".format(i+1)))
            alph = alph - gear_length
            gears.append(gear_length)
    gears.append(alph)
    #print(f"Koła: {gears}")
    return n, gears

# Losowanie klucza na podstawie ilości kół i zębów
def generateKey(n, gears):
    klucz = []
    alf = alfabet_lista.copy()
    for i in range(n):
        # print(f"i: {i}, gear: {gears}")
        length = gears[i]
        for j in range(length):
            x = random.randint(0,len(alf)-1)
            letter = alf[x]
            alf.remove(letter)
            #print(f"Koło nr {i}, ząb nr {j}: {letter}")
            klucz.append(letter)
    return klucz


# Losowanie klucza przy losowej liczbie kół i zębów
def generate_random_gears(n):
    remaining_teeth = 26
    gears = []

    for _ in range(n - 1):
        min_teeth = max(3, remaining_teeth - (n - len(gears) - 1) * 9)
        max_teeth = min(9, remaining_teeth - (n - len(gears) - 1) * 3)
        gear_length = random.randint(min_teeth, max_teeth)
        gears.append(gear_length)
        remaining_teeth -= gear_length

    gears.append(remaining_teeth)
    return gears

"""
 na kolo min 3 litery
 ilosc kol tez min 3 bo jak bedzie dwa wyjdzie liczba dwucyfrowa 13 + 13
 jezeli kolo ma miec min 3 litery to 8 * 3 = 24 wiec maksymalnie moze byc 8 kol
 a tryby losowe od 3 do 9
"""
def generateGeneralKey():
    n = random.randint(3, 8)
    gears = generate_random_gears(n)

    klucz = []
    alf = alfabet_lista.copy()

    for i in range(n):
        length = gears[i]
        for j in range(length):
            x = random.randint(0, len(alf) - 1)
            letter = alf[x]
            alf.remove(letter)
            klucz.append(letter)

    return n, gears, klucz

# --- Obracanie kół ---
def obroc_kolo(indeksy, i, klucz, n):
    for j in range(n):
        dlugosc_klucza = len(klucz[j])
        if j % 2 == i % 2:
            indeksy[j] = (indeksy[j] - 1 + dlugosc_klucza) % dlugosc_klucza
        else:
            indeksy[j] = (indeksy[j] + 1 + dlugosc_klucza) % dlugosc_klucza

def znajdz_w_kluczu(pozycja, znajdz, indeksy, klucz, n):
    for i in range(n):
        dlugosc_klucza = len(klucz[i])
        for j in range(dlugosc_klucza):
            if klucz[i][(j + indeksy[i]) % dlugosc_klucza] == znajdz:
                pozycja[0] = i + 1
                pozycja[1] = j
                return True
    pozycja[0] = pozycja[1] = -1
    return False

#--- Dzielenie klucza na poszczególne koła ---
def podziel_klucz(key, gears):
    klucz = []
    idx = 0
    for length in gears:
        klucz.append(key[idx:idx + length])
        idx += length
    return klucz

# Szyfrowanie
def encrypt(txt, klucz, gears, n):

    klucz = podziel_klucz(klucz, gears)
    indeksy = [0] * n   #lista, która przechowuje aktualne indeksy używane do szyfrowania w każdym kole
    wynik = [''] * (2 * len(txt))
    pozycja = [0, 0]    #lista dwuelementowa, która służy do przechowywania pozycji znalezionego znaku w kluczu

    #print(f" K: {klucz} ")
    for i in range(len(txt)):
        if znajdz_w_kluczu(pozycja, txt[i], indeksy, klucz, n):
            wynik[2 * i] = chr(pozycja[0] + ord('0'))
            wynik[2 * i + 1] = chr(pozycja[1] + ord('0'))
            obroc_kolo(indeksy, pozycja[0], klucz, n)
        else:
            # print(f"{txt[i]}: {wynik[2]}")
            wynik[2 * i] = '0'
            wynik[2 * i + 1] = ' '

    return ''.join(wynik)

# Deszyfrowanie
def decrypt(txt, klucz, n):
    klucz = podziel_klucz(klucz, gears)
    indeksy = [0] * n  # Inicjalizacja indeksów kół
    wynik = [''] * (len(txt) // 2)  # Przygotowanie tablicy wynikowej

    #print(f"txt: {txt}")
    #print(f"klucz: {klucz}")
    #print(f"n: {klucz}")
    i = 0
    while i < len(txt):
        if txt[i] == '0':
            wynik[i // 2] = txt[i + 1]
        else:
            idx = int(txt[i]) - 1
            shift = int(txt[i + 1])
            dlugosc_klucza = len(klucz[idx])
            wynik[i // 2] = klucz[idx][(indeksy[idx] + shift + dlugosc_klucza) % dlugosc_klucza]
            obroc_kolo(indeksy, int(txt[i]), klucz, n)
        i += 2

    return ''.join(wynik)


# n, gears, klucz = generateKey()
# print(f"liczba kół: {n}")
# print(f"rozkład zębów na kołach: {gears}")
# print(f"wygenerowany klucz: {klucz}")