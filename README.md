# Projekt - Bulls & Cows a Tic-tac-toe

Školní projekt implementující dvě klasické hry v Pythonu.

## Autor

**Jméno:** Štefan Barát
**Email:** barat70671@mot.sps-dopravni.cz
**Discord:** hatsukooo

## Popis projektu

Tento projekt obsahuje implementaci dvou her:

### 1. Bulls & Cows
Hra na hádání tajného 4-místného čísla. Program generuje náhodné číslo s unikátními číslicemi a hráč se snaží uhodnout správné číslo. Po každém pokusu program oznámí:
- **Bulls**: počet správně uhádnutých číslic na správné pozici
- **Cows**: počet správně uhádnutých číslic na špatné pozici

### 2. Tic-tac-toe (Piškvorky)
Klasická hra pro dva hráče na herním poli 3x3. Hráči střídavě umísťují své značky (X a O) s cílem získat tři značky v řadě (horizontálně, vertikálně nebo diagonálně).

## Struktura projektu

```
projekt_kozovic/
├── main.py              # Hlavní vstupní bod s menu
├── games/               # Package s hrami
│   ├── __init__.py
│   ├── bulls_and_cows.py
│   └── tic_tac_toe.py
└── utils/               # Pomocné moduly
    ├── __init__.py
    ├── timer.py         # Měření času
    └── statistics.py    # Sledování statistik
```

## Jak spustit

```bash
python main.py
```

Program zobrazí menu, kde můžete vybrat hru:
1. Bulls & Cows
2. Tic-tac-toe
3. Konec

## Funkce

### Základní funkce
- ✅ Dvě plně funkční hry
- ✅ Interaktivní menu
- ✅ Validace vstupů
- ✅ Detekce výhry/prohry/remízy

### Bonusové funkce
- ⏱️ Měření času hraní
- 📊 Sledování statistik (počet her, nejlepší výkony)

## Požadavky

- Python 3.6+
- Žádné externí knihovny nejsou potřeba

## Licence

Tento projekt je vytvořen jako školní úkol.
