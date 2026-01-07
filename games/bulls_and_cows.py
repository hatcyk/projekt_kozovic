"""
bulls_and_cows.py: CLI implementace hry Bulls & Cows

author: Štefan Barát
email: barat70671@mot.sps-dopravni.cz
discord: hatsukooo
"""

from games.bulls_and_cows_logic import (
    generate_secret_number,
    validate_input,
    calculate_bulls_cows,
    format_result,
    get_performance_message
)
from utils.timer import start_timer, stop_timer, format_time
from utils.statistics import add_bulls_cows_result


def display_welcome():
    """Zobrazí uvítací zprávu hry."""
    print("Ahoj!")
    print("-----------------------------------------------")
    print("Vygeneroval jsem pro tebe náhodné 4-místné číslo.")
    print("Pojďme si zahrát hru Bulls & Cows.")
    print("-----------------------------------------------")




def play_bulls_and_cows():
    """Hlavní funkce pro hraní Bulls & Cows."""
    # Spustit časovač
    start_time = start_timer()

    # Zobrazit uvítací zprávu
    display_welcome()

    # Vygenerovat tajné číslo
    secret = generate_secret_number()
    # DEBUG: print(f"DEBUG: Tajné číslo je {secret}")

    # Inicializovat počítadlo pokusů
    guesses = 0

    # Herní smyčka
    while True:
        # Získat vstup od hráče
        print("Zadej číslo:")
        print("-----------------------------------------------")
        guess = input(">>> ").strip()
        guesses += 1

        # Validovat vstup
        is_valid, error = validate_input(guess)
        if not is_valid:
            print(f"Chyba: {error}")
            print("-----------------------------------------------")
            guesses -= 1  # Neplatný pokus se nepočítá
            continue

        # Vypočítat bulls a cows
        bulls, cows = calculate_bulls_cows(secret, guess)

        # Zkontrolovat výhru
        if bulls == 4:
            # Zastavit časovač
            elapsed_time = stop_timer(start_time)
            print("Správně! Uhodl jsi správné číslo")
            print(f"na {guesses} pokusů!")
            print("-----------------------------------------------")
            # Zobrazit hodnocení výkonu
            performance = get_performance_message(guesses)
            print(f"To je {performance}!")
            # Zobrazit čas
            print(f"Čas: {format_time(elapsed_time)}")
            # Uložit statistiky
            add_bulls_cows_result(guesses, elapsed_time)
            break

        # Zobrazit výsledek
        print(format_result(bulls, cows))
        print("-----------------------------------------------")
