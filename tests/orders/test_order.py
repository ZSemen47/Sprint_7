import allure
import pytest

from data import order_params
from methods.order_methods import OrderMethods


class TestOrder:
    @allure.title('Заказ с разными значениями цвета возвращает трек-номер')
    @pytest.mark.parametrize("order_data", [
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": ["BLACK"]
        },
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": ["GREY"]
        },
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": ["BLACK", "GREY"]
        },
        {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": []
        }
    ])
    @allure.title('Заказ с разными значениями цвета возвращает трек-номер')
    def test_post_create_order_return_201(self, order_data):
        response, status_code = OrderMethods().post_order(order_params)
        assert status_code == 201 and 'track' in response

    @allure.title('В тело ответа возвращается список заказов')
    def test_get_order_return_list(self):
        response, status_code = OrderMethods().get_orders()
        assert len(response) > 0
