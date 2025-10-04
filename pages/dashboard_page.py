from playwright.sync_api import Page

class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        # Localizador del proyecto "Demo Project"
        self.demo_project_link = page.locator("text=Demo Project")

    def open_demo_project(self):
        self.demo_project_link.click()