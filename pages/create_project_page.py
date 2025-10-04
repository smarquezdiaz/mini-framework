class CreateProjectPage:
    # Selectores actualizados según el modal
    CREATE_BTN = "button:has-text('Create new project')"
    PROJECT_NAME_INPUT = "input[placeholder='For example: Web Application']"
    PROJECT_CODE_INPUT = "input[placeholder='For example: WA']"
    CREATE_PROJECT_BTN = "button:has-text('Create project')"
    
    def __init__(self, page):
        self.page = page
    
    def create_project(self, name: str, code: str):
        """Crea un nuevo proyecto"""
        self.page.click(self.CREATE_BTN)
        
        # Esperar a que aparezca el modal
        self.page.wait_for_selector(self.PROJECT_NAME_INPUT, timeout=5000)
        
        self.page.fill(self.PROJECT_NAME_INPUT, name)
        self.page.fill(self.PROJECT_CODE_INPUT, code)
        self.page.click(self.CREATE_PROJECT_BTN)
        self.page.wait_for_timeout(3000)