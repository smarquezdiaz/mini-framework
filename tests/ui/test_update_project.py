import pytest
from pages.update_project_page import UpdateProjectPage
from fixtures.project_fixtures import setup_and_teardown_project


def test_update_project_name(setup_and_teardown_project):
    project_data = setup_and_teardown_project
    page = project_data["page"]
    original_name = project_data["name"]
    
    update_project_page = UpdateProjectPage(page)
    # Abrir Settings
    update_project_page.open_settings()
    # Cambiar nombre
    new_name = f"{original_name} Updated"
    update_project_page.update_project_name(new_name)
    # Validar que el nombre se actualizó
    current_name = page.locator("input[id]").first.input_value()
    assert current_name == new_name, f"Expected '{new_name}', got '{current_name}'"