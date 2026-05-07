"""
Projekt 4: ASCII-ansikten
Ett interaktivt program där användaren kan skapa, klustra och slumpa ASCII-ansikten.
"""

import random
import json
import time


class Farger:
    """ANSI-färgkoder för terminalutskrift."""
    ROD = "\033[91m"
    GRON = "\033[92m"
    GUL = "\033[93m"
    BLA = "\033[94m"
    LILA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"


# === FUNKTIONER FÖR ANSIKTEN ===

def skapa_ansikte(ogon, mun, ram):
    """
    Skapar ett ASCII-ansikte som en sträng.
    """
    return ram[0] + ogon + mun + ogon + ram[1]


def slumpa_ansikte():
    """
    Skapar ett slumpmässigt ansikte.
    """
    ogon_lista = ["o", "-", "^", "x", "T", ">", "@"]
    mun_lista = ["_", "o", "^", "x", "T"]
    ram_lista = ["()", "[]", "{}", "<>", "()]", "[)"]

    ogon = random.choice(ogon_lista)
    mun = random.choice(mun_lista)
    ram = random.choice(ram_lista)

    return skapa_ansikte(ogon, mun, ram)


# === FUNKTIONER FÖR KLUSTER ===

def skriv_ut_kluster(bredd, hojd, ansikte):
    """
    Skriver ut ett kluster av samma ansikte.
    """
    for rad in range(hojd):
        for kolumn in range(bredd):
            print(ansikte, end=" ")
        print()


def skriv_ut_slumpkluster(bredd, hojd):
    """
    Skriver ut ett kluster med slumpade ansikten.
    """
    for rad in range(hojd):
        for kolumn in range(bredd):
            print(slumpa_ansikte(), end=" ")
        print()


def skriv_ut_animationskluster(bredd, hojd):
    """
    Skriver ut ett slumpat kluster med animation.
    """
    for rad in range(hojd):
        for kolumn in range(bredd):
            print(slumpa_ansikte(), end=" ")
            time.sleep(0.1)
        print()


# === MENYFUNKTIONER ===

ogon_alternativ = ["o", "-", "^", "x", "T", ">", "@"]
mun_alternativ = ["_", "o", "^", "x", "T"]
ram_alternativ = ["()", "[]", "{}", "<>", "()]", "[)"]


def hamta_heltal(text):
    """
    Säker input för heltal.
    """
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Ogiltig input, skriv ett heltal.")


def skapa_eget_ansikte():
    """
    Låter användaren designa ett eget ansikte.
    """
    print("\n--- VÄLJ ÖGON ---")
    for i, ogon in enumerate(ogon_alternativ, start=1):
        print(f"{i}. {ogon}")

    while True:
        val_ogon = hamta_heltal("Välj ögon (1-7): ")
        if 1 <= val_ogon <= 7:
            break
        print("Ogiltigt val.")

    print("\n--- VÄLJ MUN ---")
    for i, mun in enumerate(mun_alternativ, start=1):
        print(f"{i}. {mun}")

    while True:
        val_mun = hamta_heltal("Välj mun (1-5): ")
        if 1 <= val_mun <= 5:
            break
        print("Ogiltigt val.")

    print("\n--- VÄLJ RAM ---")
    for i, ram in enumerate(ram_alternativ, start=1):
        print(f"{i}. {ram}")

    while True:
        val_ram = hamta_heltal("Välj ram (1-6): ")
        if 1 <= val_ram <= 6:
            break
        print("Ogiltigt val.")

    ogon = ogon_alternativ[val_ogon - 1]
    mun = mun_alternativ[val_mun - 1]
    ram = ram_alternativ[val_ram - 1]

    ansikte = skapa_ansikte(ogon, mun, ram)

    print("\nDitt ansikte:")
    print(ansikte)

    return ansikte


def skapa_kluster():
    """
    Låter användaren skapa ett kluster.
    """
    print("\n1. Använd slumpat ansikte")
    print("2. Skapa eget ansikte")

    val = input("Välj: ")

    if val == "1":
        ansikte = slumpa_ansikte()
        print(f"Valt ansikte: {ansikte}")

    elif val == "2":
        ansikte = skapa_eget_ansikte()

    else:
        print("Ogiltigt val.")
        return

    bredd = hamta_heltal("Ange bredd: ")
    hojd = hamta_heltal("Ange höjd: ")

    skriv_ut_kluster(bredd, hojd, ansikte)


def visa_slump_ansikte():
    """
    Visar ett slumpmässigt ansikte.
    """
    print("\nSlumpat ansikte:")
    print(slumpa_ansikte())


def visa_slumpkluster():
    """
    Visar ett kluster med slumpade ansikten.
    """
    bredd = hamta_heltal("Ange bredd: ")
    hojd = hamta_heltal("Ange höjd: ")

    skriv_ut_slumpkluster(bredd, hojd)

