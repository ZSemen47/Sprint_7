import random
import string

import allure
import requests

from data import COURIER_URL, BASE_URL, ORDER_URL

class OrderMethods:
    def __init__(self):
        self.url = f'{BASE_URL}{ORDER_URL}'

    @allure.step("Создание заказа")
    def post_order(self, params):
        response = requests.post(self.url, json=params)
        try:
            return response.json(), response.status_code
        except response.json().decoder.JSONDecodeError:
            return response.text, response.status_code

    @allure.step('Получить список заказов')
    def get_orders(self):
        response = requests.get(self.url)
        try:
            return response.json(), response.status_code
        except response.json().decoder.JSONDecodeError:
            return response.text, response.status_code