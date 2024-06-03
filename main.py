from szyfrKolaZebatego import SzyfrKolaZebatego
import file_manager

normal_text = file_manager.read_file('./data/normal.txt')

dictionary = ['rain']

# tworzenie obiektu z parametrami
cipher = SzyfrKolaZebatego(2, dictionary, 10)
#print(f"Mozliwosci: {cipher.possible_keys}")

# kodowanie normalnego tekstu z konkretnym kluczem
cipher_text = cipher.code(normal_text, "aa")
# zapisanie zaszyfrowanego tekstu do pliku
file_manager.save_file('./data/kryptotekst.txt', cipher_text)

# wczytanie zaszyfrowanego tekstu
coded_text = file_manager.read_file('./data/kryptotekst.txt')
# proba zgadniecia szyfru
cipher.atack(coded_text)