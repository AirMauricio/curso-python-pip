import store
from fastapi import FastAPI # Desde el modulo fastapi se importa fastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/') # Decorador, aui se le da la ruta de por donde pueden empezar 
def get_list():
    return[1,2,3]

@app.get('/contact', response_class = HTMLResponse) # Decorador, aui se le da la ruta de por donde pueden empezar 
def get_list():
    return"""
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    """
    

def run():
    store.get_categories()

if __name__ == '__main__':
    run()