import json
import pytest
import os
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.create_case_page import CreateCasePage

# Cargar data desde JSON
with open("data/cases.json", encoding="utf-8") as f:
    cases_data = json.load(f)

load_dotenv()
USER = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

@pytest.mark.parametrize("case", cases_data)
def test_create_case_in_demo_project(page, case):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    create_case_page = CreateCasePage(page)

    # 1. Ir al login
    login_page.open()
    login_page.login("chakisoftpruebas@gmail.com", "chakisoft.1203.Qa")

    # 2. Entrar al proyecto "Demo Project"
    dashboard_page.open_demo_project()

    # 3. Crear caso de prueba con data del JSON
    create_case_page.create_case(case["title"])

    # 4. Validar creación
    assert create_case_page.is_case_created()