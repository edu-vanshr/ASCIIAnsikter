"""
Projekt 4: ASCII-ansikten
Ett interaktivt program där användaren kan skapa, klustra och slumpa ASCII-ansikten.
"""

import random   # För slumpmässiga val
import json     # För att spara/ladda ansikten i JSON-fil
import time     # För animation med fördröjning


class Farger:
    """ANSI-färgkoder för terminalutskrift."""
    ROD = "\033[91m"
    GRON = "\033[92m"
    GUL = "\033[93m"
    BLA = "\033[94m"
    LILA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"   # Återställer terminalens färg


# === FUNKTIONER FÖR ANSIKTEN ===

def skapa_ansikte(ogon, mun, ram):
    """
    Skapar ett ASCII-ansikte som en sträng.
    """
    return ram[0] + ogon + mun + ogon + ram[1]  # Bygger ihop ansiktet


def slumpa_ansikte():
    """
    Skapar ett slumpmässigt ansikte.
    """

    # Lista med möjliga ögon
    ogon_lista = ["o", "-", "^", "x", "T", ">", "@"]

    # Lista med möjliga munnar
    mun_lista = ["_", "o", "^", "x", "T"]

    # Lista med möjliga ramar
    # Varje ram är en tuple med vänster och höger del
    ram_lista = [
        ("(", ")"),
        ("[","]"),
        ("{","}"),
        ("<",">")
    ]

    # Slumpar delar från listorna
    ogon = random.choice(ogon_lista)
    mun = random.choice(mun_lista)
    ram = random.choice(ram_lista)

    # Returnerar det färdiga ansiktet
    return skapa_ansikte(ogon, mun, ram)


# === FUNKTIONER FÖR KLUSTER ===

def skriv_ut_kluster(bredd, hojd, ansikte):
    """
    Skriver ut ett kluster av samma ansikte.
    """
    for rad in range(hojd):     # Loppar genom varje rad
        for kolumn in range(bredd):     # Loopar genom varje kolumn
            print(ansikte, end=" ")     # Skriver ut ansiktet på samma rad
        print()     # Byter rad efter varje färdig rad


def skriv_ut_slumpkluster(bredd, hojd):
    """
    Skriver ut ett kluster med slumpade ansikten.
    """
    for rad in range(hojd):     # Loopar genom varje rad
        for kolumn in range(bredd):     # Loopar genom varje rad
            print(slumpa_ansikte(), end=" ")    # Skriver ut ett nytt slumpat ansikte
        print()     # Byter rad efter varje färdig rad


def skriv_ut_animationskluster(bredd, hojd):
    """
    Skriver ut ett slumpat kluster med animation.
    """
    for rad in range(hojd):     # Loopar genom raderna
        for kolumn in range(bredd):     # Loopar genom kolumnerna
            print(slumpa_ansikte(), end=" ")    # Skriver ut ett slumpat ansikte
            time.sleep(0.1)     # Väntar 0.1 sekunder för aniationseffekt
        print()     # Byter rad


# === MENYFUNKTIONER ===

# Alternativ för användarens menyval
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

    # Loopar tills användaren skriver ett giltigt heltal
    while True:
        try:
            # Försöker konvertera input till heltal
            tal = int(input(text))

            # Kontrollerar minsta värde
            if min_varde is not None and tal < min_varde:
                print(f"Ogiltigt – ange minst {min_varde}.")
                continue

            # Kontrollerar största värde
            if max_varde is not None and tal > max_varde:
                print(f"Ogiltigt – ange högst {max_varde}.")
                continue

            # Returnerar talet om allt är korrekt
            return tal

        # Körs om användaren inte skrev ett heltal
        except ValueError:
            print("Ogiltigt – skriv ett heltal.")


def skapa_eget_ansikte():
    """
    Låter användaren designa ett eget ansikte genom menyval.
    Skriver ut resultatet
    """

    # === ÖGON ===

    print("\n--- VÄLJ ÖGON ---")

    # Skriver ut alla ögonalternativ
    for i, ogon in enumerate(ogon_alternativ, start=1):
        print(f"{i}. {ogon}")

    while True:
        val_ogon = hamta_heltal("Välj ögon (1-7): ")
        if 1 <= val_ogon <= 7:
            break
        print("Ogiltigt val.")

    # === MUN ===

    print("\n--- VÄLJ MUN ---")

    # Skriver ut alla munalternativ
    for i, mun in enumerate(mun_alternativ, start=1):
        print(f"{i}. {mun}")

    while True:
        val_mun = hamta_heltal("Välj mun (1-5): ")
        if 1 <= val_mun <= 5:
            break
        print("Ogiltigt val.")

    # === RAM ===

    print("\n--- VÄLJ RAM ---")

    # Skriver ut alla ramalternativ
    for i, ram in enumerate(ram_alternativ, start=1):
        print(f"{i}. {ram}")

    while True:
        val_ram = hamta_heltal("Välj ram (1-6): ")
        if 1 <= val_ram <= 6:
            break
        print("Ogiltigt val.")

    # Hämtar valda delar från listorna
    ogon = ogon_alternativ[val_ogon - 1]
    mun = mun_alternativ[val_mun - 1]
    ram = ram_alternativ[val_ram - 1]

    # Skapar ansiktet
    ansikte = skapa_ansikte(ogon, mun, ram)

    # Skriver ut resultatet
    print("\nDitt ansikte:")
    print(ansikte)

    # Returnerar ansiktet
    return ansikte


