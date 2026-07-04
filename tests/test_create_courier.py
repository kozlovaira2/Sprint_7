"""
Тесты для создания курьера
"""

import pytest
import allure
import requests

from utils.endpoints import Endpoints
from utils.test_data import CourierData, StatusCodes
from utils.error_messages import ErrorMessages
from helpers import create_courier_request, generate_courier_data


@allure.epic("Курьеры")
@allure.feature("Создание курьера")
class TestCreateCourier:
    
    @allure.title("Курьера можно создать")
    def test_create_courier_success(self):
        """Проверка успешного создания курьера"""
        login, password, first_name = generate_courier_data()
        response = create_courier_request(login, password, first_name)
        
        assert response.status_code == StatusCodes.CREATED
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_error(self):
        """Проверка создания двух одинаковых курьеров"""
        login, password, first_name = generate_courier_data()
        
        response_first = create_courier_request(login, password, first_name)
        assert response_first.status_code == StatusCodes.CREATED
        
        response_second = create_courier_request(login, password, first_name)
        
        assert response_second.status_code == StatusCodes.CONFLICT
        assert response_second.json()["message"] == ErrorMessages.COURIER_EXISTS

    @allure.title("Для создания курьера нужно передать все обязательные поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_fields(self, missing_field):
        """Проверка ошибки при отсутствии обязательных полей"""
        login = CourierData.generate_random_login()
        password = CourierData.generate_random_password()
        first_name = CourierData.generate_random_first_name()
        
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        del payload[missing_field]
        
        response = requests.post(Endpoints.COURIER, data=payload)
        
        assert response.status_code == StatusCodes.BAD_REQUEST
        assert ErrorMessages.MISSING_FIELD in response.json()["message"]

    @allure.title("Если создать пользователя с логином, который уже есть, возвращается ошибка")
    def test_create_courier_existing_login(self):
        """Проверка ошибки при создании курьера с существующим логином"""
        login, password, first_name = generate_courier_data()
        
        response_first = create_courier_request(login, password, first_name)
        assert response_first.status_code == StatusCodes.CREATED
        
        response_second = create_courier_request(login, "another_password", "AnotherName")
        
        assert response_second.status_code == StatusCodes.CONFLICT
        assert response_second.json()["message"] == ErrorMessages.COURIER_EXISTS