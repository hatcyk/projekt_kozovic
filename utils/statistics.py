"""
statistics.py: Modul pro sledování statistik her

author: Štefan Barát
email: barat70671@mot.sps-dopravni.cz
discord: hatsukooo
"""

import json
import os


STATS_FILE = os.path.join(os.path.dirname(__file__), 'game_stats.json')


def load_statistics():
    """
    Načte statistiky ze souboru.

    Returns:
        dict: Slovník se statistikami her
    """
    if not os.path.exists(STATS_FILE):
        return {
            'bulls_and_cows': {
                'total_games': 0,
                'total_guesses': 0,
                'best_guesses': None,
                'total_time': 0
            },
            'tic_tac_toe': {
                'total_games': 0,
                'player_o_wins': 0,
                'player_x_wins': 0,
                'draws': 0,
                'total_time': 0
            }
        }

    try:
        with open(STATS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return load_statistics.__defaults__[0]


def save_statistics(stats):
    """
    Uloží statistiky do souboru.

    Args:
        stats (dict): Slovník se statistikami
    """
    try:
        with open(STATS_FILE, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Chyba při ukládání statistik: {e}")


def add_bulls_cows_result(guesses, time_seconds):
    """
    Přidá výsledek hry Bulls & Cows.

    Args:
        guesses (int): Počet pokusů
        time_seconds (float): Čas v sekundách
    """
    stats = load_statistics()

    stats['bulls_and_cows']['total_games'] += 1
    stats['bulls_and_cows']['total_guesses'] += guesses
    stats['bulls_and_cows']['total_time'] += time_seconds

    # Aktualizovat nejlepší výkon
    if (stats['bulls_and_cows']['best_guesses'] is None or
            guesses < stats['bulls_and_cows']['best_guesses']):
        stats['bulls_and_cows']['best_guesses'] = guesses

    save_statistics(stats)


def add_tic_tac_toe_result(winner, time_seconds):
    """
    Přidá výsledek hry Tic-tac-toe.

    Args:
        winner (str): 'X', 'O', nebo 'draw'
        time_seconds (float): Čas v sekundách
    """
    stats = load_statistics()

    stats['tic_tac_toe']['total_games'] += 1
    stats['tic_tac_toe']['total_time'] += time_seconds

    if winner == 'O':
        stats['tic_tac_toe']['player_o_wins'] += 1
    elif winner == 'X':
        stats['tic_tac_toe']['player_x_wins'] += 1
    else:
        stats['tic_tac_toe']['draws'] += 1

    save_statistics(stats)


def display_statistics():
    """Zobrazí statistiky her."""
    stats = load_statistics()

    print("\n" + "=" * 50)
    print("STATISTIKY HER")
    print("=" * 50)

    # Bulls & Cows statistiky
    bc_stats = stats['bulls_and_cows']
    print("\nBulls & Cows:")
    print(f"  Celkem her: {bc_stats['total_games']}")

    if bc_stats['total_games'] > 0:
        avg_guesses = bc_stats['total_guesses'] / bc_stats['total_games']
        print(f"  Průměrný počet pokusů: {avg_guesses:.1f}")
        print(f"  Nejlepší výkon: {bc_stats['best_guesses']} pokusů")
        avg_time = bc_stats['total_time'] / bc_stats['total_games']
        print(f"  Průměrný čas: {avg_time:.1f}s")

    # Tic-tac-toe statistiky
    ttt_stats = stats['tic_tac_toe']
    print("\nTic-tac-toe:")
    print(f"  Celkem her: {ttt_stats['total_games']}")

    if ttt_stats['total_games'] > 0:
        print(f"  Výhry hráče O: {ttt_stats['player_o_wins']}")
        print(f"  Výhry hráče X: {ttt_stats['player_x_wins']}")
        print(f"  Remízy: {ttt_stats['draws']}")
        avg_time = ttt_stats['total_time'] / ttt_stats['total_games']
        print(f"  Průměrný čas: {avg_time:.1f}s")

    print("=" * 50)
