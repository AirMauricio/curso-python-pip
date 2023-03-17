import requests # Libreria para traer información de una pagian Web

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text) # Lo trae en forma de String
    cateogiries = r.json()

    print('*'*10)
    for category in cateogiries:
        print(category['name'])
