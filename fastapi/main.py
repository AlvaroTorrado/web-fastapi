from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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
