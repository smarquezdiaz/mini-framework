class UpdateProjectPage:
    # Selectores
    SETTINGS_LINK = "text=Settings"
    PROJECT_NAME_INPUT = "input[id]"
    UPDATE_BTN = "button:has-text('Update settings')"
    DELETE_BTN = "button:has-text('Delete project')"
    
    def __init__(self, page):
        self.page = page
    
    def open_settings(self):
        """Abre Settings del proyecto"""
        self.page.evaluate("document.querySelector('.sidebar')?.scrollTo(0, 9999)")
        self.page.wait_for_timeout(500)
        self.page.locator("text=Settings").last.click()
        self.page.wait_for_timeout(1500)
    
    def update_project_name(self, new_name: str):
        """Actualiza el nombre del proyecto"""
        self.page.locator(self.PROJECT_NAME_INPUT).first.fill(new_name)
        self.page.click(self.UPDATE_BTN)
        self.page.wait_for_timeout(2000)
    
    def delete_project(self, project_code: str):
        """Elimina el proyecto"""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        self.page.wait_for_timeout(500)
        self.page.click(self.DELETE_BTN)
        self.page.wait_for_timeout(1000)
        # Click en el botón dentro del dialog modal
        self.page.locator("dialog >> button:has-text('Delete project')").click()
        self.page.wait_for_timeout(2000)