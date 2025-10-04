import pytest
import pytest
import requests
import json
import os
import tempfile
from playwright.sync_api import sync_playwright
from utils.config import HEADLESS


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
@pytest.fixture(scope="session")
def api_session():
    """Crea una sesión de requests con headers por defecto."""
    session = requests.Session()
    session.headers.update({
        "accept": "application/json",
        "Token": "4e3d1e0ee0850de835adc3e96f8bc6915871296e20bf6fb90b9914b1f7a14aa2"
    })
    return session
@pytest.fixture(scope="session")
def attachments_schema():
    """Carga el schema JSON de attachments."""
    schema_path = os.path.join(os.path.dirname(__file__), "data", "attachments_schema.json")
    with open(schema_path, "r") as f:
        return json.load(f)
    