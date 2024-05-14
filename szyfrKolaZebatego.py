#Szyfrowanie szyfrem koła zębatego

class SzyfrKolaZebatego:
    def __init__(self, klucz):
        self.klucz = klucz

    def szyfruj(self, tekst):
        zaszyfrowany_tekst = ""
        for litera in tekst:
            if litera.isalpha():
                offset = ord(self.klucz) - ord('a')  # Przesunięcie
                zaszyfrowana_litera = chr((ord(litera.lower()) - ord('a') + offset) % 26 + ord('a'))
                if litera.isupper():
                    zaszyfrowany_tekst += zaszyfrowana_litera.upper()
                else:
                    zaszyfrowany_tekst += zaszyfrowana_litera
            else:
                continue  # Pomijamy spacje
        return zaszyfrowany_tekst

    def deszyfruj(self, zaszyfrowany_tekst):
        deszyfrowany_tekst = ""
        for litera in zaszyfrowany_tekst:
            if litera.isalpha():
                offset = ord(self.klucz) - ord('a')  # Przesunięcie
                deszyfrowana_litera = chr((ord(litera.lower()) - ord('a') - offset) % 26 + ord('a'))
                if litera.isupper():
                    deszyfrowany_tekst += deszyfrowana_litera.upper()
                else:
                    deszyfrowany_tekst += deszyfrowana_litera
            else:
                continue  # Pomijamy spacje
        return deszyfrowany_tekst


