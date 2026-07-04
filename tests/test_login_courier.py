"""
Тесты для авторизации курьера
"""

import allure
import requests
import pytest

from utils.endpoints import Endpoints
from utils.test_data import Users, CourierData
from utils.error_messages import ErrorMessages
from helpers import login_courier_request


class TestLoginCourier:

    @allure.title('Авторизация под курьером выдает id')
    def test_courier_log_in(self, create_courier):
        """Проверка успешной авторизации курьера"""
        response = login_courier_request(
            create_courier["login"],
            create_courier["password"]
        )
        assert response.status_code == 200
        assert 'id' in response.text

    @allure.title('Ошибка при авторизации если логин или пароль не корректные')
    def test_courier_log_negative(self):
        """Проверка ошибки при неверном логине или пароле"""
        response = login_courier_request(
            Users.data_negative["login"],
            Users.data_negative["password"]
        )
        assert response.status_code == 404
        assert ErrorMessages.AUTH_FAILED in response.text

    @allure.title('Ошибка при авторизации если логин пустой')
    def test_courier_log_with_empty_login(self):
        """Проверка ошибки при авторизации с пустым логином"""
        response = login_courier_request("", CourierData.DEFAULT_PASSWORD)
        assert response.status_code == 400
        assert ErrorMessages.MISSING_AUTH_FIELDS in response.text

    @allure.title('Ошибка при авторизации если пароль пустой')
    def test_courier_log_with_empty_password(self):
        """Проверка ошибки при авторизации с пустым паролем"""
        response = login_courier_request(CourierData.DEFAULT_LOGIN, "")
        assert response.status_code == 400
        assert ErrorMessages.MISSING_AUTH_FIELDS in response.text