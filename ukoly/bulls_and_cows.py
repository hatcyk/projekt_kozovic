#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bulls & Cows - Hra na hádání čtyřciferného čísla
Autor: Štefan Barát
Email: barat70671@mot.sps-dopravni.cz
Discord: hatsukooo
"""

import random
import time


def generuj_tajne_cislo():
    """Vygeneruje náhodné 4-místné číslo s unikátními číslicemi (nezačíná 0)."""
    cislice = list(range(10))
    
    # První číslo nesmí být 0
    prvni = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
    cislice.remove(prvni)
    
    # Zbývající tři číslice
    zbytek = random.sample(cislice, 3)
    
    return str(prvni) + ''.join(map(str, zbytek))


def validuj_vstup(tip):
    """Zkontroluje, jestli je zadaný tip platný."""
    # Kontrola délky
    if len(tip) != 4:
        return False, "Zadej přesně 4 číslice!"
    
    # Kontrola, jestli jsou všechny znaky číslice
    if not tip.isdigit():
        return False, "Zadej pouze čísla!"
    
    # Kontrola, jestli nezačíná nulou
    if tip[0] == '0':
        return False, "Číslo nesmí začínat nulou!"
    
    # Kontrola duplicit
    if len(set(tip)) != 4:
        return False, "Číslo nesmí obsahovat duplicity!"
    
    return True, ""


def vyhodnot_tip(tajne_cislo, tip):
    """Vyhodnotí tip a vrátí počet bulls a cows."""
    bulls = 0
    cows = 0
    
    for i in range(4):
        if tip[i] == tajne_cislo[i]:
            bulls += 1
        elif tip[i] in tajne_cislo:
            cows += 1
    
    return bulls, cows


def formatuj_vysledek(bulls, cows):
    """Naformátuje výsledek s gramaticky správným tvarem."""
    bull_text = "bull" if bulls == 1 else "bulls"
    cow_text = "cow" if cows == 1 else "cows"
    
    return f"{bulls} {bull_text}, {cows} {cow_text}"


def hodnoceni_vysledku(pokusy):
    """Vrátí hodnocení na základě počtu pokusů."""
    if pokusy <= 4:
        return "amazing"
    elif pokusy <= 7:
        return "average"
    elif pokusy <= 10:
        return "not so good"
    else:
        return "you could do better"


def hraj_bulls_and_cows():
    """Hlavní herní smyčka."""
    print("\nHi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)
    
    tajne_cislo = generuj_tajne_cislo()
    pokusy = 0
    start_cas = time.time()
    
    while True:
        print("Enter a number:")
        print("-" * 47)
        tip = input(">>> ").strip()
        
        # Validace vstupu
        platny, chyba = validuj_vstup(tip)
        if not platny:
            print(f"✗ {chyba}")
            print("-" * 47)
            continue
        
        pokusy += 1
        
        # Vyhodnocení
        bulls, cows = vyhodnot_tip(tajne_cislo, tip)
        
        if bulls == 4:
            konec_cas = time.time()
            cas_hry = int(konec_cas - start_cas)
            
            print("Correct, you've guessed the right number")
            print(f"in {pokusy} guesses!")
            print("-" * 47)
            print(f"That's {hodnoceni_vysledku(pokusy)}!")
            print(f"Time: {cas_hry} seconds")
            print("-" * 47)
            break
        else:
            print(formatuj_vysledek(bulls, cows))
            print("-" * 47)


def main():
    """Hlavní funkce s možností opakování hry."""
    while True:
        hraj_bulls_and_cows()
        
        opakovat = input("\nChceš hrát znovu? (a/n): ").strip().lower()
        if opakovat != 'a':
            print("\nDíky za hru! 🎮")
            break


if __name__ == "__main__":
    main()
