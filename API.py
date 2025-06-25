# API is tussenpersoon waar je een aanvraag in doet. Deze komt dan terug met zijn response.
# endpoint
#requests zoals: get, post, put, delete

# get = ophalen informatie uit backed of database
# post  = gegevens naar backend of database versturen
# put = vervangt bestaande gegevens op backend of database
# delete = verwijderen

# endpoint is specificeren waar je het verzoek maakt. URI is de bron, geen webpagina maar databron

# module installeren
"pip install requests"
import requests

#JSON is javascript object notation
# json = response.json()

# params zijn aanvullende parameters in je get verzoek.
#
# header = voor aanvullened context of instructies. Voor formaat van gegevens of een autenthicatie.
# body = onderdeel van postverzoek requests.post(url, data=data)
# data = {'key', ' value'}

# status codes
# code verstuurd vanuit server als reactie op het verzoek.
# 1xx informatief
# 2xx succesvol
# 3xx redirection
# 4xx clienterror
# 5xx server error

response.status_code om te controleren om het verzoek succesvol was,
indien niet een passende foutmelding te geven aan de gebruiker.