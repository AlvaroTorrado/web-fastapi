from fastapi import FastAPI, Request,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from data.database import database
from typing import Annotated
from typing import Union
from data.modelo.jugador import Jugador
from data.dao.dao_jugadores import DaoJugadores


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/laliga", response_class=HTMLResponse)
async def laliga(request: Request):
    return templates.TemplateResponse("laliga.html", {"request": request})

@app.get("/premierleague", response_class=HTMLResponse)
async def premier(request: Request):
    return templates.TemplateResponse("premierleague.html", {"request": request})

@app.get("/bundesliga", response_class=HTMLResponse)
async def bundesliga(request: Request):
    return templates.TemplateResponse("bundesliga.html", {"request": request})

@app.get("/seriea", response_class=HTMLResponse)
async def seriea(request: Request):
    return templates.TemplateResponse("seriea.html", {"request": request})

@app.get("/mls", response_class=HTMLResponse)
async def mls(request: Request):
    return templates.TemplateResponse("mls.html", {"request": request})

@app.get("/ligue1", response_class=HTMLResponse)
async def ligue1(request: Request):
    return templates.TemplateResponse("ligue1.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/")
def read_root():
    return DaoJugadores().get_all(database)

@app.get("/jugadores")
def get_jugadores(request: Request, nombre: str = "usuario", otro: int = 1):
    jugadores = DaoJugadores().get_all(database)
    return templates.TemplateResponse(
        "jugadores.html", 
        {"request": request, "jugadores": jugadores}
    )

@app.post("/jugadores/add")
def add_jugadores(request: Request, nombre: Annotated[str, Form()]):
    dao = DaoJugadores()
    dao.insert(database, nombre)
    jugadores = DaoJugadores().get_all(database)  # Volver a cargar la lista de jugadores
    return templates.TemplateResponse(
        "jugadores.html", 
        {"request": request, "jugadores": jugadores}
    )

@app.post("/jugadores/delete")
def delete_jugadores(request: Request, nombre: Annotated[str, Form()]):
    dao = DaoJugadores()
    dao.delete(database, nombre)
    jugadores = DaoJugadores().get_all(database)  # Volver a cargar la lista de jugadores después de eliminar
    return templates.TemplateResponse(
        "jugadores.html", 
        {"request": request, "jugadores": jugadores, "message": f"Jugador '{nombre}' eliminado correctamente"}
    )

@app.get("/jugadores/buscar")
def buscar_jugador(request: Request, nombre: str):
    # Intentamos encontrar el jugador en la base de datos
    jugadores = DaoJugadores().get_all(database)
    
    # Filtrar el jugador que coincida con el nombre
    jugador_encontrado = None
    for jugador in jugadores:
        if jugador.nombre.lower() == nombre.lower():  # Compara sin distinguir mayúsculas/minúsculas
            jugador_encontrado = jugador
            break
    
    if jugador_encontrado:
        return templates.TemplateResponse("jugador_encontrado.html", {"request": request, "jugador": jugador_encontrado})
    else:
        return templates.TemplateResponse("jugadores.html", {"request": request, "jugadores": jugadores, "message": f"No se encontró al jugador '{nombre}'."})


