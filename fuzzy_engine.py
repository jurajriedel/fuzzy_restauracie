# fuzzy_engine.py

def lichobeznik(x, a, b, c, d):
    """Lichobeznikova funkcia prislusnosti."""
    if x <= a or x >= d:
        return 0.0
    if b <= x <= c:
        return 1.0
    if a < x < b:
        return (x - a) / (b - a)
    if c < x < d:
        return (d - x) / (d - c)
    return 0.0

def trojuholnik(x, a, b, c):
    """Trojuholnikova funkcia prislusnosti."""
    if x <= a or x >= c:
        return 0.0
    if a < x < b:
        return (x - a) / (b - a)
    if b < x < c:
        return (c - x) / (c - b)
    if x == b:
        return 1.0
    return 0.0

# --- fuzzy mnoziny ---

def cena_prislusnost(cena):
    return {
        "lacna":    lichobeznik(cena, 0, 0, 6, 10),
        "stredna":  lichobeznik(cena, 8, 10, 15, 18),
        "draha":    lichobeznik(cena, 15, 20, 100, 200),
    }

def hodnotenie_prislusnost(h):
    return {
        "zle":        trojuholnik(h, 0.0, 2.0, 3.0),
        "priemerne":  trojuholnik(h, 2.5, 3.5, 4.2),
        "vyborne":    trojuholnik(h, 4.0, 4.7, 5.0),
    }

def popularita_prislusnost(p):
    return {
        "neznamy": lichobeznik(p, 0, 0, 20, 35),
        "znamy":   trojuholnik(p, 20, 50, 70),
        "top":     lichobeznik(p, 60, 75, 100, 100),
    }

def vzdialenost_prislusnost(d):
    return {
        "blizko":  trojuholnik(d, 0.0, 0.5, 1.5),
        "stredne": trojuholnik(d, 1.0, 2.5, 4.0),
        "daleko":  trojuholnik(d, 3.0, 7.0, 20.0),
    }

def zhoda_kuchyne(kuchyna_rest, kuchyna_pouz):
    if not kuchyna_pouz:
        return 0.5
    return 1.0 if kuchyna_rest.lower().strip() == kuchyna_pouz.lower().strip() else 0.0

def zhoda_parkovania(hodnota_parkovania):
    # ocakavame 1/0 alebo True/False
    return 1.0 if hodnota_parkovania in (1, True, "1") else 0.0

def normalizuj_vahy(vahy):
    s = sum(vahy.values())
    if s == 0:
        return {k: 1.0 / len(vahy) for k in vahy}
    return {k: v / s for k, v in vahy.items()}

def vypocitaj_skore(restauracia, preferencie, vahy):
    """
    restauracia: dict s klucmi nazov, cena, hodnotenie, popularita, vzdialenost, kuchyna, parkovanie
    """
    cp = cena_prislusnost(restauracia["cena"])[preferencie.get("cena_preferencia", "stredna")]
    hp = hodnotenie_prislusnost(restauracia["hodnotenie"])[preferencie.get("hodnotenie_preferencia", "vyborne")]
    pp = popularita_prislusnost(restauracia["popularita"])[preferencie.get("popularita_preferencia", "znamy")]
    dp = vzdialenost_prislusnost(restauracia["vzdialenost"])[preferencie.get("vzdialenost_preferencia", "blizko")]
    kp = zhoda_kuchyne(restauracia.get("kuchyna", ""), preferencie.get("kuchyna", ""))
    park = zhoda_parkovania(restauracia.get("parkovanie", 0))

    n_vahy = normalizuj_vahy(vahy)

    skore = (
        n_vahy["cena"] * cp +
        n_vahy["hodnotenie"] * hp +
        n_vahy["popularita"] * pp +
        n_vahy["vzdialenost"] * dp +
        n_vahy["kuchyna"] * kp +
        n_vahy["parkovanie"] * park
    )
    return round(skore, 4)