def skapa_kluster():
    """
    Låter användaren skapa ett kluster.
    """

    print("\n1. Använd slumpat ansikte")
    print("2. Skapa eget ansikte")

    val = input("Välj: ")   # Hämtar användarens val

    # Om användaren vill slumpa
    if val == "1":
        ansikte = slumpa_ansikte()
        print(f"Valt ansikte: {ansikte}")

    # Om användaren vill skapa eget
    elif val == "2":
        ansikte = skapa_eget_ansikte()

    # Om användaren skrev något ogiltigt
    else:
        print("Ogiltigt val.")
        return

    # Hämtar bredd och höjd
    bredd = hamta_heltal("Ange bredd: ")
    hojd = hamta_heltal("Ange höjd: ")

    # Skriver ut klustret
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

    # Hämtar bredd och höjd
    bredd = hamta_heltal("Ange bredd: ", 1)
    hojd = hamta_heltal("Ange höjd: ", 1)

    skriv_ut_slumpkluster(bredd, hojd)  # Skriver ut slumpklustret


# === HUVUDPROGRAM ===

def huvudprogram():
    """
    Huvudprogrammet som styr menyn och programflödet
    """

    # Programmet loopar tills användaren väljer avsluta
    while True:
        # Skriver ut huvudmenyn
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

        # Hämtar användarens menyval
        val = input("Välj: ")

        # Menyval 1
        if val == "1":
            skapa_eget_ansikte()

        # Menyval 2
        elif val == "2":
            skapa_kluster()

        # Menyval 3
        elif val == "3":
            visa_slump_ansikte()

        # Menyval 4
        elif val == "4":
            visa_slumpkluster()

        # Menyval 5
        elif val == "5":
            visa_fargade_ansikten()

        # Menyval 6
        elif val == "6":
            ansikte = skapa_eget_ansikte()
            spara_ansikte_till_json(ansikte)
            print("Ansiktet sparades")

        # Menyval 7
        elif val == "7":
            visa_sparade()

        # Menyval 8
        elif val == "8":
            bredd = hamta_heltal("Bredd: ", 1)
            hojd = hamta_heltal("Höjd: ", 1)
            skriv_ut_animationskluster(bredd, hojd)

        # Menyval 9
        elif val == "9":
            print("Hej då!")
            break

        # Om användaren skrev något ogiltigt
        else:
            print("Ogiltigt val")


# === EXTRA FUNKTIONER FÖR UTMANINGAR ===

def farglagg_ansikte(ansikte, farg):
    return farg + ansikte + Farger.RESET


def visa_fargade_ansikten():    # Lista med tillgängliga färger
    farger = [
        Farger.ROD,
        Farger.GRON,
        Farger.GUL,
        Farger.BLA,
        Farger.LILA,
        Farger.CYAN
    ]

    print("\n--- FÄRGADE ANSIKTEN ---")

    for _ in range(10):     # Loopar 10 gånger och skriver ut ett slumpmässigt ansikte med en slumpmässig färg
        print(farglagg_ansikte(slumpa_ansikte(), random.choice(farger)))


def spara_ansikte_till_json(ansikte, fil="ansikten.json"):
    """
    Sparar ett ansikte till en JSON-fil
    """

    try:    # Försöker öppn filen och läsa tidigare data
        with open(fil, "r") as f:
            data = json.load(f)
    except:     # Om filen inte finns eller är tom skapas en tom lista
        data = []

    data.append(ansikte)    # Lägger till det nya ansiktet i listan

    with open(fil, "w") as f:   # Skriver tillbaka hela listan i filen
        json.dump(data, f, indent=4)


def visa_sparade():
    """
    Visar alla sparade ansikten
    """

    try:    # Öppnar JSON-filen och läser innehållet
        with open("ansikten.json", "r") as f:
            data = json.load(f)

            print("\n--- SPARADE ANSIKTEN ---")

            for ansikte in data:
                print(ansikte)  # Skriver ut alla sparade ansikten

    except (FileNotFoundError, json.JSONDecodeError):
        print("Inga sparade ansikten")  # Körs om filen saknas eller är trasig


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()
