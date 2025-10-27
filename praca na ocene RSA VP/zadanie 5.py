import os


def konwertuj_znaki_na_liczbe(znak1, znak2):
    """
    Konwertuje parę znaków na liczbę do zaszyfrowania.
    Łączy kody ASCII dwóch znaków w jedną liczbę.

    Args:
        znak1: Pierwszy znak
        znak2: Drugi znak (może być pusty string)

    Returns:
        Liczba utworzona z kodów ASCII znaków
    """
    kod1 = ord(znak1)

    if znak2:
        kod2 = ord(znak2)
        # Łączenie: pierwszy kod * 256 + drugi kod
        return kod1 * 256 + kod2
    else:
        # Ostatni nieparzysty znak
        return kod1


def szyfruj_RSA(liczba, e, n):
    """
    Szyfruje liczbę algorytmem RSA: (liczba^e) mod n

    Args:
        liczba: Liczba do zaszyfrowania (long long)
        e: Wykładnik klucza publicznego
        n: Moduł klucza publicznego

    Returns:
        Zaszyfrowana liczba
    """
    return pow(liczba, e, n)


def szyfruj_plik(plik_wejsciowy, plik_wyjsciowy, e, n):
    """
    Szyfruje plik tekstowy algorytmem RSA.
    Przetwarza tekst po dwa znaki, każdą parę konwertuje na liczbę i szyfruje.

    Args:
        plik_wejsciowy: Nazwa pliku do zaszyfrowania
        plik_wyjsciowy: Nazwa pliku z zaszyfrowanymi danymi
        e: Wykładnik klucza publicznego
        n: Moduł klucza publicznego
    """
    try:
        # Wczytaj tekst
        with open(plik_wejsciowy, 'r', encoding='utf-8') as plik:
            tekst = plik.read()

        if not tekst:
            print("⚠ Ostrzeżenie: Plik jest pusty!")
            return

        print(f"Wczytano {len(tekst)} znaków z pliku '{plik_wejsciowy}'")

        zaszyfrowane_liczby = []

        # Przetwarzaj tekst po dwa znaki
        for i in range(0, len(tekst), 2):
            if i + 1 < len(tekst):
                # Para znaków
                liczba = konwertuj_znaki_na_liczbe(tekst[i], tekst[i + 1])
            else:
                # Ostatni pojedynczy znak
                liczba = konwertuj_znaki_na_liczbe(tekst[i], '')

            # Szyfruj liczbę algorytmem RSA
            zaszyfrowana = szyfruj_RSA(liczba, e, n)
            zaszyfrowane_liczby.append(str(zaszyfrowana))

        # Zapisz zaszyfrowane liczby oddzielone spacjami
        with open(plik_wyjsciowy, 'w', encoding='utf-8') as plik:
            plik.write(' '.join(zaszyfrowane_liczby))

        print(f"\n✓ Szyfrowanie zakończone pomyślnie!")
        print(f"✓ Zaszyfrowano {len(zaszyfrowane_liczby)} liczb")
        print(f"✓ Wynik zapisano do: {plik_wyjsciowy}")

    except FileNotFoundError:
        print(f"✗ Błąd: Plik '{plik_wejsciowy}' nie został znaleziony!")
    except PermissionError:
        print(f"✗ Błąd: Brak uprawnień do odczytu/zapisu pliku!")
    except Exception as e:
        print(f"✗ Nieoczekiwany błąd: {e}")


# GŁÓWNY PROGRAM
if __name__ == "__main__":
    print("=" * 60)
    print("PROGRAM SZYFRUJĄCY RSA")
    print("=" * 60)

    # Parametry klucza publicznego RSA (zgodnie z zadaniem)
    e = 3  # Wykładnik
    n = 66013  # Moduł

    print(f"\nKlucz publiczny: (e={e}, n={n})")

    # Nazwy plików
    plik_wejsciowy = "tajny-tekst.txt"
    plik_wyjsciowy = "zaszyfrowany_RSA.txt"

    # Sprawdź czy plik istnieje
    if not os.path.exists(plik_wejsciowy):
        print(f"\n✗ Błąd: Plik '{plik_wejsciowy}' nie istnieje!")
        print("Umieść plik do zaszyfrowania i uruchom program ponownie.")
    else:
        # Wykonaj szyfrowanie
        print("\nRozpoczynam szyfrowanie...")
        print("-" * 60)
        szyfruj_plik(plik_wejsciowy, plik_wyjsciowy, e, n)
        print("=" * 60)
