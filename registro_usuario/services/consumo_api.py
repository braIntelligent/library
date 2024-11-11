import requests

def consumo_api_nombre(valor_obtenido):
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={valor_obtenido}')
    response.raise_for_status()
    if response.status_code == 200:
        data = response.json()
        books = data.get('items', [])
        return books
    
def consumo_api_id(id):
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes/{id}')
    response.raise_for_status()
    if response.status_code == 200:
        data = response.json()
        return data


