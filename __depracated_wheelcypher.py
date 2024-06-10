# """
# LOSUJE ROZNE WIELKOSCI ZEBATEK DLA KOL
# """
# def generate_key(self):
#     # tworzenie pustych kol
#     self.wheels = list(range(1, self.number_gears + 1))
#     length_wheels = [random.randint(1, max(1, self.number_gears // self.number_wheels)) for _ in range(self.number_wheels - 1)]
#     sum_length = sum(length_wheels)
#
#     # dodanie reszty do ostatniego zbioru
#     if sum_length < self.number_gears:
#         length_wheels.append(self.number_gears - sum_length)
#     else:
#         # jezeli suma dlugosc przekracza dlugosc zebatek
#         # to redukujemy ostatnie kolo aby dlugosc zebatek sie zgadzala
#         over_size = sum_length - self.number_gears
#         for i in range(over_size):
#             length_wheels[i % len(length_wheels)] -= 1
#         length_wheels.append(0)
#
#     print(length_wheels)
#     # rozdzielanie liter na zbiory
#     for i in range(self.number_gears):
#         """
#         jezeli domyslne litery z alfabetu zostana wykorzystane
#         wtedy losuj juz dowolna litere
#         dzieki weryfikacji jakie litery zostaly wykorzystane
#         mozemy uniknac sytuacji w ktorej majac podana liczbe
#         trybow (np. 26 - czyli caly alfabet) dana litera nie wystapi
#         """
#         if len(self.unused_aplhabet) > 0:
#             letter = random.choice(self.unused_aplhabet)
#             self.unused_aplhabet.remove(letter)
#             #print(f" {self.unused_aplhabet}")
#         else:
#             letter = random.choice(alphabet)
#
#         #print(f"i: {i}, letter: {letter}")
#         self.wheels[i % self.number_wheels].append(letter)