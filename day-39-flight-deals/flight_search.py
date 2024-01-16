import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta


class FlightSearch:
    def __init__(self):
        load_dotenv()
        self.headers = {
            "apikey": os.environ["TEQ_APIKEY"],
        }
        self.code_list = []

    def get_city_code(self, city_list):
        get_endpoint = os.environ["GET_ENDPOINT"]
        for name in city_list:
            get_params = {
                "term": name,
                "location_types": "city"
            }
            response = requests.get(url=get_endpoint, params=get_params, headers=self.headers)
            response.raise_for_status()
            data = response.json()['locations'][0]['code']
            self.code_list.append(data)
        return self.code_list

    def search_flight(self, destination):
        search_endpoint = os.environ["SEARCH_ENDPOINT"]
        search_params = {
            "fly_from": "SIN",
            "fly_to": destination,
            "date_from": (datetime.now() + timedelta(1)).strftime("%d/%m/%Y"),
            "date_to": (datetime.now() + timedelta(91)).strftime("%d/%m/%Y"),
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "curr": "SGD",
            "max_stopovers": 0,
        }
        response = requests.get(url=search_endpoint, params=search_params, headers=self.headers)
        response.raise_for_status()
        return response.json()




