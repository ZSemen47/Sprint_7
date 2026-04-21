import pytest
from methods.courier_methods import CourierMethods


@pytest.fixture
def create_courier():
    response1, status_code1, login, password, first_name = CourierMethods().create_courier()
    yield response1, status_code1
    params = {
        'login': login,
        'password': password
    }
    response2, status_code2 = CourierMethods().login_courier(params)
    CourierMethods().delete_courier(response2.get('id'))

@pytest.fixture
def create_courier_duplicate():
    response1, status_code1, login, password, first_name = CourierMethods().create_courier()
    params_for_duplicate = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response2, status_code2, login2, password2, first_name2 = CourierMethods().create_courier(params_for_duplicate)
    yield response2, status_code2
    params_for_login = {
        'login': login,
        'password': password
    }
    response3, status_code3 = CourierMethods().login_courier(params_for_login)
    CourierMethods().delete_courier(response3.get('id'))

@pytest.fixture
def create_courier_without_one_filed():
    params = CourierMethods().generate_courier_data_without_one_field()
    response1, status_code1, login, password, first_name = CourierMethods().create_courier(params)
    yield response1, status_code1


@pytest.fixture
def create_courier_and_login():
    response1, status_code1, login, password, first_name = CourierMethods().create_courier()
    params = {
        'login': login,
        'password': password
    }
    response2, status_code2 = CourierMethods().login_courier(params)
    response_id = response2.get('id')
    yield response2, status_code2, response_id
    CourierMethods().delete_courier(response_id)

@pytest.fixture
def create_courier_and_login_with_wrong_pass():
    response1, status_code1, login, password, first_name = CourierMethods().create_courier()
    params = {
        'login': password,
        'password': login
    }
    response2, status_code2 = CourierMethods().login_courier(params)
    response_id = response2.get('id')
    yield response2, status_code2, response_id
    CourierMethods().delete_courier(response_id)

@pytest.fixture
def create_courier_and_login_without_one_field():
    response1, status_code1, login, password, first_name = CourierMethods().create_courier()
    params = {
        'login': '',
        'password': password
    }
    response2, status_code2 = CourierMethods().login_courier(params)
    response_id = response2.get('id')
    yield response2, status_code2, response_id
    CourierMethods().delete_courier(response_id)

@pytest.fixture
def login_not_existed_courier():
    params = {
        'login': 'absolutely_not_existed',
        'password': 'absolutely_not_existed'
    }
    response, status_code = CourierMethods().login_courier(params)
    yield response, status_code

@pytest.fixture
def create_courier_and_login_and_delete():
    response1, status_code1, login, password = CourierMethods().create_courier()
    params = {
        'login': login,
        'password': password
    }
    response2, status_code2 = CourierMethods().login_courier(params)
    response_id = response2.get('id')
    response3 = CourierMethods().delete_courier(response_id)
    yield response3
