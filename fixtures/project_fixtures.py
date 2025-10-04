import pytest
import json
from pages.login_page import LoginPage
from pages.create_project_page import CreateProjectPage
from pages.update_project_page import UpdateProjectPage
from utils.config import USERNAME, PASSWORD


@pytest.fixture
def setup_and_teardown_project(page):
    # Cargar datos del proyecto
    with open("data/projects.json", encoding="utf-8") as f:
        projects_data = json.load(f)
    
    project = projects_data[0]  # Tomar el primer proyecto
    
    # Setup
    login_page = LoginPage(page)
    create_project_page = CreateProjectPage(page)
    update_project_page = UpdateProjectPage(page)
    
    # Login
    login_page.open()
    login_page.login(USERNAME, PASSWORD)
    page.wait_for_timeout(2000)
    
    # Crear proyecto
    create_project_page.create_project(project["name"], project["code"])
    
    # Entrar al proyecto recién creado
    page.click(f"text={project['name']}")
    page.wait_for_timeout(2000)
    
    # Retornar datos del proyecto para usar en el test
    yield {"name": project["name"], "code": project["code"], "page": page}
    
    # Teardown - Eliminar proyecto
    update_project_page.open_settings()
    update_project_page.delete_project(project["code"])