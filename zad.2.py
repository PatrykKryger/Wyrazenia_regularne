import re

with open('dane2.txt', 'r', encoding='utf-8') as plik:
    zawartosc = plik.read()

wzorzec = r"#\w+"
hasztagi = re.findall(wzorzec, zawartosc)

print("Wszystkie # w tekście:", hasztagi)
