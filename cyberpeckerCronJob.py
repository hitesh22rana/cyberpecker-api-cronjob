import os
import requests
from dotenv import load_dotenv
load_dotenv()


class cyberPeckerCronJob:

    def __init__(self) -> None:
        self.session = requests.session()
        self.BASE_URL = os.getenv("BASE_URL")
        self.WORKERS = 4

    def _getNewsQueries(self):
        return self.session.get(self.BASE_URL, timeout=10).json()

    def _getNewsRoute(self):
        data = self._getNewsQueries()

        routes = []
        for individualLink in data:
            route = list(individualLink.keys())[0]
            routes.append(self.BASE_URL + route)

        return routes

    def getNewsResponse(self, route):
        self.session.get(route, timeout=10)