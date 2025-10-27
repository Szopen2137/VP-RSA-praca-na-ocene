import os


def deszyfruj_RSA(liczba, d, n):
    """
    Deszyfruje liczbę algorytmem RSA: (liczba^d) mod n
    """
    return pow(liczba, d, n)


def konwertuj_liczbe_na_bajty(liczba):
    """
    Konwertuje liczbę na parę bajtów.
    """
    if liczba >= 256:
        bajt1 = liczba // 256
        bajt2 = liczba % 256
        return bytes([bajt1, bajt2])
    else:
        return bytes([liczba])


def deszyfruj_plik(plik_wejsciowy, plik_wyjsciowy, d, n):
    """
    Deszyfruje plik zaszyfrowany algorytmem RSA.
    Czyta liczby, deszyfruje je i konwertuje na bajty UTF-8.
    """
    try:
        # Wczytaj zaszyfrowane liczby
        with open(plik_wejsciowy, 'r', encoding='utf-8') as plik:
            szyfrogram = plik.read()

        zaszyfrowane_liczby = szyfrogram.split()

        if not zaszyfrowane_liczby:
            print("⚠ Ostrzeżenie: Plik jest pusty!")
            return

        print(f"Wczytano {len(zaszyfrowane_liczby)} zaszyfrowanych liczb z pliku '{plik_wejsciowy}'")

        odszyfrowane_bajty = []

        # Deszyfruj każdą liczbę
        for liczba_str in zaszyfrowane_liczby:
            try:
                liczba = int(liczba_str)

                # Deszyfruj algorytmem RSA
                odszyfrowana = deszyfruj_RSA(liczba, d, n)

                # Konwertuj na bajty
                bajty = konwertuj_liczbe_na_bajty(odszyfrowana)
                odszyfrowane_bajty.extend(bajty)

            except ValueError:
                print(f"⚠ Ostrzeżenie: Pomijam nieprawidłową wartość: {liczba_str}")
                continue

        # Konwertuj bajty na tekst UTF-8
        wynik = bytes(odszyfrowane_bajty).decode('utf-8')

        # Zapisz odszyfrowany tekst
        with open(plik_wyjsciowy, 'w', encoding='utf-8') as plik:
            plik.write(wynik)

        print(f"\n✓ Deszyfrowanie zakończone pomyślnie!")
        print(f"✓ Odszyfrowano {len(zaszyfrowane_liczby)} liczb")
        print(f"✓ Wynik zapisano do: {plik_wyjsciowy}")
        print(f"\nOdszyfrowany tekst:")
        print("-" * 60)
        print(wynik)
        print("-" * 60)

    except FileNotFoundError:
        print(f"✗ Błąd: Plik '{plik_wejsciowy}' nie został znaleziony!")
    except Exception as e:
        print(f"✗ Błąd: {e}")


# GŁÓWNY PROGRAM
if __name__ == "__main__":
    print("=" * 60)
    print("PROGRAM DESZYFRUJĄCY RSA")
    print("=" * 60)

    # Parametry klucza prywatnego RSA
    d = 43667
    n = 66013

    print(f"\nKlucz prywatny: (d={d}, n={n})")

    # Nazwy plików
    plik_wejsciowy = "tajny-szyfrogram.txt"
    plik_wyjsciowy = "tajny_odszyfrowany.txt"

    # Sprawdź czy plik istnieje
    if not os.path.exists(plik_wejsciowy):
        print(f"\n✗ Błąd: Plik '{plik_wejsciowy}' nie istnieje!")
        print("Umieść plik z szyfrogramem od nauczyciela i uruchom program ponownie.")
    else:
        print("\nRozpoczynam deszyfrowanie...")
        print("-" * 60)
        deszyfruj_plik(plik_wejsciowy, plik_wyjsciowy, d, n)
        print("=" * 60)
