# ==========================================
# Opdracht 4:
# De eigenaar van dierentuin 'Het Zootje' heeft een lijst met dieren en hun aantallen. De dieren en hun aantallen zijn opgeslagen in een dictionary.
# Maak onderstaande deelopdrachten.
#
# Opdracht 4a:
# De eigenaar wil de dieren op alfabetische volgorde zien. Sorteer de dieren op naam en print de dictionary uit.
# Verwachte uitkomst: {'Aap': 5, 'Giraffe': 2, 'Leeuw': 3, 'Olifant': 4, 'Zebra': 1}
#
# Opdracht 4b:
# Nu wil de eigenaar in een oogopslag wat het hoogste aantal is en het laagste. Sorteer nu de aantallen van hoog naar laag en print de dictionary uit. (De keys hoef je niet te printen)
# ==========================================

#
# dieren = {'Olifant': 5, 'Zebra': 8, 'Aap': 12, 'Giraffe': 3, 'Neushoorn': 7}
#
# sorted_dieren = (sorted(dieren.items()))
#
# print(sorted_dieren)

#optie B
# dieren = {'Olifant': 5, 'Zebra': 8, 'Aap': 12, 'Giraffe': 3, 'Neushoorn': 7}
# print(sorted(dieren.items()))

dieren = {'Olifant': 5, 'Zebra': 8, 'Aap': 12, 'Giraffe': 3, 'Neushoorn': 7}
print(sorted(dieren.values(),reverse=True))