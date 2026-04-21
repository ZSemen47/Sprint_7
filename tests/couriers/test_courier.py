import allure

from data import expected_result_create_409, expected_result_ok_true, expected_result_code_400, \
    expected_result_login_bad_request, expected_result_login_not_found
from methods.courier_methods import CourierMethods


class TestCourierCreate:
    @allure.title('Курьера можно создать')
    def test_post_create_courier_is_possible(self, create_courier):
        response, status_code = create_courier
        assert status_code == 201

    @allure.title('Чтобы создать курьера, нужно передать в ручку все обязательные поля')
    def test_post_create_all_required_fields_success(self, create_courier):
        response, status_code = create_courier
        assert status_code == 201

    @allure.title('Запрос возвращает правильный код ответа')
    def test_post_create_courier_return_correct_status_code(self, create_courier):
        response, status_code = create_courier
        assert status_code == 201

    @allure.title('Успешный запрос возвращает {"ok":true}')
    def test_post_create_courier_return_ok_true(self, create_courier):
        response, status_code = create_courier
        assert response == expected_result_ok_true

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_post_create_courier_duplicate_return_4o9(self, create_courier_duplicate):
        response, status_code = create_courier_duplicate
        assert response == expected_result_create_409

    @allure.title('Если создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_post_create_courier_duplicate_return_4o9(self, create_courier_duplicate):
        response, status_code = create_courier_duplicate
        assert response == expected_result_create_409

    @allure.title('Если одного из полей нет, запрос возвращает ошибку')
    def test_post_create_courier_without_one_filed_return_400(self, create_courier_without_one_filed):
        response, status_code = create_courier_without_one_filed
        assert response == expected_result_code_400


class TestCourierLogin:
    @allure.title('Курьер может авторизоваться')
    def test_post_login_is_possible_and_return_200(self, create_courier_and_login):
        response, status_code, id = create_courier_and_login
        assert status_code == 200

    @allure.title('Для авторизации нужно передать все обязательные поля')
    def test_post_login_is_possible_with_all_fields(self, create_courier_and_login):
        response, status_code, id = create_courier_and_login
        assert status_code == 200

    @allure.title('Система вернёт ошибку, если неправильно указать логин или пароль')
    def test_post_login_wrong_login_pass_return_404(self, create_courier_and_login_with_wrong_pass):
        response, status_code, id = create_courier_and_login_with_wrong_pass
        assert status_code == 404

    @allure.title('Если какого-то поля нет, запрос возвращает ошибку')
    def test_post_login_without_one_field_bad_request(self, create_courier_and_login_without_one_field):
        response, status_code, id = create_courier_and_login_without_one_field
        assert response == expected_result_login_bad_request

    @allure.title('Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_post_login_not_existed_courier_not_found(self, login_not_existed_courier):
        response, status_code = login_not_existed_courier
        assert response == expected_result_login_not_found

    @allure.title('Успешный запрос возвращает id')
    def test_post_login_success_return_id(self, create_courier_and_login):
        response, status_code, id = create_courier_and_login
        assert 'id' in response
