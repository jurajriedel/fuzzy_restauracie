import pandas as pd
import random

# Nastavíme seed, aby sa pri každom spustení vygeneroval rovnaký dataset
random.seed(42)

MESTA = [
    "Bratislava", "Košice", "Prešov", "Žilina", "Banská Bystrica",
    "Nitra", "Trnava", "Trenčín", "Martin", "Poprad",
    "Prievidza", "Zvolen", "Považská Bystrica", "Nové Zámky",
    "Spišská Nová Ves", "Komárno", "Levice", "Michalovce",
    "Piešťany", "Ružomberok",
]

TYPY = [
    "Reštaurácia", "Bistro", "Koliba", "Piváreň", "Hostinec",
    "Pizzeria", "Steak house", "Pub", "Čajovňa", "Kaviareň"
]

PRIDAVNE = [
    "Zlatá", "Strieborná", "Modrá", "Zelená", "Červená", "Divoká",
    "Starý", "Nová", "Tichá", "Veselá", "Uličná", "Mestská",
    "Podhradská", "Lesná", "Slnečná"
]

PODSTATNE = [
    "Líška", "Sova", "Vrana", "Kačka", "Koza", "Ovca",
    "Studňa", "Skala", "Ruža", "Lipa", "Borovica",
    "Dolina", "Rieka", "Mlyn", "Háj", "Vrch", "Lúka"
]

KUCHYNE = [
    "slovenska", "talianska", "burger", "veganska", "indicka",
    "medzinarodna", "pivaren", "kaviaren", "polievkaren",
    "stredomorska", "steakhouse", "fine_dining"
]

def vygeneruj_nazov(pouzite_nazvy):
    """Vygeneruje jeden unikátny názov reštaurácie."""
    while True:
        mesto = random.choice(MESTA)
        typ = random.choice(TYPY)
        prid = random.choice(PRIDAVNE)
        pod = random.choice(PODSTATNE)

        nazov = f"{typ} {prid} {pod} ({mesto})"

        if nazov not in pouzite_nazvy:
            pouzite_nazvy.add(nazov)
            return nazov

def vygeneruj_dataset(pocet=200):
    zaznamy = []
    pouzite_nazvy = set()

    for _ in range(pocet):
        nazov = vygeneruj_nazov(pouzite_nazvy)
        kuchyna = random.choice(KUCHYNE)

        # Cena podľa typu kuchyne
        if kuchyna in ("fine_dining", "steakhouse"):
            cena = random.uniform(18, 35)
        elif kuchyna in ("burger", "talianska", "stredomorska"):
            cena = random.uniform(10, 20)
        elif kuchyna in ("kaviaren", "polievkaren"):
            cena = random.uniform(5, 12)
        else:
            cena = random.uniform(8, 18)

        hodnotenie = random.uniform(3.0, 5.0)       # rating 3.0–5.0
        popularita = random.uniform(20, 100)        # 20–100 %
        vzdialenost = random.uniform(0.2, 15.0)     # 0.2–15 km
        parkovanie = 1 if random.random() < 0.6 else 0  # cca 60 % áno

        zaznamy.append({
            "name": nazov,
            "price": round(cena, 2),
            "rating": round(hodnotenie, 2),
            "popularity": round(popularita, 1),
            "distance": round(vzdialenost, 2),
            "cuisine": kuchyna,
            "parking": parkovanie,
        })

    df = pd.DataFrame(zaznamy)
    df.to_csv("restaurants_sample.csv", index=False)
    print(f"Vygenerované restaurants_sample.csv s {len(df)} záznamami (200 unikátnych, stabilných reštaurácií).")

if __name__ == "__main__":
    vygeneruj_dataset(200)
