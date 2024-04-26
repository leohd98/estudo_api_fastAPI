# Importa a library requests
import requests
# Importa a library json
import json

# Efetua a requisição de acesso da API em arquivo JSON usando requests.get
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

# Passa por um filtro que determina duas respostas diferentes, caso a requisição tenha sucesso ou não.
if response.status_code == 200:

    # poe o jason dentro da variavel dados_json que é uma lista contendo diversos dicionários nesse caso.
    dados_json = response.json()

    # cria um dicionário vazio na variável dados_restaurante
    dados_restaurante = {}

    # faz um loop através dos dicionários que estão dentro de uma lista em dados_json.
    for item in dados_json:

        # coloca o conteúdo da chave Company que retém o nome do restaurante dentro da variável nome_do_restaurante a cada loop do for.
        nome_do_restaurante = item['Company']

        # faz o teste a cada loop, se o nome_do_restaurante não estiver dentro do dicionário dados_restaurante ele faz algo.
        if nome_do_restaurante not in dados_restaurante:

            # cria uma nova chave com o nome do restaurante que tem uma lista vazia como valor.
            dados_restaurante[nome_do_restaurante] = []

        # na chave do nome do restaurante, que é uma lista vazia, ele adiciona através do append um dicionário contendo as infos de cada
        # loop for, que passa de dicionários em dicionários dentro do json.
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

else:
    print(f'O erro foi {response.status_code}')

for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)
