import time

import spanish_wheelcypher as wheelcypher
import spanish_attack as attack
import ngram_score as ns
import file_manager


ngram = ns.ngram_score("./data/spanish_bigrams.txt")

if __name__ == "__main__":
    # Szyfrowanie w języku hiszpańskim

    n, gears, key = wheelcypher.generateGeneralKey()  # Generowanie zupełnie losowego klucza
    score = ngram.score(wheelcypher.normal_text)
    print(f"Wygenerowany klucz: {key}")
    podzielony_klucz = wheelcypher.podziel_klucz(key, gears)  # Dzielenie klucza na poszczególne koła
    print(f"\nPodzielony na koła klucz:")
    for k in podzielony_klucz:
        print(k)

    zaszyfrowany = wheelcypher.encrypt(wheelcypher.normal_text, key, gears, n)  # Szyfrowanie tekstu
    num_letters = len(wheelcypher.normal_text)
    print(f"Ilość liter w tekście: {num_letters}")
    print(f'Tekst zaszyfrowany: {zaszyfrowany} \n z kluczem: {key}')

    file_manager.save_file('./data/kryptotekst_spanish.txt',
                           zaszyfrowany)  # Zapisywanie kryptotekstu do pliku zewnętrznego

    # encrypted_text = spanish_wheelcypher.decrypt(tekst, key, n) #Deszyfrowanie w celu sprawdzenia poprawności

    ########
    # Atak
    encrypted_text = file_manager.read_file('./data/kryptotekst_spanish.txt')
    correct_score = ngram.score(wheelcypher.normal_text)

    print(f"\n\n\nAtak: \nKryptotekst pobrany z pliku: {encrypted_text}")
    wheelcypher.n, wheelcypher.gears = attack.analyze_encrypted_text(
        encrypted_text)  # Analiza kryptotekstu w celu znalezienia ilości kół oraz zębatek
    print(f"Znalezione koła = {wheelcypher.n}, zębatki = {wheelcypher.gears}")
    randKey = wheelcypher.generateKey(wheelcypher.n,
                                      wheelcypher.gears)  # Generowanie zupełnie losowego klucza na podstawie znalezionej ilości kół i zębatek
    print(f"Pierwszy losowy klucz: {randKey}")

    start_time = time.time()
    best_key, best_score = attack.hill_climbing(encrypted_text, randKey, wheelcypher.n)
    end_time = time.time()
    decrypted_text = wheelcypher.decrypt(encrypted_text, best_key,
                                         wheelcypher.n)  # Tekst odszyfrowany na podstawie znalezionego przez hill climbing najlepszego klucza
    print(f'Najlepszy klucz znaleziony przez Hill Climbing: {best_key}')
    print(f'Odszyfrowany tekst: {decrypted_text}')
    print(f'Best score: {best_score}')
    print(f'Correct score: {correct_score}')
    print(f'Poprawność: {correct_score / best_score}')
    print(f'Czas wykonywania ataku: {end_time - start_time} s')
