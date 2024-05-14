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
                zaszyfrowany_tekst += litera
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
                deszyfrowany_tekst += litera
        return deszyfrowany_tekst

klucz = 'c'  # Przykładowy klucz
tekst = "To jest tekst do zaszyfrowania!"
szyfr = SzyfrKolaZebatego(klucz)
zaszyfrowany_tekst = szyfr.szyfruj(tekst)
print("Zaszyfrowany tekst:", zaszyfrowany_tekst)
deszyfrowany_tekst = szyfr.deszyfruj(zaszyfrowany_tekst)
print("Deszyfrowany tekst:", deszyfrowany_tekst)
