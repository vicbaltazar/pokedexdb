# 📚 Pokédex com MongoDB e Python

Projeto de estudos que carrega dados de Pokémon a partir de um arquivo `pokemon.json`, insere tudo em uma collection do MongoDB e expõe consultas simples em Python (e pode ser estendido para uma API).  

O foco é praticar leitura de JSON, conexão com banco NoSQL (MongoDB) e consultas básicas.

---

## ⚙️ Tecnologias usadas

- Python 3
- MongoDB (banco NoSQL)
- Biblioteca `pymongo` para conexão com o MongoDB
- Arquivo `pokemon.json` como fonte de dados

---

## 📥 Carregar os Pokémon no MongoDB

Script principal: `carregar_pokemons_mongo.py` (ou o nome que você usou).

### 1. Instalar dependências

- pip install pymongo

### 2. Configurar conexão

No script, a conexão padrão é local:

- client = MongoClient("mongodb://localhost:27017")
- db = client["pokemon_db"]
- collection = db["pokemons"]

Se estiver usando MongoDB Atlas, basta trocar a connection string.

### 3. Executar o script

- python carregar_pokemons_mongo.py


O script:

- Lê o arquivo `pokemon.json`.
- Apaga documentos antigos da collection (`delete_many({})`).
- Insere todos os Pokémon.
- Imprime quantos foram inseridos no terminal.

---

## 🔍 Consultas de exemplo

Trecho de código para buscar dados depois de carregar a base:

- `Buscar um Pokémon específico`
mimikyu = collection.find_one({"name": "Mimikyu"})
print(mimikyu)

- `Listar todos os pokémons de um tipo`
fantasmas = collection.find({"type": "Ghost"})
for p in fantasmas:
print(p["name"], p["type"])

Você pode adaptar esses exemplos para outros campos, como `attack`, `hp`, `total`, etc.

---

## 🔮 Próximos passos

- Criar uma API com FastAPI ou Flask para expor a Pokédex via HTTP.
- Adicionar filtros mais avançados (por múltiplos tipos, faixa de ataque, HP mínimo/máximo).
- Criar índices no MongoDB (`name`, `type`) para melhorar a performance das buscas.
- Conectar um front-end (React, HTML/JS simples) consumindo essa Pokédex.

---

Projeto feito para praticar **Python + MongoDB** com um tema divertido de Pokémon. 🐾
