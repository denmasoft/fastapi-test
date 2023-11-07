try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin
import requests
import json
from src.endpoints import BASE_URL

USERS_URL = urljoin(BASE_URL, 'users')


def get_users():
    response = requests.get(USERS_URL)
    if response.ok:
        return json.loads(response.text)
    else:
        return None
