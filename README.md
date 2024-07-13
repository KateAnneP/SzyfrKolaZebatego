Temat projektu: Szyfr Koła Zębatego wraz z atakiem metodą Hill Climbing

<u>Opis:</u> Projekt dotyczy ataku na szyfr koła zębatego. Znajdują się w nim funkcje do szyfrowania i deszyfrowania (w pliku wheelcypher) oraz funkcja do ataku metodą wspinaczkową (Hill Climbing).
Metoda wspinaczkowa opiera się na niewielkich zmianach we wcześniej wylosowanym kluczu w celu znalezienia jak najlepszego dopasowania klucza i odszyfrowania kryptotekstu.
Zmiany dokonywane są za pomocą funkcji generującej sąsiedni klucz, która losuje dwa znaki z klucza i zamienia je miejscami.

W projekcie znajdują się następujące pliki:
- main - główny plik projektu, w którym funkcje szyfrowania i ataku są wywoływane i testowane.
- spanish_main - j.w., ale dla języka hiszpańskiego
- wheelcypher - plik zawierający funkcje do szyfrowania (encrypt) i deszyfrowania(decrypt) tekstów w języku hiszpańskim, oraz wszystkie funkcje, które są używane przy tych operacjach:
  - generateGeneralKey, generateKey, - funkcje do generowania klucza losowo, oraz wprowadzając ilość kół i zębatek
  - obroc_kolo - funkcja do obrotu kołami
  - znajdz_w_kluczu - funkcja do szukania pozycji danego znaku w kluczu
  - podziel_klucz - funkcja dzieląca cały klucz na poszczególne koła
- wheelcypher_spanish - funkcje jak powyżej, ale używane przy szyfrowaniu i deszyfrowaniu tekstów w języku hiszpańskim
- attack - plik zawierający funkcje służące do ataku Hill Climbing:
  - analyze_encrypted_text - funkcja przeszukująca kryptotekst w celu odszyfrowania, ile kół i zębatek na każdym kole znajdowało się w kluczu, którym zaszyforwany był teskt
  - score_text - funkcja do oceny tekstu za pomocą ngram_score
  - generate_neighbor - funkcja generująca sąsiedni klucz w stosunku do klucza, który dostaje. Funkcja losuje dwa znaki z klucza i zamienia je miejscami
  - hill_climbing - funkcja do ataku, wykonuje zadaną ilość iteracji, porównując dwa klucze i wybierając ten, z którym tekst może zostać odszyfrowany w lepszy sposób
- spanish_attack - plik jak powyżej, ale zawierający funkcje do ataku na kryptoteksty w języku hiszpańskim
- ngram_score - plik do oceny jakości tekstu na podstawie zawartości ngramów. Zawiera funkcję score, którą należy wywołać w celu oceny tekstu
- ngram_create - plik z funkcjami do tworzenia statystyk ngramów
- file_manager - plik z funkcjami do odczytu i zapisu danych z pliku

Oraz pliki tekstowe zawierające teskty do szyfrowania w języku angielskim oraz hiszpańskim, a także pliki z kryptotekstami i bigramami dla obu języków.

W celu wykonania szyfrowania i ataku należy uruchomić plik main.py
Odpowiednie doświadczenia dla języka hiszpańskiego znajdują się w pliku spanish_main.py.

<u>Wyniki doświadczeń: </u>

<b>Język angielski:</b>
Funkcje szyfrowania i deszyfrowania działają poprawnie. 
Przy kolejnych próbach ataku na kryptotekst poprawność wahała się zwykle pomiędzy 90% a 100%. W przypadku wyższych wyników ok. 100% tekst jest możliwy do odczytania po odszyfrowaniu.
Atak Hill Climbing dobrze radzi sobie z językiem angielskim, który nie posiada żadnych znaków specjalnych
Minimalna ilość tekstu przy którym funkcje działają poprawnie (poprawnie znajdywane są ilości zębatek w kołach) to około  500 liter (bez znaków specjalnych, spacji, cyfr itp.)
Im większa będzie ilość tekstu, tym wyższa szansa na poprawne odgadnięcie ilości zębatek w kołach. 
Przy odpowiedniej ilości tekstu zwykle co 3 próba jest próbą ze 100% poprawnością odszyfrowania kryptotekstu.
Czas wykonywania 10 tyś. iteracji ataku Hill Climbing to ok. 15-20 sekund dla 500 liter w tekście. 

<b>Język hiszpański:</b>
Funkcje szyfrowania i deszyfrowania działają poprawnie w większości przypadków. 
Zdarza się w niektórych przypadkach, że niektóre znaki specjalne nie są szyfrowane we właściwy sposób (są zamieniane przez szyfr na na przykła ':' lub spację, co uniemożliwia wykonanie ataku. 
Przy kolejnych próbach ataku na kryptotekst poprawność waha się zwykle pomiędzy 90% a 100%. W przypadku wyższych wyników ok. 100% tekst jest możliwy do odczytania po odszyfrowaniu.
Jeśli atak otrzymuje kryptotekst poprawnie zaszyfrowany, to radzi sobie z nim w miarę dobrze.
Minimalna ilość tekstu przy którym funkcje działają poprawnie (poprawnie znajdywane są ilości zębatek w kołach) to około  200 liter (bez znaków specjalnych, spacji, cyfr itp.)
Im większa będzie ilość tekstu, tym wyższa szansa na poprawne odgadnięcie ilości zębatek w kołach. 
Przy odpowiedniej ilości tekstu zwykle co 5 próba jest próbą ze 100% poprawnością odszyfrowania kryptotekstu. Jest to nieco gorszy wynik niż w przypadku języka angielskiego.
Czas wykonywania 10 tyś. iteracji ataku Hill Climbing to ok. 7 sekund dla 200 znaków. 