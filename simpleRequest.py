import requests
#https://pokeapi.co/
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_infor(name):
    url = f"{base_url}/pokemon/{name}"
    responce = requests.get(url)
    print(requests)

    if responce.status_code==200:
        pokemon_data = responce.json()
        return pokemon_data
        #print(pokemon_data)
         #print("Data was retieved")
    else:
        print(f"Data was not retieved{responce.status_code}")
pokemone_name = "pikachu"
pokemon_infor = get_pokemon_infor(pokemone_name) 

if pokemon_infor:
    print(f"name:{pokemon_infor["name"]}")
    print(f"id:{pokemon_infor["id"]}")
    print(f"height:{pokemon_infor["height"]}")
    print(f"weight:{pokemon_infor["weight"]}")