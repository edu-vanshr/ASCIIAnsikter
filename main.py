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
    ram_lista = [
        ("(", ")"),
        ("[","]"),
        ("{","}"),
        ("<",">")
    ]

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

ram_alternativ = [
    ("(", ")"),
    ("[", "]"),
    ("{", "}"),
    ("<", ">")
]


def hamta_heltal(text, min_varde=None, max_varde=None):
    """
    Hämtar ett giltigt heltal från användaren
    """
    while True:
        try:
            tal = int(input(text))

            if min_varde is not None and tal < min_varde:
                print(f"Ogiltigt – ange minst {min_varde}.")
                continue

            if max_varde is not None and tal > max_varde:
                print(f"Ogiltigt – ange högst {max_varde}.")
                continue

            return tal

        except ValueError:
            print("Ogiltigt – skriv ett heltal.")


def skapa_eget_ansikte():
    """
    Låter användaren designa ett eget ansikte genom menyval.
    Skriver ut resultatet
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
    bredd = hamta_heltal("Ange bredd: ", 1)
    hojd = hamta_heltal("Ange höjd: ", 1)

    skriv_ut_slumpkluster(bredd, hojd)


# === HUVUDPROGRAM ===

def huvudprogram():
    """
    Huvudprogrammet som styr menyn och programflödet
    """

    while True:
        print("\n--- ASCII-ANSIKTEN ---")
        print("1. Skapa eget ansikte")
        print("2. Skapa kluster")
        print("3. Slumpat ansikte")
        print("4. Slumpkluster")
        print("5. Färgade ansikten")
        print("6. Spara ansikte")
        print("7. Visa sparade")
        print("8. Animation")
        print("9. Avsluta")

        val = input("Välj: ")

        if val == "1":
            skapa_eget_ansikte()

        elif val == "2":
            skapa_kluster()

        elif val == "3":
            visa_slump_ansikte()

        elif val == "4":
            visa_slumpkluster()

        elif val == "5":
            visa_fargade_ansikten()

        elif val == "6":
            ansikte = skapa_eget_ansikte()
            spara_ansikte_till_json(ansikte)
            print("Ansiktet sparades")

        elif val == "7":
            visa_sparade()

        elif val == "8":
            bredd = hamta_heltal("Bredd: ", 1)
            hojd = hamta_heltal("Höjd: ", 1)
            skriv_ut_animationskluster(bredd, hojd)

        elif val == "9":
            print("Hej då!")
            break

        else:
            print("Ogiltigt val")


# === EXTRA FUNKTIONER FÖR UTMANINGAR ===

def farglagg_ansikte(ansikte, farg):
    return farg + ansikte + Farger.RESET


def visa_fargade_ansikten():
    farger = [
        Farger.ROD,
        Farger.GRON,
        Farger.GUL,
        Farger.BLA,
        Farger.LILA,
        Farger.CYAN
    ]

    print("\n--- FÄRGADE ANSIKTEN ---")

    for _ in range(10):
        print(farglagg_ansikte(slumpa_ansikte(), random.choice(farger)))


def spara_ansikte_till_json(ansikte, fil="ansikten.json"):
    """
    Sparar ett ansikte till en JSON-fil
    """

    try:
        with open(fil, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(ansikte)

    with open(fil, "w") as f:
        json.dump(data, f, indent=4)


def visa_sparade():
    """
    Visar alla sparade ansikten
    """

    try:
        with open("ansikten.json", "r") as f:
            data = json.load(f)

            print("\n--- SPARADE ANSIKTEN ---")

            for ansikte in data:
                print(ansikte)

    except (FileNotFoundError, json.JSONDecodeError):
        print("Inga sparade ansikten")


if __name__ == "__main__":
    huvudprogram()
