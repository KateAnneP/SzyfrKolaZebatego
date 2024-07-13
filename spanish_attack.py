import random
import spanish_wheelcypher as wheelcypher
import ngram_score as ns
import file_manager

ngram = ns.ngram_score("data/spanish_bigrams.txt")

###################################################################################
# Funkcja oceniająca jakość klucza
def score_text(decrypted_text):
    return ngram.score(decrypted_text)

# Funkcja generująca losowe sąsiednie klucze
def generate_neighbor(key):
    neighbor_key = list(key)
    idx1, idx2 = random.sample(range(len(key)), 2)
    neighbor_key[idx1], neighbor_key[idx2] = neighbor_key[idx2], neighbor_key[idx1]
    return ''.join(neighbor_key)

# Algorytm Hill Climbing dla szyfru
def hill_climbing(encrypted_text, randomKey, n, max_iterations=10000):
    print("Rozpoczynanie ataku Hill Climbing...")
    best_score = score_text(wheelcypher.decrypt(encrypted_text, randomKey, n))
    best_key = randomKey
    iterations_without_improvement = 0

    while iterations_without_improvement < max_iterations:
        neighbor_key = generate_neighbor(best_key)
        neighbor_score = score_text(wheelcypher.decrypt(encrypted_text, neighbor_key, n))
        if neighbor_score > best_score:
            best_score = neighbor_score
            best_key = neighbor_key
            iterations_without_improvement = 0
            #print(f"poprawa -> neighbor_score: {neighbor_score}")
        else:
            iterations_without_improvement += 1

    return best_key, best_score

def analyze_encrypted_text(encrypted_text):
    max_gear_numbers = {}

    for i in range(0, len(encrypted_text), 2):
        wheel_number = int(encrypted_text[i])
        if wheel_number == 0:
            continue

        tooth_number = int(encrypted_text[i + 1])

        if wheel_number not in max_gear_numbers:
            max_gear_numbers[wheel_number] = tooth_number
        else:
            if tooth_number > max_gear_numbers[wheel_number]:
                max_gear_numbers[wheel_number] = tooth_number

    number_of_wheels = max(max_gear_numbers.keys(), default=0)

    max_teeth_per_wheel = [0] * number_of_wheels
    for wheel_number, max_tooth in max_gear_numbers.items():
        max_teeth_per_wheel[wheel_number - 1] = max_tooth + 1

    return number_of_wheels, max_teeth_per_wheel

