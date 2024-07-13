import re
from collections import defaultdict

#Tworzenie statystyk ngramów
def utworz_statystyki_ngramow(korpus, n):
    ngramy = defaultdict(int)
    for i in range(len(korpus) - n + 1):
        ngram = korpus[i:i+n]
        ngramy[ngram] += 1
    return ngramy


with open("data/book_spanish/spanish.txt", "r", encoding="utf-8") as file:
    text = file.read().upper()

text = re.sub(r'[^A-ZÁÉÍÓÚÑÜ ]', '', text)
bigramy = utworz_statystyki_ngramow(text, 2)

# # Zapisanie statystyk do pliku
# with open('data/spanish_bigrams.txt', 'w', encoding="utf-8") as f:
#     for ngram, count in bigramy.items():
#         f.write(f"{ngram} {count}\n")
