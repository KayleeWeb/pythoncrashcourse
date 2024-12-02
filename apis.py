import requests 

class Pokemon:
    def __init__(self,name,number,height,weight,stats,types):
        self.name = name
        self.number = number
        self.height = height
        self.weight = weight
        self.stats = stats
        # hp, atk, def, spa, spd, 
        self.types = types


    def __str__(self):
        output_string = ""
        output_string += str(self.number) + "\n"
        output_string += self.name.capitalize() + "\n"
        output_string += f"Height: {self.height/10}m, Weight: {self.weight/10}kg\n"
        output_string += "Types: " + ", ".join(self.types) + "\n"
        output_string += f"HP: {self.stats[0]}, ATK: {self.stats[1]}, DEF: {self.stats[2]}, SPA: {self.stats[3]}, SPD: {self.stats[4]}, SPE:{self.stats[5]}\n"
        return output_string
    
r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")

data = r.json()
results = data["results"]

for result in results[:10]:
    r = requests.get(result["url"])
    data = r.json()

    stats = []
    for stat in data["stats"]:
        stats.append(stat["base_stat"])

    types = []
    for poke_type in data["types"]:
        types.append(poke_type["type"]["name"])

    pokemon = Pokemon(data["name"], data ["id"],data ["height"],data["weight"],stats,types)
    print(pokemon)
  #  print(pokemon.number, pokemon.name,pokemon.height,pokemon.weight,pokemon.stats,pokemon.types)

