import requests
import json

ts = 1
private_key = "bb2b97bb1b66b2435284485c9542c91302924ab1"
public_key = "1ac3877559dd79f0d78144270b96f9b8"
hash = "1a7e6112569305e792e3f360b4efe947"

url = f"http://gateway.marvel.com/v1/public/characters?ts={ts}&apikey={public_key}&hash={hash}"

datos = requests.get(url).json()
datos = datos["data"]["results"]

for personaje in datos:
    print(personaje["name"])
