import json
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

# URL da página da web
base_url = 'https://pt.wikipedia.org/wiki/%C3%93scar'

response = requests.get(base_url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

# Encontrar todos os elementos <p> e filtrar aqueles que contêm o texto "melhor", para melhores ganhadores do oscar.
text_p = [p.get_text().strip() for p in soup.find_all('p') if "melhor" in p.get_text().lower()]

# Salvar em JSON
json_filename = "dados.json"

with open(json_filename, mode='w', encoding='utf-8') as json_file:
    data = {"textos": text_p}
    json.dump(data, json_file, ensure_ascii=False, indent=4)

# Mongo connection
client = MongoClient('mongodb://localhost:27017')
db = client['WebScrapingJSON']
collection = db['textJSON']

# Ler dados do arquivo JSON e inserir no MongoDB
with open(json_filename, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    textos = data.get("textos", [])

    for idx, texto in enumerate(textos, start=1):
        data = {
            "id": idx,  # Atribuir um ID único baseado no índice
            "texto": texto  # Extrair o texto da coluna 'texto'
        }
        collection.insert_one(data)
        print(f'Dados {idx} inseridos com sucesso no MongoDB.')
client.close()