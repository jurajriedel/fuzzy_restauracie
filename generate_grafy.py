# generate_grafy.py
import numpy as np
import matplotlib.pyplot as plt

from fuzzy_engine import (
    cena_prislusnost,
    hodnotenie_prislusnost,
    popularita_prislusnost,
    vzdialenost_prislusnost,
)

def kresli_cena():
    x = np.linspace(0, 40, 400)
    y_lacna = [cena_prislusnost(v)["lacna"] for v in x]
    y_stredna = [cena_prislusnost(v)["stredna"] for v in x]
    y_draha = [cena_prislusnost(v)["draha"] for v in x]

    plt.figure()
    plt.plot(x, y_lacna, label="lacná")
    plt.plot(x, y_stredna, label="stredná")
    plt.plot(x, y_draha, label="drahá")
    plt.xlabel("cena [€]")
    plt.ylabel("príslušnosť")
    plt.title("Fuzzy množiny – cena")
    plt.legend()
    plt.grid(True)
    plt.savefig("graf_cena.png", dpi=200, bbox_inches="tight")

def kresli_hodnotenie():
    x = np.linspace(1, 5, 400)
    y_zle = [hodnotenie_prislusnost(v)["zle"] for v in x]
    y_priem = [hodnotenie_prislusnost(v)["priemerne"] for v in x]
    y_vyb = [hodnotenie_prislusnost(v)["vyborne"] for v in x]

    plt.figure()
    plt.plot(x, y_zle, label="zlé")
    plt.plot(x, y_priem, label="priemerné")
    plt.plot(x, y_vyb, label="výborné")
    plt.xlabel("hodnotenie [1–5]")
    plt.ylabel("príslušnosť")
    plt.title("Fuzzy množiny – hodnotenie")
    plt.legend()
    plt.grid(True)
    plt.savefig("graf_hodnotenie.png", dpi=200, bbox_inches="tight")

def kresli_popularita():
    x = np.linspace(0, 100, 400)
    y_nez = [popularita_prislusnost(v)["neznamy"] for v in x]
    y_znamy = [popularita_prislusnost(v)["znamy"] for v in x]
    y_top = [popularita_prislusnost(v)["top"] for v in x]

    plt.figure()
    plt.plot(x, y_nez, label="neznámy")
    plt.plot(x, y_znamy, label="známy")
    plt.plot(x, y_top, label="top")
    plt.xlabel("obľúbenosť [%]")
    plt.ylabel("príslušnosť")
    plt.title("Fuzzy množiny – popularita")
    plt.legend()
    plt.grid(True)
    plt.savefig("graf_popularita.png", dpi=200, bbox_inches="tight")

def kresli_vzdialenost():
    x = np.linspace(0, 10, 400)
    y_blizko = [vzdialenost_prislusnost(v)["blizko"] for v in x]
    y_stredne = [vzdialenost_prislusnost(v)["stredne"] for v in x]
    y_daleko = [vzdialenost_prislusnost(v)["daleko"] for v in x]

    plt.figure()
    plt.plot(x, y_blizko, label="blízko")
    plt.plot(x, y_stredne, label="stredne")
    plt.plot(x, y_daleko, label="ďaleko")
    plt.xlabel("vzdialenosť [km]")
    plt.ylabel("príslušnosť")
    plt.title("Fuzzy množiny – vzdialenosť")
    plt.legend()
    plt.grid(True)
    plt.savefig("graf_vzdialenost.png", dpi=200, bbox_inches="tight")

def main():
    kresli_cena()
    kresli_hodnotenie()
    kresli_popularita()
    kresli_vzdialenost()
    print("Grafy uložené ako graf_cena.png, graf_hodnotenie.png, graf_popularita.png, graf_vzdialenost.png")

if __name__ == "__main__":
    main()
