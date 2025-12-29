## Je potrebne mat Python 3.12

## Spustenie projektu (Windows)
## Stiahnut subory "Kliknut na code" + "download ZIP"
## Rozbalit na plochu
## V príkazovom riadku pomocou prikazu- cd Desktop\fuzzy_restauracie-main  sa dostaneme do daneho suboru
## Inštalácia potrebných knižníc
python -m pip install -r requirements.txt
## Vygenerovanie databázy
python generate_dataset.py
## Nacitanie
python load_db.py
## Spustenie konzolovej verzie (CLI)
python cli.py
## Spustenie webu
python webapp.py
## Aplikácia sa otvorí v prehliadači na adrese:
http://127.0.0.1:5000

