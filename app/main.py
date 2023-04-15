from .api import auth, user
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import sessionmaker

from app.db import models
from app.db.database import engine

models.Base.metadata.create_all(bind=engine)

# Create a database session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Register the API endpoints
app.include_router(auth.router)
app.include_router(user.router)


# The base view is the login view
@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


# Route used to display the home page to the user
@app.get("/home")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
