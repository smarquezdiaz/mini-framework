import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

BASE_URL = "https://api.qase.io/v1"
TOKEN = os.getenv("TOKEN")

HEADERS = {
    "Token": TOKEN,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

def post(endpoint: str, payload: dict):
    url = f"{BASE_URL}{endpoint}"
    return requests.post(url, headers=HEADERS, json=payload)

def get(endpoint: str):
    url = f"{BASE_URL}{endpoint}"
    return requests.get(url, headers=HEADERS)
