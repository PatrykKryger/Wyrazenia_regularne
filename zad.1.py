import re

with open('dane1.txt', 'r') as plik:
    zawartosc = plik.read()

    wzorzec_pl = r"\+48\s\d{3}\s\d{3}\s\d{3}"
    numery_pl = re.findall(wzorzec_pl, zawartosc)

    wzorzec = r"\+\d{1,2}\s\d{3}\s\d{3}\s\d{3}"
    numery = re.findall(wzorzec, zawartosc)

    print("Polskie numery telefonów w tekście:", numery_pl)
    print("Numery telefonów w tekście:", numery)
