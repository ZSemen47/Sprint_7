BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
COURIER_URL = 'courier'
ORDER_URL = 'orders'
COURIER_URL_FOR_DELETE = 'courier/'
not_existed_courier = {
    'login': 'not_existed_courier_login',
    'password': 'not_existed_courier_password',
}
expected_result_create_409 = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
expected_result_ok_true = {'ok': True}
expected_result_code_400 = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
expected_result_login_not_found = {'code': 404, 'message': 'Учетная запись не найдена'}
expected_result_login_bad_request = {'code': 400, 'message': 'Недостаточно данных для входа'}
