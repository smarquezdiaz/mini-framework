import os

BASE_URL = os.getenv('BASE_URL1','https://www.saucedemo.com/')
HEADLESS = os.getenv('HEADLESS','True').lower() == 'true'