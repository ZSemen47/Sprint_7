import random
import string
from http.client import responses

import allure
import requests

from data import COURIER_URL, BASE_URL, COURIER_URL_FOR_DELETE


class CourierMethods:
    @staticmethod
    @allure.step('Создать курьера')
    def create_courier(params=None):
        if params is None:
            params = CourierMethods.generate_courier_data()
        login = params.get('login')
        password = params.get('password')
        first_name = params.get('firstName')
        response = requests.post(f'{BASE_URL}{COURIER_URL}', data=params)
        try:
            return response.json(), response.status_code, login, password, first_name
        except requests.exceptions.JSONDecodeError:
            return response.text, response.status_code, login, password, first_name

    @staticmethod
    @allure.step('Логин курьера')
    def login_courier(params=None):
        response = requests.post(f'{BASE_URL}{COURIER_URL}/login', data=params)
        try:
            return response.json(), response.status_code
        except requests.exceptions.JSONDecodeError:
            return response.text, response.status_code

    @staticmethod
    @allure.step('Удалить курьера')
    def delete_courier(response_id):
        params = {"id": response_id}
        response = requests.delete(f'{BASE_URL}{COURIER_URL_FOR_DELETE}{response_id}', data=params)
        try:
            return response.json(), response.status_code
        except requests.exceptions.JSONDecodeError:
            return response.text, response.status_code

    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_courier_data():
        login = CourierMethods.generate_random_string(10)
        password = CourierMethods.generate_random_string(10)
        first_name = CourierMethods.generate_random_string(10)

        params = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return params

    @staticmethod
    def generate_courier_data_without_one_field():
        password = CourierMethods.generate_random_string(10)
        first_name = CourierMethods.generate_random_string(10)

        params = {
            "password": password,
            "firstName": first_name
        }

        return params

    @staticmethod
    def register_new_courier_and_return_login_password():
        login_pass = []

        login = CourierMethods.generate_random_string(10)
        password = CourierMethods.generate_random_string(10)
        first_name = CourierMethods.generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f'{BASE_URL}{COURIER_URL}', data=payload)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass