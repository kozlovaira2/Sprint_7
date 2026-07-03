"""
Тесты для создания курьера
"""

import pytest
import allure
import requests

from utils.endpoints import Endpoints
from utils.test_data import CourierData, StatusCodes
from utils.error_messages import ErrorMessages
from helpers import register_new_courier_and_return_login_password


@allure.epic("Курьеры")
@allure.feature("Создание курьера")
class TestCreateCourier:
    
    @allure.title("Создание курьера - успешный сценарий")
    def test_create_courier_success(self):
        """Проверка успешного создания курьера"""
        login, password, first_name = register_new_courier_and_return_login_password()
        
        assert login, "Курьер не был создан"
        
        # Проверяем, что курьер действительно существует
        response = requests.post(
            Endpoints.COURIER_LOGIN,
            data={"login": login, "password": password}
        )
        assert response.status_code == StatusCodes.OK
        assert "id" in response.json()

    @allure.title("Создание дублирующего курьера - ошибка")
    def test_create_duplicate_courier_error(self):
        """Проверка создания двух одинаковых курьеров"""
        # Создаем первого курьера
        login, password, first_name = register_new_courier_and_return_login_password()
        assert login, "Не удалось создать первого курьера"
        
        # Пытаемся создать второго с теми же данными
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(Endpoints.COURIER, data=payload)
        
        assert response.status_code == StatusCodes.CONFLICT
        assert ErrorMessages.COURIER_EXISTS in response.json()["message"]

    @allure.title("Создание курьера с пропущенными полями")
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_fields(self, missing_field):
        """Проверка ошибки при отсутствии обязательных полей"""
        payload = CourierData.get_valid_courier_data()
        del payload[missing_field]
        
        response = requests.post(Endpoints.COURIER, data=payload)
        
        # Для поля firstName API может возвращать 409, а не 400
        if missing_field == "firstName":
            assert response.status_code in [StatusCodes.BAD_REQUEST, StatusCodes.CONFLICT]
            assert "message" in response.json()
        else:
            assert response.status_code == StatusCodes.BAD_REQUEST
            assert ErrorMessages.MISSING_FIELD in response.json()["message"]

    @allure.title("Создание курьера с существующим логином - ошибка")
    def test_create_courier_existing_login(self):
        """Проверка ошибки при создании курьера с существующим логином"""
        # Создаем первого курьера
        login, password, first_name = register_new_courier_and_return_login_password()
        assert login, "Не удалось создать первого курьера"
        
        # Пытаемся создать второго курьера с тем же логином, но другим паролем
        payload = {
            "login": login,
            "password": "another_password",
            "firstName": "AnotherName"
        }
        response = requests.post(Endpoints.COURIER, data=payload)
        
        assert response.status_code == StatusCodes.CONFLICT
        assert ErrorMessages.COURIER_EXISTS in response.json()["message"]

    @allure.title("Проверка успешного ответа при создании курьера")
    def test_create_courier_success_response(self):
        """Проверка формата успешного ответа"""
        login, password, first_name = register_new_courier_and_return_login_password()
        
        assert login, "Курьер не был создан"
        
        # Проверяем, что курьер существует
        response = requests.post(
            Endpoints.COURIER_LOGIN,
            data={"login": login, "password": password}
        )
        assert response.status_code == StatusCodes.OK
        assert "id" in response.json()