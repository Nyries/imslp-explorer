import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://imslp.org/api.php"


def login(username: str = None, password: str = None) -> requests.Session:
    username = username or os.getenv("IMSLP_USER")
    password = password or os.getenv("IMSLP_PASS")
    response = requests.post(API_URL+f"?action=login&lgname={username}&lgpassword={password}")
    print(response)
    response.raise_for_status()

login()