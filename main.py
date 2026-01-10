def display_menu():
    # Zobrazí hlavní menu.
    print("\n" + "=" * 50)
    print("Vítejte v motolské sbírce projektů!")
    print("=" * 50)
    print("1. Bulls & Cows")
    print("2. Tic-tac-toe")
    print("3. Zobrazit statistiky")
    print("4. Konec")
    print("=" * 50)

def main():
    # Hlavní funkce programu.
    while True:
        display_menu()
        choice = input("\nZadej svou volbu (1-4): ").strip()

        if choice == "1":
            print("\nSpouštím... ", choice)
            break
        elif choice == "2":
            print("\nSpouštím... ", choice)
            break
        elif choice == "3":
            print("\nSpouštím... ", choice)
            break
        else:
            print("\nNeplatná volba! Zadej číslo 1-4.")


if __name__ == "__main__":
    main()
