class CreateCasePage:
    NEW_CASE_BTN = "button[id='create-case-menu-trigger']"
    MANUAL_OPTION = "text= Create manually"
    TITLE_INPUT = "input[name='title']"
    SAVE_BTN = "button[id='save-case']"
    SUCCESS_MSG = "text=Test case was created successfully!" 

    def __init__(self, page):
        self.page = page

    def open_new_case_form(self):
        self.page.click(self.NEW_CASE_BTN)
        self.page.click(self.MANUAL_OPTION)

    def create_case(self, title: str):
        self.open_new_case_form()
        self.page.fill(self.TITLE_INPUT, title)
        self.page.click(self.SAVE_BTN)

    def is_case_created(self) -> bool:
        
        try:
            self.page.wait_for_selector(self.SUCCESS_MSG, timeout=5000)
            return True
        except:
            return False
