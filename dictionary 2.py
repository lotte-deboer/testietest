# ==========================================
# Opdracht 2:
# Gegeven zijn vier boodschappenlijstjes als dictionary. Je kan een if statement gebruiken en de == operator om te vergelijken.
#
# Opdracht 2a:
# Vergelijk de boodschappenlijstjes van Marie en Raj. Als de lijstjes gelijk zijn, print 'De boodschappenlijstjes zijn gelijk.'.
#
# Opdracht 2b:
# Vergelijk de boodschappenlijstjes (Marie, Raj en Jan). Als de lijstjes gelijk zijn, print 'De boodschappenlijstjes zijn gelijk.'.
# Waarom worden deze lijstjes wel/niet als gelijk beschouwd?
#
# Opdracht 2c:
# Vergelijk nu op dezelfde manier alle lijstjes. Zijn ze gelijk? Waarom wel/niet?
# ==========================================

boodschappenlijst_marie = {'Brood': 1, 'Appels': 6}
boodschappenlijst_raj = {'Brood': 1, 'Appels': 6}
boodschappenlijst_jan = {'Appels': 6, 'Brood': 1}
boodschappenlijst_karel = {'Appels': 6, 'Brood': 25}

if boodschappenlijst_marie == boodschappenlijst_raj == boodschappenlijst_jan ==boodschappenlijst_karel:
    print("De boodschappenlijstjes zijn gelijk")

else:
    print("Andere boodschappen")

    #Andere volgorde maar zelfde inhoud is nog steeds zelfde dictionary lijstje

