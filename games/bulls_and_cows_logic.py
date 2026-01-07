"""
bulls_and_cows_logic.py: Sdílená herní logika pro Bulls & Cows

author: Štefan Barát
email: barat70671@mot.sps-dopravni.cz
discord: hatsukooo
"""

import random


def generate_secret_number():
    """
    Vygeneruje tajné 4-místné číslo s unikátními číslicemi.
    První číslice nesmí být 0.

    Returns:
        str: 4-místné číslo jako string
    """
    # První číslice: 1-9 (ne nula)
    first_digit = random.choice('123456789')

    # Zbývající číslice: 0-9 kromě první číslice
    remaining_digits = [d for d in '0123456789' if d != first_digit]
    other_digits = random.sample(remaining_digits, 3)

    # Spojit do jednoho čísla
    secret = first_digit + ''.join(other_digits)
    return secret


def validate_input(guess):
    """
    Validuje vstup hráče.

    Args:
        guess (str): Hráčův tip

    Returns:
        tuple: (is_valid, error_message)
               is_valid je True pokud je vstup platný, False jinak
               error_message obsahuje chybovou zprávu nebo None
    """
    # Kontrola že je vstup text
    if not isinstance(guess, str):
        return False, "Vstup musí být text!"

    # Kontrola délky
    if len(guess) != 4:
        return False, "Číslo musí mít přesně 4 číslice!"

    # Kontrola že jsou všechny znaky číslice
    if not guess.isdigit():
        return False, "Vstup musí obsahovat pouze číslice!"

    # Kontrola že nezačíná nulou
    if guess[0] == '0':
        return False, "Číslo nesmí začínat nulou!"

    # Kontrola duplicit
    if len(set(guess)) != 4:
        return False, "Číslice musí být unikátní (žádné duplicity)!"

    return True, None


def calculate_bulls_cows(secret, guess):
    """
    Vypočítá počet bulls a cows.

    Bulls = správná číslice na správné pozici
    Cows = správná číslice na špatné pozici

    Args:
        secret (str): Tajné číslo
        guess (str): Hráčův tip

    Returns:
        tuple: (bulls, cows)
    """
    bulls = 0
    cows = 0

    # Počítání bulls - správná pozice
    for i in range(4):
        if secret[i] == guess[i]:
            bulls += 1

    # Počítání cows - špatná pozice
    for i in range(4):
        if guess[i] in secret and secret[i] != guess[i]:
            cows += 1

    return bulls, cows


def format_result(bulls, cows):
    """
    Formátuje výsledek s correctnou gramatikou (jednotné/množné číslo).

    Args:
        bulls (int): Počet bulls
        cows (int): Počet cows

    Returns:
        str: Formátovaný výsledek (např. "1 bull, 2 cows")
    """
    # Formátování bulls
    if bulls == 1:
        bulls_str = "1 bull"
    else:
        bulls_str = f"{bulls} bulls"

    # Formátování cows
    if cows == 1:
        cows_str = "1 cow"
    else:
        cows_str = f"{cows} cows"

    return f"{bulls_str}, {cows_str}"


def get_performance_message(guesses):
    """
    Vrátí hodnocení výkonu na základě počtu pokusů.

    Args:
        guesses (int): Počet pokusů

    Returns:
        str: Hodnocení výkonu
    """
    if guesses <= 3:
        return "úžasné"
    elif guesses <= 6:
        return "průměrné"
    elif guesses <= 10:
        return "mohlo být lepší"
    else:
        return "příště to půjde lépe"
