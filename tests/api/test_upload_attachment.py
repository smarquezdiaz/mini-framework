import requests
import pytest
from fixtures.fixtures import generate_txt_file  

BASE_URL = "https://api.qase.io/v1"
TOKEN = "4e3d1e0ee0850de835adc3e96f8bc6915871296e20bf6fb90b9914b1f7a14aa2"

headers = {
    "accept": "application/json",
    "Token": TOKEN
}
def test_upload_txt_file(generate_txt_file):
    """Test que sube un archivo txt a Qase y valida el schema de respuesta"""

    url = f"{BASE_URL}/attachment/DEMO"

    # Preparar archivo para subir
    files = {
        "file": ("test_file.txt", open(generate_txt_file, "rb"), "text/plain")
    }

    response = requests.post(url, files=files, headers=headers)

    # Validación del status code
    assert response.status_code == 200, f"Error en API: {response.text}"

    data = response.json()

    # Validar que tenga la estructura del schema
    assert "status" in data
    assert isinstance(data["status"], bool)

    assert "result" in data
    assert isinstance(data["result"], list)

    if data["result"]:  # si hay resultados
        item = data["result"][0]
        for field in ["extension", "filename", "hash", "mime", "team", "url"]:
            assert field in item, f"Falta el campo {field} en la respuesta"
