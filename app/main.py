from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from .routes import router

app = FastAPI()

os.makedirs("reportes", exist_ok=True)

app.mount("/reportes", StaticFiles(directory="reportes"), name="reportes")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes poner el dominio exacto de tu Angular si ya lo sabes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas
app.include_router(router)
