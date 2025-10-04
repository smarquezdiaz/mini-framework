from pages.login_page import LoginPage
from utils.config import PASSWORD, USERNAME
from utils.helpers import assert_visible
from playwright.sync_api import expect


def test_login(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    page.wait_for_url("https://app.qase.io/projects")
    projects_heading_selector = "h1:has-text('Projects')"
    page.wait_for_selector(projects_heading_selector, timeout=15000)
    projects_heading = page.get_by_role("heading", name="Projects")
    expect(projects_heading).to_be_visible()