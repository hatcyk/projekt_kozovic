# Projekt - Bulls & Cows a Tic-tac-toe

Školní projekt implementující dvě klasické hry v Pythonu.

## Autor

**Jméno:** Štefan Barát
**Email:** barat70671@mot.sps-dopravni.cz
**Discord:** hatsukooo

## Popis projektu

Tento projekt obsahuje implementaci dvou her s možností výběru mezi **CLI (textové)** a **GUI (grafické)** rozhraní:

### 1. Bulls & Cows
Hra na hádání tajného 4-místného čísla. Program generuje náhodné číslo s unikátními číslicemi a hráč se snaží uhodnout správné číslo. Po každém pokusu program oznámí:
- **Bulls**: počet správně uhádnutých číslic na správné pozici
- **Cows**: počet správně uhádnutých číslic na špatné pozici

### 2. Tic-tac-toe (Piškvorky)
Klasická hra pro dva hráče na herním poli 3x3. Hráči střídavě umísťují své značky (X a O) s cílem získat tři značky v řadě (horizontálně, vertikálně nebo diagonálně).

## Rozhraní

Projekt nabízí dvě možnosti hraní:
- **CLI (Command Line Interface)**: Textové rozhraní v konzoli
- **GUI (Graphical User Interface)**: Grafické rozhraní pomocí tkinter

## Struktura projektu

```
projekt_kozovic/
├── main.py                        # Hlavní vstupní bod s menu
├── games/                         # Package s hrami
│   ├── __init__.py
│   ├── bulls_and_cows.py         # CLI verze Bulls & Cows
│   ├── bulls_and_cows_logic.py   # Sdílená herní logika Bulls & Cows
│   ├── tic_tac_toe.py            # CLI verze Tic-tac-toe
│   ├── tic_tac_toe_logic.py      # Sdílená herní logika Tic-tac-toe
│   └── gui/                       # GUI implementace
│       ├── __init__.py
│       ├── bulls_and_cows_gui.py # GUI verze Bulls & Cows
│       └── tic_tac_toe_gui.py    # GUI verze Tic-tac-toe
└── utils/                         # Pomocné moduly
    ├── __init__.py
    ├── timer.py                   # Měření času
    └── statistics.py              # Sledování statistik
```

## Jak spustit

```bash
python main.py
```

Program zobrazí menu, kde můžete vybrat hru:
1. Bulls & Cows
2. Tic-tac-toe
3. Zobrazit statistiky
4. Konec

Po výběru hry (1 nebo 2) si můžete vybrat rozhraní:
- **a) CLI** - textové rozhraní v konzoli
- **b) GUI** - grafické okno pomocí tkinter

## Funkce

### Základní funkce
- ✅ Dvě plně funkční hry
- ✅ Interaktivní menu
- ✅ Validace vstupů
- ✅ Detekce výhry/prohry/remízy
- ✅ Výběr mezi CLI a GUI rozhraním

### Bonusové funkce
- ⏱️ Měření času hraní
- 📊 Sledování statistik (počet her, nejlepší výkony)
- 🎨 Grafické rozhraní (GUI) pomocí tkinter

### GUI funkce
- **Bulls & Cows GUI:**
  - Vstupní pole s validací
  - Historie pokusů
  - Real-time zobrazení času a počtu pokusů
  - Výherní dialog s možností hrát znovu

- **Tic-tac-toe GUI:**
  - 3x3 grid tlačítek
  - Barevné rozlišení hráčů (O = modrá, X = červená)
  - Real-time zobrazení času a aktuálního hráče
  - Výherní/remízový dialog s možností hrát znovu

## Požadavky

- Python 3.6+
- tkinter (součást standardní Python instalace)
- Žádné externí knihovny nejsou potřeba

## Licence

Tento projekt je vytvořen jako školní úkol.
