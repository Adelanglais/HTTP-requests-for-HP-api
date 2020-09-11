import requests
from urllib.request import urlopen
import json

print('Renseigner votre clef personnelle: ')
token = input()

dirSpells = "spells"
param={'key': token}

r = requests.get('https://www.potterapi.com/v1/'+dirSpells, params = param)

data = json.loads(r.text)
for k in data:
    print(k['spell'])

