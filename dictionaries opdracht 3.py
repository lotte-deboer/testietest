# ==========================================
# Opdracht 3:
# Docent Erik heeft proefwerken van studenten nagekeken en de cijfers in een dictionary opgeslagen.
# Erik komt erachter dat hij een fout heeft gemaakt en moet de cijfers met een factor 1,5 vermenigvuldigen.
# Met als enige uitzondering dat een cijfer nooit hoger mag zijn dan een 10.
# Print de uitkomst om te zien of je het juiste resultaat krijgt.

# Gegeven is de dictionary 'cijfers' met daarin de keys 'Jaap', 'Winnie', 'Jeroen' en 'Lana' en hun cijfers.
# Verwachte uitkomst: {'Jaap': 4.5, 'Winnie': 6.0, 'Jeroen': 10, 'Lana': 10}
# ==========================================

# cijfers = {'Jaap': 3, 'Winnie': 4, 'Jeroen': 9, 'Lana': 10}
# keer_factor = 1.5
# eind_cijfer = 1
# for x in cijfers:
#     eind_cijfer =  eind_cijfer*cijfers[x]*1.5
#
# print(cijfers)

cijfers = {'Jaap': 3, 'Winnie': 4, 'Jeroen': 9, 'Lana': 10}
for value in cijfers:
        cijfers[value] = cijfers.get(value) * 1.5
        if cijfers[value] > 10:
            cijfers[value] = 10
print(cijfers)
