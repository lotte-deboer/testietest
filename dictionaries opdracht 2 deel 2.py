# ==========================================
# Opdracht 2:
# De voorraad van meubelwinkel 'Op Eigen Houtje' is als volgt:
# Gegeven is de dictionary 'meubels' met daarin de keys 'banken' en 'stoelen'.
# Maak de volgende deelopdrachten. Print de uitkomst van elke opdracht om te zien of je het juiste resultaat krijgt.
#
# Opdracht 2a:
# Er worden 6 banken verkocht. Pas de waarde van de naam 'banken' aan en print de aangepaste dictionary
# Verwachte uitkomst: {'banken': 4, 'stoelen': 20}

# Opdracht 2b:
# Er komen klachten dat klanten door eerder gekochte stoelen zijn gezakt. De winkel besluit om de stoelen uit het assortiment te halen.
# Verwijder de naam 'stoelen' (en daarmee ook de bijbehorende value) uit de dictionary en print de aangepaste dictionary.
# Verwachte uitkomst: {'banken': 4}

# Opdracht 2c:
# De winkel gaat tafels verkopen en koopt er gelijk 15 in. Voeg de naam 'tafels' toe met een waarde van 15 en print de aangepaste dictionary.
# Verwachte uitkomst: {'banken': 4, 'tafels': 15}
# ==========================================
#2A
# meubels = {'banken': 10, 'stoelen': 20}
# meubels['banken'] = 4
# print(meubels)
#2B
# meubels = {'banken': 10, 'stoelen': 20}
# meubels['banken'] = 4
# del meubels['stoelen']
# print(meubels)
#2C
meubels = {'banken': 10, 'stoelen': 20}
meubels['banken'] = 4
del meubels['stoelen']
meubels['tafels'] = 15
print(meubels)