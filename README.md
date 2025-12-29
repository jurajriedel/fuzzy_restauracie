## Vložit príkazy do konzoly po jednom a stalčit enter
## Spustenie projektu (Windows)
git clone https://github.com/jurajriedel/fuzzy_restauracie.git
cd fuzzy_restauracie
## Inštalácia potrebných knižníc
pip install -r requirements.txt
## Vygenerovanie dát a databázy
python generate_dataset.py
python load_db.py
## Spustenie konzolovej verzie (CLI)
python cli.py
## Spustenie webu
python webapp.py
## Aplikácia sa otvorí v prehliadači na adrese:
http://127.0.0.1:5000

