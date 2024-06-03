import random
import string
from itertools import product


class SzyfrKolaZebatego:
    def __init__(self, length, dictionary=None, success_length=10):
        if dictionary is None:
            dictionary = []

        self.length = length
        self.dictionary = dictionary
        self.success_length = success_length
        self.possible_keys = self.generate_key()

    # metoda sprawdza ilosc wystepowanych slow
    # w odszyfrowanym tekscie, jesli liczba przekroczy
    # podany parametr, wtedy uzna ze udalo sie
    # odszyfrowac tekst oraz rozpoznac klucz
    #
    # @return TRUE/FALSE
    # jezeli ILOSC rozpoznanych slow jest wieksza lub rowna
    # self.success_length to zwroc TRUE w przeciwnym razie FALSE
    # TODO: ? ? ? czy mozna sprawdzic kolejnosc wystepowania slow
    #  ze np. slowa ze slownika sa obok siebie np. ['THE']['WORLD']
    def is_sensible_message(self, encoded_text):
        count = 0
        for word in self.dictionary:
            if word in encoded_text:
                count += 1

        return count >= self.success_length
    def atack(self, coded_text):
        # foreach po wszystkich mozliwych kluczach
        for key in self.possible_keys:
            decoded_text = self.decode(coded_text, key)
            # TODO: zrobic opcje ze zliczaniem czestotliwosc slow/wyrazow
            #  np. zaszyfrowany tekst posiada: 100x slowo 'TAK' lub 'OKAY'
            #  wtedy bedziemy miec wieksza pewnosc ze odszyfrowany tekst
            #  jest prawidlowy
            # sprawdzenie czy rozszyfrowany tekst zawiera slowa z tablicy
            # jezeli zawiera to moze oznaczac ze jest prawidlowy klucz
            #if(any(word in decoded_text for word in self.dictionary)):
                #print(f"Próba z kluczem '{key}': {decoded_text}")

            print(f"Klucz {key} {decoded_text}")
            if self.is_sensible_message(decoded_text):
                print(f"To jest to ;) '{key}': {decoded_text}")


    # generowanie tablicy z wszystkimi mozliwymi kluczmi
    # TODO: rozwazyc opcje z generowanie najpierw jednego
    #  klucza a nastepnie sprawdzic czy jest prawidlowy
    #  i dopiero pozniej generowac kolejny
    # WARNING !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # upewnic sie czy klucz ma byc tylko z wielkich liter
    # czy moze zawierac tez male litery
    # np. abc , aBc, ABC, ABc
    # string.ascii_letters.upper()
    def generate_key(self):
        return [''.join(p) for p in product(string.ascii_letters, repeat=self.length)]

    @staticmethod
    def code(text, key):
        encrypted_text = []
        key_length = len(key)
        for i, letter in enumerate(text):
            #print(f"Litera: {letter} - index litery {i}")
            if letter.isalpha():
                # przesuniecie
                if letter.isupper():
                    shift = ord(key[i % key_length].upper()) - ord('A')
                    encrypted_letter = chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
                else:
                    shift = ord(key[i % key_length].upper()) - ord('a')
                    encrypted_letter = chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))

                # dodanie litery do tablicy
                encrypted_text.append(encrypted_letter)

            else:
                # jezeli to spacja to ignorujemy / nie dodajemy nigdzie
                continue

        return ''.join(encrypted_text)

    @staticmethod
    def decode(text, key):
        decryted_text = []
        key_length = len(key)
        for i, letter in enumerate(text):
            if letter.isalpha():
                # przesuniecie
                if letter.isupper():
                    shift = ord(key[i % key_length].upper()) - ord('A')
                    encrypted_letter = chr((ord(letter) - ord('A') - shift) % 26 + ord('A'))
                else:
                    shift = ord(key[i % key_length].upper()) - ord('a')
                    encrypted_letter = chr((ord(letter) - ord('a') - shift) % 26 + ord('a'))

                # dodanie litery do tablicy
                decryted_text.append(encrypted_letter)

            else:
                # spacja wiec ignore
                continue

        return ''.join(decryted_text)

