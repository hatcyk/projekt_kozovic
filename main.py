"""
main.py: Hlavní vstupní bod pro projekt her

author: Štefan Barát
email: barat70671@mot.sps-dopravni.cz
discord: hatsukooo
"""


def display_menu():
    """Zobrazí hlavní menu."""
    print("\n" + "=" * 50)
    print("MENU - Výběr hry")
    print("=" * 50)
    print("1. Bulls & Cows")
    print("2. Tic-tac-toe")
    print("3. Zobrazit statistiky")
    print("4. Konec")
    print("=" * 50)


def choose_interface():
    """
    Umožní výběr rozhraní.

    Returns:
        str: 'a' pro CLI, 'b' pro GUI, nebo None pro zrušení
    """
    print("\nVyber rozhraní:")
    print("a) CLI (textové rozhraní)")
    print("b) GUI (grafické rozhraní)")
    choice = input("Volba (a/b): ").strip().lower()

    if choice in ['a', 'b']:
        return choice
    else:
        print("\nNeplatná volba!")
        return None


def main():
    """Hlavní funkce programu."""
    while True:
        display_menu()
        choice = input("\nZadej svou volbu (1-4): ").strip()

        if choice == "1":
            # Bulls & Cows - výběr rozhraní
            interface = choose_interface()
            if interface == 'a':
                from games.bulls_and_cows import play_bulls_and_cows
                play_bulls_and_cows()
            elif interface == 'b':
                from games.gui.bulls_and_cows_gui import play_bulls_and_cows_gui
                play_bulls_and_cows_gui()

        elif choice == "2":
            # Tic-tac-toe - výběr rozhraní
            interface = choose_interface()
            if interface == 'a':
                from games.tic_tac_toe import play_tic_tac_toe
                play_tic_tac_toe()
            elif interface == 'b':
                from games.gui.tic_tac_toe_gui import play_tic_tac_toe_gui
                play_tic_tac_toe_gui()
        elif choice == "3":
            from utils.statistics import display_statistics
            display_statistics()
        elif choice == "4":
            print("\nDěkuji za hru! Nashledanou!")
            break
        else:
            print("\nNeplatná volba! Zadej číslo 1-4.")


if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("Vítej v herním programu!")
    print("=" * 50)
    main()
