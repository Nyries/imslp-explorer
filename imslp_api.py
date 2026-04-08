import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://imslp.org/api.php"


def login(username: str = None, password: str = None) -> requests.Session:
    username = username or os.getenv("IMSLP_USER")
    password = password or os.getenv("IMSLP_PASS")
    response = requests.post(API_URL+f"?action=login&lgname={username}&lgpassword={password}")
    response.raise_for_status()


def page_search(): 

    response =  requests.post(API_URL+"?action=query&titles=Symphony_No.5,_Op.67_(Beethoven,_Ludwig_van)&format=json")
    print(response.content)

if __name__ == "__main__":
    login()
    page_search()