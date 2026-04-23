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
