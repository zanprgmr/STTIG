from __future__ import annotations
import requests
from craiyon.templates import GeneratedImages

class Craiyon:
   
    def __init__(self) -> None:
        self.BASE_URL = "https://backend.craiyon.com"
        self.session = requests.Session()

    def generate(self, tokens: str) -> GeneratedImages:
        url = self.BASE_URL + "/generate"
        resp = self.session.post(url, json={'prompt': tokens})
        return GeneratedImages(resp.json()['images'])