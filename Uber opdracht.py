# Gegevens:
# De gebruikers kunnen kiezen uit 3 verschillende diensten met elk een eigen prijs. Zorg dat deze
# diensten in een logische collectie in je applicatie staan.
# De diensten zijn:
# "Uber Black": 2.00,
# "Uber Van": 3.50,
# "Uber X": 1.50
# Opdracht:
# Zorg dat de applicatie de volgende flow heeft:
# - De gebruiker kan kiezen uit 1 van de drie diensten
# - De gebruiker kan aangeven hoeveel kilometer gereden moet worden
# - De applicatie berekend de totale kosten
# - De gebruiker krijgt te zien hoeveel de rit gaat kosten


uber_services = {'Uber Black': 2.0, 'Uber Van': 3.5, 'Uber X': 1.5}
keuze_service = str(input('Er zijn 3 Uber services beschikbaar. Uber Black, Uber Van en Uber X. \nSchrijf de naam van de service die je wilt boeken.\n'))

keuze_km = int(input('Geef aan hoeveel kilometers je wilt met Uber wilt rijden.\n'))

#gegevens opslaan gebruikers
user_details = {"Voorkeur service": "", "Kilometers": []}

def kosten_berekening(km_price, distance):
    totaal_prijs = km_price * distance
    return(totaal_prijs)

for key,value in uber_services.items():
    if keuze_service == key:
        print(f"De kosten van de service {key} voor {keuze_km} km is intotaal", kosten_berekening(value, keuze_km),"euro.")
        user_details['Voorkeur service'] += key
        user_details['Kilometers'].append(keuze_km)
        break


    elif keuze_service not in uber_services.keys():
        print("Onjuiste invoer, typ de naam van de gewenste Uber service opnieuw")
        break


aanpas_opties = int(input("\nZou je de opgeslagen gegevens willen aanpassen? \n"
                          "Kies 1 voor: Aanpassen Uber dienst met je voorkeur \n"
                          "Kies 2 voor: Inzien van je geschiedenis\n"))



if aanpas_opties == 1:
    favoriete_service = input("Schrijf hier je favoriete Uber Service, dan slaan we je favoriet op.\n")
    user_details['Voorkeur service'] = favoriete_service
    print(user_details['Voorkeur service'])

if aanpas_opties == 2:
    print(f"Je favoriete dienst is:", {user_details['Voorkeur service']}, "\n"
    "De totale hoeveelheid gereden kilometers zijn:", user_details['Kilometers'])



#Uitproberen hoofdletter elke begin letter
# hoofdletter_keuze_service = string.capwords(keuze_service)
#
# print(hoofdletter_keuze_service)

