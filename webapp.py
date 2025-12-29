# webapp.py
from flask import Flask, render_template, request, jsonify
import sqlite3
from fuzzy_engine import vypocitaj_skore, normalizuj_vahy

app = Flask(__name__)
DB_SUBOR = "restaurants.db"

def nacitaj_restauracie(limit=1000):
    conn = sqlite3.connect(DB_SUBOR)
    cur = conn.cursor()
    riadky = []
    try:
        cur.execute("SELECT name, price, rating, popularity, distance, cuisine, parking FROM restaurants")
        riadky = cur.fetchall()
        conn.close()
        vysledok = []
        for r in riadky:
            vysledok.append({
                "nazov": r[0],
                "cena": r[1],
                "hodnotenie": r[2],
                "popularita": r[3],
                "vzdialenost": r[4],
                "kuchyna": r[5],
                "parkovanie": r[6],
            })
        return vysledok
    except sqlite3.OperationalError:
        # ak stlpec parking neexistuje
        cur.execute("SELECT name, price, rating, popularity, distance, cuisine FROM restaurants")
        riadky = cur.fetchall()
        conn.close()
        vysledok = []
        for r in riadky:
            vysledok.append({
                "nazov": r[0],
                "cena": r[1],
                "hodnotenie": r[2],
                "popularita": r[3],
                "vzdialenost": r[4],
                "kuchyna": r[5],
                "parkovanie": 0,
            })
        return vysledok

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/hladat", methods=["POST"])
def api_hladat():
    body = request.json or {}

    preferencie = {
        "kuchyna": body.get("kuchyna", ""),
        "cena_preferencia": body.get("cena_preferencia", "stredna"),
        "hodnotenie_preferencia": body.get("hodnotenie_preferencia", "vyborne"),
        "popularita_preferencia": body.get("popularita_preferencia", "znamy"),
        "vzdialenost_preferencia": body.get("vzdialenost_preferencia", "blizko"),
    }

    vahy = {
        "cena": float(body.get("vaha_cena", 3)),
        "hodnotenie": float(body.get("vaha_hodnotenie", 4)),
        "popularita": float(body.get("vaha_popularita", 3)),
        "vzdialenost": float(body.get("vaha_vzdialenost", 4)),
        "kuchyna": float(body.get("vaha_kuchyna", 2)),
        "parkovanie": float(body.get("vaha_parkovanie", 3)),
    }

    vahy = normalizuj_vahy(vahy)
    zaznamy = nacitaj_restauracie()
    vysledky = []

    for r in zaznamy:
        sk = vypocitaj_skore(r, preferencie, vahy)
        if sk >= 0.2:
            vysledky.append({
                "nazov": r["nazov"],
                "skore": sk,
                "cena": r["cena"],
                "hodnotenie": r["hodnotenie"],
                "popularita": r["popularita"],
                "vzdialenost": r["vzdialenost"],
                "kuchyna": r["kuchyna"],
                "parkovanie": bool(r["parkovanie"]),
            })

    vysledky.sort(key=lambda x: x["skore"], reverse=True)
    return jsonify(vysledky[:100])

if __name__ == "__main__":
    app.run(debug=True)
