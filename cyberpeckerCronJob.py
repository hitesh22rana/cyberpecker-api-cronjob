import os
import requests
from dotenv import load_dotenv
load_dotenv()


class CyberPeckerCronJob:

    def __init__(self) -> None:
        self.session = requests.session()
        self.URL = os.getenv("BASE_URL")
        self.WORKERS = 4

    @property
    def __get_news_queries(self):
        return self.session.get(self.URL, timeout=10).json()

    def _get_news_route(self):
        data = self.__get_news_queries

        routes = []
        for individual_link in data:
            route = list(individual_link.keys())[0]
            routes.append(self.URL + route)

        return routes

    def get_news_response(self, route):
        self.session.get(route, timeout=10)