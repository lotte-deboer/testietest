bibliotheek = {
    "The Silent Patient":
        {
        "auteur": "Alex Michaelides",
        "genre": "Thriller",
        "publicatiejaar": 2019
    }
    ,
    "Where the Crawdads Sing": {
        "auteur": "Delia Owens",
        "genre": "Fictie",
        "publicatiejaar": 2018
    },
    "The Night Circus": {
        "auteur": "Erin Morgenstern",
        "genre": "Fantasy",
        "publicatiejaar": 2011
    },
    "Educated": {
        "auteur": "Tara Westover",
        "genre": "Memoir",
        "publicatiejaar": 2018
    },
    "Circe": {
        "auteur": "Madeline Miller",
        "genre": "Fantasy",
        "publicatiejaar": 2018
    }
}

def keuze():
    keuze_menu = int(input("Welkom in de bibliotheek. Maak gebruik van het volgende keuzemenu.\n"
                       "1: Voeg een boek toe\n"
                       "2: Ontvang lijst van alle boeken en details\n"
                       "3: Zoek per genre\n"
                       "4: Verlaat de bibliotheek\n"))
    return(keuze_menu)

keuze()
keuze_menu = keuze()
print(keuze_menu)

while keuze_menu < 10:

    if keuze_menu == 1:
    #invoer gebruiker
        add_naam = str(input("Welke naam heeft het boek?\n"))
        add_auteur= str(input("Wat is de naam van de auteur?\n"))
        add_genre= str(input("Wat voor soort genre is het?\n"))
        add_jaar= str(input("Welk jaar is het boek uitgekomen?\n"))

    #toevoegen aan dict
        bibliotheek[add_naam] = {"auteur": add_auteur, "genre": add_genre, "publicatiejaar": add_jaar}
    continue

    elif keuze_menu == 2:
        print(bibliotheek)

    elif keuze_menu == 3:
        filter_genre = str(input("Van welk genre wil je de boeken zien?\n"))
        for k,v in bibliotheek.items():
            if bibliotheek[k]["genre"] == filter_genre:
                print(f"Naam van het boek is: {k}\n"
                      f"De naam van de auteur is: {bibliotheek[k]["auteur"]}\n"
                      f"Het publicatiejaar is: {bibliotheek[k]["publicatiejaar"]}\n")

    elif keuze_menu == 4:
        break

else:
    print("Onjuiste keuze")









