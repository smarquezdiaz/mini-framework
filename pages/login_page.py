class LoginPage:
    URL="https://app.qase.io/login"
    USER = "[name='email']" 
    PWD = "[name='password']"
    BTN = ":text('Sign in')"
    # ERR="[data-test='error']"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def login(self, user, pwd):
        self.page.fill(self.USER, user)
        self.page.fill(self.PWD, pwd)
        self.page.click(self.BTN)

    # def error_visible(self):
    #     return self.page.locator(self.ERR).is_visible()