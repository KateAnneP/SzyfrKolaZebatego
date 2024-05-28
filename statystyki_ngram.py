from collections import defaultdict

#Tworzenie statystyk ngramów
def utworz_statystyki_ngramow(korpus, n):
    ngramy = defaultdict(int)
    for i in range(len(korpus) - n + 1):
        ngram = korpus[i:i+n]
        ngramy[ngram] += 1
    return ngramy

# Przykładowe użycie:
korpus = "Teeekst tekst tttekst."
bigramy = utworz_statystyki_ngramow(korpus, 2)

# Zapisanie statystyk do pliku:
with open('bigramy.txt', 'w') as f:
    for ngram, count in bigramy.items():
        f.write(f"{ngram} {count}\n")


#Odczytywanie statystyk ngramów
def wczytaj_statystyki_ngramow(plik):
    ngramy = {}
    with open(plik, 'r') as f:
        for line in f:
            ngram, count = line.split()
            ngramy[ngram] = int(count)
    return ngramy

def ocena_kryptotekstu(kryptotekst, ngramy, n):
    ocena = 0
    for i in range(len(kryptotekst) - n + 1):
        ngram = kryptotekst[i:i+n]
        if ngram in ngramy:
            ocena += ngramy[ngram]
    return ocena

# Przykładowe użycie:
bigramy = wczytaj_statystyki_ngramow('bigramy.txt')

kryptotekst = "this is a criptic text."
ocena = ocena_kryptotekstu(kryptotekst, bigramy, 2)
print("Ocena kryptotekstu:", ocena)
