# cli.py
import sqlite3
from fuzzy_engine import vypocitaj_skore, normalizuj_vahy

DB = "restaurants.db"

def fetch_all():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT name, price, rating, popularity, distance, cuisine FROM restaurants")
    rows = cur.fetchall()
    conn.close()
    return [
        {
            "nazov": r[0],
            "cena": r[1],
            "hodnotenie": r[2],
            "popularita": r[3],
            "vzdialenost": r[4],
            "kuchyna": r[5],
            "parkovanie": 0
        }
        for r in rows
    ]

def input_prefs():
    print("=== Fuzzy vyhľadávanie reštaurácií (CLI) ===")

    kuchyna = input("Preferovaná kuchyňa (nechaj prázdne ak nezáleží): ").strip()

    cena_pref = input("Cenová úroveň (lacna/stredna/draha) [stredna]: ").strip() or "stredna"
    hodnotenie_pref = input("Hodnotenie (zle/priemerne/vyborne) [vyborne]: ").strip() or "vyborne"
    popularita_pref = input("Popularita (neznamy/znamy/top) [znamy]: ").strip() or "znamy"
    vzdialenost_pref = input("Vzdialenosť (blizko/stredne/daleko) [blizko]: ").strip() or "blizko"

    vahy = {}
    try:
        vahy["cena"] = float(input("Dôležitosť ceny (1–5) [1]: ") or "1")
        vahy["hodnotenie"] = float(input("Dôležitosť hodnotenia [1]: ") or "1")
        vahy["popularita"] = float(input("Dôležitosť popularity [1]: ") or "1")
        vahy["vzdialenost"] = float(input("Dôležitosť vzdialenosti [1]: ") or "1")
        vahy["kuchyna"] = float(input("Dôležitosť kuchyne [1]: ") or "1")
        vahy["parkovanie"] = 0.0
    except:
        print("Neplatný vstup – nastavujem všetky váhy na 1.")
        vahy = {k: 1.0 for k in ["cena","hodnotenie","popularita","vzdialenost","kuchyna","parkovanie"]}

    preferencie = {
        "kuchyna": kuchyna,
        "cena_preferencia": cena_pref,
        "hodnotenie_preferencia": hodnotenie_pref,
        "popularita_preferencia": popularita_pref,
        "vzdialenost_preferencia": vzdialenost_pref,
    }

    vahy = normalizuj_vahy(vahy)
    return preferencie, vahy

def main():
    preferencie, vahy = input_prefs()
    zaznamy = fetch_all()
    vysledky = []

    for r in zaznamy:
        sk = vypocitaj_skore(r, preferencie, vahy)
        if sk >= 0.2:
            vysledky.append((r["nazov"], sk))

    vysledky.sort(key=lambda x: x[1], reverse=True)

    print("\n=== Výsledky ===")
    if not vysledky:
        print("Nenašli sa žiadne vhodné reštaurácie.")
    else:
        for nazov, sk in vysledky[:50]:
            print(f"{nazov:35} → {sk:.3f}")

if __name__ == "__main__":
    main()
