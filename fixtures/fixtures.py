import pytest
import requests
import os

BASE_URL = "https://api.qase.io/v1"
TOKEN = "4e3d1e0ee0850de835adc3e96f8bc6915871296e20bf6fb90b9914b1f7a14aa2"

@pytest.fixture
def get_attachments():
    url = f"{BASE_URL}/attachment?limit=10&offset=0"
    headers = {
        "accept": "application/json",
        "Token": TOKEN
    }
    response = requests.get(url, headers=headers)
    return response


@pytest.fixture
def generate_txt_file(tmp_path):
    """Genera un archivo txt temporal para pruebas"""
    file_path = tmp_path / "test_file.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("Este es un archivo de prueba para Qase API.")
    return str(file_path)
