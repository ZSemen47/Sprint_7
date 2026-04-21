import random
import string
from http.client import responses

import allure
import requests

from data import COURIER_URL, BASE_URL, COURIER_URL_FOR_DELETE


class CourierMethods:
    @allure.step('Создать курьера')
    def create_courier(self, params=None):
        if params is None:
            params = self.generate_courier_data()
        login = params.get('login')
        password = params.get('password')
        first_name = params.get('firstName')
        response = requests.post(f'{BASE_URL}{COURIER_URL}', data=params)
        try:
            return response.json(), response.status_code, login, password, first_name
        except response.json().decoder.JSONDecodeError:
            return response.text, response.status_code, login, password, first_name


    @allure.step('Логин курьера')
    def login_courier(self, params=None):
        # login_pass = self.register_new_courier_and_return_login_password_name()
        # for_login_creds = {'login': login_pass[0], 'password': login_pass[1]}
        response = requests.post(f'{BASE_URL}{COURIER_URL}/login', data=params)
        try:
            return response.json(), response.status_code
        except response.json().decoder.JSONDecodeError:
            return response.text, response.status_code


    @allure.step('Удалить курьера')
    def delete_courier(self, response_id):
        params  = {"id": response_id}
        response = requests.delete(f'{BASE_URL}{COURIER_URL_FOR_DELETE}{response_id}', data=params)
        try:
            return response.json(), response.status_code
        except response.json().decoder.JSONDecodeError:
            return response.text, response.status_code

    @staticmethod
    def generate_courier_data():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        params = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return params

    @staticmethod
    def generate_courier_data_without_one_field():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        password = generate_random_string(10)
        first_name = generate_random_string(10)

        params = {
            "password": password,
            "firstName": first_name
        }

        return params

    @staticmethod
    def register_new_courier_and_return_login_password_name():
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
        return login_pass
