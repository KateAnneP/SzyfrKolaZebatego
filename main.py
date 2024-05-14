from szyfrKolaZebatego import SzyfrKolaZebatego


klucz = 'c'  # Przykładowy klucz
tekst = "To jest tekst do zaszyfrowania!"
tekst2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer fermentum velit sed nisi congue auctor. Praesent non dui vel nisl volutpat congue ut a velit. Nullam sit amet ante condimentum, semper velit nec, interdum tortor. Cras in nulla non neque tincidunt condimentum quis at eros. Quisque fermentum rutrum nisl non suscipit. Cras eget erat volutpat quam finibus mattis vitae nec tortor. Aliquam a elit id nibh mollis pretium. Fusce id sapien ligula."

szyfr = SzyfrKolaZebatego(klucz)

zaszyfrowany_tekst = szyfr.szyfruj(tekst)
print("Zaszyfrowany tekst:", zaszyfrowany_tekst)
deszyfrowany_tekst = szyfr.deszyfruj(zaszyfrowany_tekst)
print("Deszyfrowany tekst:", deszyfrowany_tekst)

zaszyfrowany_tekst2 = szyfr.szyfruj(tekst2)
print("Zaszyfrowany tekst:", zaszyfrowany_tekst2)
deszyfrowany_tekst2 = szyfr.deszyfruj(zaszyfrowany_tekst2)
print("Deszyfrowany tekst:", deszyfrowany_tekst2)

#na losowych kluczach czy działa