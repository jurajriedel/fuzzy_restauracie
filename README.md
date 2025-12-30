## Je potrebne mat Python 3.12
## Spustenie projektu (Windows)
## Stiahnut subory "Kliknut na code" + "download ZIP"
## Rozbalit na plochu
## Do príkazove riadku napíšeme- cd Desktop\fuzzy_restauracie-main  
## Inštalácia potrebných knižníc___________
python -m pip install -r requirements.txt
## Vygenerovanie databázy______________
python generate_dataset.py
## Nacitanie_______________
python load_db.py
## Spustenie konzolovej verzie (CLI)________________
python cli.py
## Spustenie webu_______________
python webapp.py
## Aplikácia sa otvorí v prehliadači na adrese:
http://127.0.0.1:5000

