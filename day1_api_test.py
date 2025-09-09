import requests

# Example: Pokémon API
url = "https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Name:", data["name"])
    print("ID:", data["id"])
    print("Base Experience:", data["base_experience"])
    print("Abilities:", [ability["ability"]["name"] for ability in data["abilities"]])
else:
    print("Error:", response.status_code)
