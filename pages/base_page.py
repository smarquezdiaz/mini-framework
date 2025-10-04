
class BasePage:
    def __init__(self, page):
        self.page = page
    def goto(self, url): self.page.goto(url)
    def fill(self, sel, val): self.page.fill(sel, val)
    def click(self, sel): self.page.click(sel)