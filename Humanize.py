import humanize
import datetime as dt

vandaag = humanize.naturaldate(dt.date(2023, 6, 10))
nummer = humanize.apnumber(5)
afkorten_cijfer = humanize.intword(56874254125411)
#Tekst zonder toepassing Humanizing


print("Het is vandaag 18/06/2025, Shakeela heeft 56874254125411 euro op haar bankrekening staan. Je kan 5 schrijven of vijf.")

print(f"Het is vandaag",vandaag, f"Shakeela heeft", afkorten_cijfer , "op haar bankrekening staan. Je kan", nummer , "schrijven of vijf")









# print(f"Dit is 542542554121 maar dan in een meer leesbare term. Dan ziet het er zo uit", humanize.intword(542542554121))
#
#
#
#
#
# print(humanize.naturaltime(dt.datetime.now() - dt.timedelta(weeks=1)))
# dt.timedelta(seconds=1001)
# dt.timedelta()
# dt.datetime.now()
#
# humanize.intword(542542554121)
# humanize.apnumber(4)