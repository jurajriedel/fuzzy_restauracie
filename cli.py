# cli.py
import sqlite3
from fuzzy_engine import compute_score, normalize_weights

DB = "restaurants.db"

def fetch_all():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT name, price, rating, popularity, distance, cuisine FROM restaurants")
    rows = cur.fetchall()
    conn.close()
    return [{"name": r[0], "price": r[1], "rating": r[2], "popularity": r[3], "distance": r[4], "cuisine": r[5]} for r in rows]

def input_prefs():
    print("=== Fuzzy Restaurant CLI ===")
    cuisine = input("Preferovaná kuchyňa (zostaň prázdny pre ignorovanie): ").strip()
    price_pref = input("Cena preferencia (cheap/medium/expensive) [medium]: ").strip() or "medium"
    rating_pref = input("Hodnotenie preferencia (bad/average/excellent) [excellent]: ").strip() or "excellent"
    popularity_pref = input("Popularita preferencia (unknown/known/top) [known]: ").strip() or "known"
    distance_pref = input("Vzdialenosť preferencia (close/medium/far) [close]: ").strip() or "close"

    weights = {}
    try:
        weights["price"] = float(input("Váha ceny (napr. 1-5) [1]: ") or "1")
        weights["rating"] = float(input("Váha hodnotenia [1]: ") or "1")
        weights["popularity"] = float(input("Váha popularity [1]: ") or "1")
        weights["distance"] = float(input("Váha vzdialenosti [1]: ") or "1")
        weights["cuisine"] = float(input("Váha kuchyne [1]: ") or "1")
    except:
        print("Neplatný vstup váh, použijem default 1 pre všetky.")
        weights = {k:1 for k in ["price","rating","popularity","distance","cuisine"]}

    prefs = {
        "cuisine": cuisine,
        "price_pref": price_pref,
        "rating_pref": rating_pref,
        "popularity_pref": popularity_pref,
        "distance_pref": distance_pref
    }
    weights = normalize_weights(weights)
    return prefs, weights

def main():
    prefs, weights = input_prefs()
    rows = fetch_all()
    scored = []
    for r in rows:
        sc = compute_score(r, prefs, weights)
        if sc >= 0.2:
            scored.append((r["name"], sc))
    scored.sort(key=lambda x: x[1], reverse=True)
    print("\n=== Výsledky ===")
    for name, s in scored[:50]:
        print(f"{name:30} → {s:.3f}")

if __name__ == "__main__":
    main()
