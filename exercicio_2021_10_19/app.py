from os import name
from flask import Flask
from service import Service
import json
app = Flask(__name__)

@app.route('/obterPokemons/<p_pokemon>', methods=['GET'])
def obterPokemon(p_pokemon):  
    service = Service()
    pokemons = service.obterPokemons()
    for pokemon in pokemons ['results']:
        if pokemon['name'] == p_pokemon:
            return pokemon
    return "Erro: raça não encontrada" 
 
@app.route('/listarPokemons', methods=['GET'])
def listarPokemons():  
    service = Service()
    pokemons = service.obterPokemons()
    return json.dumps(pokemons)
 
@app.route('/listarNomes', methods=['GET'])
def listarNomes():  
    service = Service()
    pokemons = service.obterPokemons()
    poke_name = [dict(name = k1['name']) for k1 in pokemons['results']]
    resultado = json.dumps(poke_name)
    return resultado