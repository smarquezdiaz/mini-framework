import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("BASE_URL1", "https://www.saucedemo.com/")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
TOKEN = os.getenv("TOKEN", "placeholder_token_for_safety")
USERNAME = os.getenv("USERNAME", "placeholder_user@example.com")
PASSWORD = os.getenv("PASSWORD", "placeholder_password")
BASE_URL_API = os.getenv("BASE_URL_API", "https://api.default.com/v1/")
SUITE = os.getenv("SUITE", "default_suite_name")

# HEADLESS = False  # o True, según lo que quieras por defecto
BROWSER = "chromium"  # opcional, si quieres parametrizar