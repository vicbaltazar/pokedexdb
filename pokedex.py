import json
from pymongo import MongoClient

# 1. Ler JSON local
with open("pokemon.json", "r", encoding="utf-8") as f:
    pokemons = json.load(f)

# 2 Conectar ao MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["pokemon_db"]
collection = db["pokemons"]

# 3 Limpar collection
collection.delete_many({})

# 4 Inserir os documentos
result = collection.insert_many(pokemons)
print(f"Inseridos {len(result.inserted_ids)} pokémons no MongoDB.")

# Buscar um Pokémon 
mimikyu = collection.find_one({"name": "Mimikyu"})
print(mimikyu)

# Todos os pokémon de um tipo
fantasmas = collection.find({"type": "Ghost"})
for p in fantasmas:
    print(p["name"], p["type"])