import requests
import json
from pprint import pprint

ts = 1
private_key = "bb2b97bb1b66b2435284485c9542c91302924ab1"
public_key = "1ac3877559dd79f0d78144270b96f9b8"
hash = "1a7e6112569305e792e3f360b4efe947"

url = f"http://gateway.marvel.com/v1/public/characters?ts={ts}&apikey={public_key}&hash={hash}"

response = requests.get(url)

if response.status_code == 200:
    datos = response.json()
    personajes = datos["data"]["results"]

contenedor = []

for personaje in personajes:
    name = personaje["name"]
    thumbnail = (
        personaje["thumbnail"]["path"] + "." + personaje["thumbnail"]["extension"]
    )
    comics = personaje["comics"]["available"]
    series = personaje["series"]["available"]
    character = {
        "name": name,
        "comics": comics,
        "series": series,
        "thumbnail": thumbnail,
    }
    contenedor.append(character)

for personaje in contenedor:
    print(
        f'El personaje {personaje["name"]} tiene {personaje["comics"]} comics y {personaje["series"]} series y el thumbnail es {personaje["thumbnail"]}'
    )
