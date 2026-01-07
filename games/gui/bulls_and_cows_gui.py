"""
bulls_and_cows_gui.py: GUI implementace hry Bulls & Cows pomocí tkinter

author: Štefan Barát
email: barat70671@mot.sps-dopravni.cz
discord: hatsukooo
"""

import tkinter as tk
from tkinter import messagebox
import time
from games.bulls_and_cows_logic import (
    generate_secret_number,
    validate_input,
    calculate_bulls_cows,
    format_result,
    get_performance_message
)
from utils.timer import start_timer, stop_timer, format_time
from utils.statistics import add_bulls_cows_result


class BullsAndCowsGUI:
    """GUI třída pro hru Bulls & Cows."""

    def __init__(self, root):
        """
        Inicializace GUI.

        Args:
            root: Hlavní tkinter okno
        """
        self.root = root
        self.root.title("Bulls & Cows")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        # Herní stav
        self.secret = None
        self.guesses = 0
        self.start_time = None
        self.game_ended = False
        self.timer_id = None

        # Vytvoření widgetů
        self.create_widgets()

        # Start hry
        self.start_game()

    def create_widgets(self):
        """Vytvoří všechny GUI komponenty."""
        # Nadpis
        title_label = tk.Label(
            self.root,
            text="Bulls & Cows",
            font=("Arial", 24, "bold"),
            pady=20
        )
        title_label.pack()

        # Frame pro informace
        info_frame = tk.Frame(self.root)
        info_frame.pack(pady=10)

        # Počítadlo pokusů
        self.guess_count_label = tk.Label(
            info_frame,
            text="Pokus: 0",
            font=("Arial", 14)
        )
        self.guess_count_label.grid(row=0, column=0, padx=20)

        # Časovač
        self.timer_label = tk.Label(
            info_frame,
            text="Čas: 0s",
            font=("Arial", 14)
        )
        self.timer_label.grid(row=0, column=1, padx=20)

        # Oddělovač
        separator1 = tk.Frame(self.root, height=2, bg="gray")
        separator1.pack(fill="x", padx=20, pady=10)

        # Instrukce
        instruction_label = tk.Label(
            self.root,
            text="Zadej 4-místné číslo (unikátní číslice, nezačíná 0):",
            font=("Arial", 12)
        )
        instruction_label.pack(pady=10)

        # Frame pro vstup
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        # Vstupní pole
        self.entry = tk.Entry(
            input_frame,
            font=("Arial", 18),
            width=10,
            justify="center"
        )
        self.entry.pack(side="left", padx=10)
        self.entry.bind("<Return>", lambda event: self.submit_guess())
        self.entry.focus()

        # Tlačítko Odeslat
        self.submit_button = tk.Button(
            input_frame,
            text="Odeslat",
            font=("Arial", 14, "bold"),
            command=self.submit_guess,
            bg="#2E7D32",
            fg="white",
            activebackground="#1B5E20",
            activeforeground="white",
            highlightbackground="#2E7D32",
            padx=20,
            pady=10,
            relief="raised",
            bd=2,
            cursor="hand2"
        )
        self.submit_button.pack(side="left", padx=10)

        # Oddělovač
        separator2 = tk.Frame(self.root, height=2, bg="gray")
        separator2.pack(fill="x", padx=20, pady=10)

        # Historie pokusů
        history_label = tk.Label(
            self.root,
            text="Historie pokusů:",
            font=("Arial", 12, "bold")
        )
        history_label.pack(pady=5)

        # Scrollable textové pole pro historii
        history_frame = tk.Frame(self.root)
        history_frame.pack(pady=10, padx=20, fill="both", expand=True)

        scrollbar = tk.Scrollbar(history_frame)
        scrollbar.pack(side="right", fill="y")

        self.history_text = tk.Text(
            history_frame,
            font=("Courier", 11),
            height=15,
            width=50,
            yscrollcommand=scrollbar.set,
            state="disabled",
            bg="#f0f0f0"
        )
        self.history_text.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=self.history_text.yview)

    def start_game(self):
        """Začne novou hru."""
        self.secret = generate_secret_number()
        self.guesses = 0
        self.start_time = start_timer()
        self.game_ended = False

        # Aktualizace UI
        self.guess_count_label.config(text="Pokus: 0")
        self.timer_label.config(text="Čas: 0s")
        self.entry.delete(0, tk.END)
        self.entry.config(state="normal")
        self.submit_button.config(state="normal")

        # Vymazat historii
        self.history_text.config(state="normal")
        self.history_text.delete(1.0, tk.END)
        self.history_text.config(state="disabled")

        # Spustit aktualizaci časovače
        self.update_timer()

        # DEBUG (odkomentuj pro testování)
        # print(f"DEBUG: Tajné číslo je {self.secret}")

    def submit_guess(self):
        """Zpracuje odhad hráče."""
        if self.game_ended:
            return

        guess = self.entry.get().strip()

        # Validace vstupu
        is_valid, error = validate_input(guess)
        if not is_valid:
            messagebox.showerror("Chyba", error)
            return

        # Zvýšit počítadlo pokusů
        self.guesses += 1
        self.guess_count_label.config(text=f"Pokus: {self.guesses}")

        # Vypočítat bulls a cows
        bulls, cows = calculate_bulls_cows(self.secret, guess)

        # Přidat do historie
        result_text = format_result(bulls, cows)
        self.add_to_history(guess, result_text)

        # Zkontrolovat výhru
        if bulls == 4:
            self.handle_win()
        else:
            # Vymazat vstupní pole pro další pokus
            self.entry.delete(0, tk.END)

    def add_to_history(self, guess, result):
        """
        Přidá pokus do historie.

        Args:
            guess (str): Hráčův tip
            result (str): Výsledek (např. "2 bulls, 1 cow")
        """
        self.history_text.config(state="normal")
        history_line = f"{self.guesses}. {guess} → {result}\n"
        self.history_text.insert(tk.END, history_line)
        self.history_text.see(tk.END)
        self.history_text.config(state="disabled")

    def handle_win(self):
        """Zpracuje výhru."""
        self.game_ended = True

        # Zastavit časovač
        elapsed_time = stop_timer(self.start_time)

        # Získat hodnocení výkonu
        performance = get_performance_message(self.guesses)

        # Uložit statistiky
        add_bulls_cows_result(self.guesses, elapsed_time)

        # Deaktivovat vstup
        self.entry.config(state="disabled")
        self.submit_button.config(state="disabled")

        # Zobrazit výherní dialog
        message = (
            f"Gratulujeme! Uhodl jsi správné číslo\n"
            f"na {self.guesses} pokusů!\n\n"
            f"To je {performance}!\n\n"
            f"Čas: {format_time(elapsed_time)}"
        )

        result = messagebox.askquestion(
            "Výhra!",
            message + "\n\nChceš hrát znovu?",
            icon='info'
        )

        if result == 'yes':
            self.start_game()
        else:
            # Zrušit časovač před zavřením
            if self.timer_id is not None:
                self.root.after_cancel(self.timer_id)
            self.root.quit()
            self.root.destroy()

    def update_timer(self):
        """Aktualizuje časovač každou sekundu."""
        if not self.game_ended:
            elapsed = time.time() - self.start_time
            self.timer_label.config(text=f"Čas: {format_time(elapsed)}")
            self.timer_id = self.root.after(1000, self.update_timer)


def play_bulls_and_cows_gui():
    """Spustí GUI verzi Bulls & Cows."""
    root = tk.Tk()
    game = BullsAndCowsGUI(root)
    root.mainloop()


if __name__ == "__main__":
    play_bulls_and_cows_gui()
