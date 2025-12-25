from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from bson import ObjectId

# ----- Configuração MongoDB -----
client = MongoClient("mongodb://localhost:27017")
db = client["pokemon_db"]
collection = db["pokemons"]

app = FastAPI(title="Pokédex API - MongoDB")

# CORS (opcional, útil para front-end em JS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Utilitário para converter ObjectId em string
def serialize_pokemon(doc):
    if not doc:
        return None
    doc["_id"] = str(doc["_id"])
    return doc

# ----- Rotas -----

@app.get("/")
def root():
    return {"message": "Pokédex API está no ar!"}

@app.get("/pokemons")
def listar_pokemons(limit: int = 20, skip: int = 0):
    """Lista pokémons com paginação simples."""
    cursor = collection.find({}).skip(skip).limit(limit)
    pokemons = [serialize_pokemon(p) for p in cursor]
    return pokemons

@app.get("/pokemons/{name}")
def buscar_por_nome(name: str):
    """Busca um pokémon pelo nome exato (case sensitive)."""
    doc = collection.find_one({"name": name})
    if not doc:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")
    return serialize_pokemon(doc)

@app.get("/tipo/{tipo}")
def buscar_por_tipo(tipo: str, limit: int = 50):
    """Lista pokémons que tenham esse tipo (ex.: Ghost, Fire)."""
    cursor = collection.find({"type": tipo}).limit(limit)
    pokemons = [serialize_pokemon(p) for p in cursor]
    return pokemons

@app.get("/ataque/minimo/{valor}")
def buscar_por_ataque_minimo(valor: int, limit: int = 50):
    """Pokémons com ataque >= valor."""
    cursor = collection.find({"attack": {"$gte": valor}}).limit(limit)
    pokemons = [serialize_pokemon(p) for p in cursor]
    return pokemons
