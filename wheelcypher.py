import random


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Wheelcypher:
    def __init__(self, wheels=None, number_wheels=6, number_gears=26):
        # ilosc kol
        self.number_wheels = number_wheels
        # ilosc zebatek lacznie z kazdego kola
        self.number_gears = number_gears

        # uzyte litery z alfabetu
        self.unused_aplhabet = list(alphabet)
        self.backup_wheels = []


        # kola
        if wheels is None:
            self.wheels = []
            self.generate_key()
        else:
            self.wheels = wheels



    def generate_key(self):
        # obliczenia dlugosci trybow dla kola
        length_wheels = [self.number_gears // self.number_wheels] * self.number_wheels
        rest = self.number_gears % self.number_wheels

        # jezeli jest reszta to dodaje aby wykorzystac wszystkie tryby
        for i in range(rest):
            length_wheels[i] += 1


        #print(length_wheels)
        # rozdzielanie liter na zbiory

        for wheel in length_wheels:
            wheel_letter = []
            for _ in range(wheel):
                """
                jezeli domyslne litery z alfabetu zostana wykorzystane
                wtedy losuj juz dowolna litere
                dzieki weryfikacji jakie litery zostaly wykorzystane
                mozemy uniknac sytuacji w ktorej majac podana liczbe
                trybow (np. 26 - czyli caly alfabet) dana litera nie wystapi
                """
                letter = ''
                if len(self.unused_aplhabet) > 0:
                    letter = random.choice(self.unused_aplhabet)
                    self.unused_aplhabet.remove(letter)
                else:
                    letter = random.choice(alphabet)

                wheel_letter.append(letter)

            # jezeli przejdziemy przez cale jedno kolo
            # to wygenerowany alfabet dla kola dodajemy do zmiennej
            self.wheels.append(wheel_letter)


        # tworzenie poczatkowej wartosci
        # TODO: sprwadzic czy mam wracac do poczatkowch wartosci czy nie
        new_list = list(self.wheels)
        self.backup_wheels = new_list

        # koniec generowania kol
        # debug/test
        #print(self.wheels)


    """
    SEKCJA SZYFROWANIE  -- START
    """
    def rotate_wheel(self, position):
        for i in range(len(self.wheels)):
            # obliczenie o ile indeksow przesunac
            # w prawo lub w lewo - zalezne od parzystosci kola
            move = len(self.wheels[i]) - position
            if i % 2 == 0:
                self.wheels[i] = self.wheels[i][-move:] + self.wheels[i][:-move]
            else:
                self.wheels[i] = self.wheels[i][move:] + self.wheels[i][:move]

        # DEBUG
        # sprawdzenie kol po przesunieciu
        #self.print_wheels()

    def encrypt_letter(self, litera):
        for number_wheel, wheel in enumerate(self.wheels):
            if litera in wheel:
                index_position_letter = wheel.index(litera)
                return f"{number_wheel + 1}{index_position_letter}"

        pass # TODO - ERROR gdy brakuje litery na wszystkich trybach

    def encrypt_text(self, text):
        encrypted_text = []
        for letter in text:
            # zakodowanie litery
            key = self.encrypt_letter(letter)
            encrypted_text.append(key)
            # ustalenie pozycji aby pozniej wiedziec o ile przesunac
            position = int(key[1:])
            # obrocenie kol
            self.rotate_wheel(position)
        return " ".join(encrypted_text)

    """
      SEKCJA SZYFROWANIE  -- KONIEC
    """

    """
      SEKCJA DESZYFROWANIE  -- START
    """

    def rotate_wheel_reverse(self, pozycja):
        for i in range(len(self.wheels)):
            move = len(self.wheels[i]) - pozycja
            if i % 2 == 0:
                self.wheels[i] = self.wheels[i][-move:] + self.wheels[i][:-move]
            else:
                self.wheels[i] = self.wheels[i][move:] + self.wheels[i][:move]

        self.print_wheels()


    def decrypt_letter(self, number_wheel, position):
        number_wheel = int(number_wheel) - 1
        position = int(position)
        return self.wheels[number_wheel][position]

    def decrypt_text(self, text):
        decrypted_text = []
        # podzielenie wszystkich kluczy
        # spacje daje nowy klucz
        key = text.split()
        for part in key:
            # numer kola
            number_wheel = part[0]
            # pozycja na kole
            position = part[1:]

            letter = self.decrypt_letter(number_wheel, position)
            decrypted_text.append(letter)
            position = int(position)

            # obrocenie kola
            self.rotate_wheel_reverse(position)
        return "".join(decrypted_text)

    def reset_to_default(self):
        self.wheels = self.backup_wheels

    """
      SEKCJA DESZYFROWANIE  -- KONIEC
    """
    def print_wheels(self):
        """
        metoda wyswietla aktualne kola/zebatki
        """
        for wheel in self.wheels:
            print(','.join([c for c in wheel]))

        print("\n\n")



wheels = [
    ['N', 'T', 'M', 'R', 'V'],
    ['W', 'Q', 'H', 'E', 'U'],
    ['O', 'J', 'L', 'Y'],
    ['F', 'I' 'Z', 'A'],
    ['G', 'S', 'B', 'X'],
    ['K', 'D', 'C', 'P']
]






wheelcypher = Wheelcypher()

wheelcypher.print_wheels()

text = "TESTT"
encrypted_text = wheelcypher.encrypt_text(text)
print(f"zaszyfrowane slowo '{text}': {encrypted_text}")


wheelcypher.reset_to_default()

wheelcypher.print_wheels()

decrypted_text = wheelcypher.decrypt_text(encrypted_text)
print(f"odszyfrowane slowo '{encrypted_text}': {decrypted_text}")

