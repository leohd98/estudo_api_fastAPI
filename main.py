from fastapi import *
# Usando QUARY
import requests
app = FastAPI()


@app.get('/api/hello')
def hello_world():
    '''
    Mensagem louca!
    '''
    return {'Hello': 'World'}


@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):

    # Efetua a requisição de acesso da API em arquivo JSON usando requests.get
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    # Passa por um filtro que determina duas respostas diferentes, caso a requisição tenha sucesso ou não.
    if response.status_code == 200:
        # poe o jason dentro da variavel dados_json que é uma lista contendo diversos dicionários nesse caso.
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        # faz um loop através dos dicionários que estão dentro de uma lista em dados_json.
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurantes': restaurante, 'Cardapio': dados_restaurante}

    else:
        return {'ERRO': f'{response.status_code} - {response.text}'}
