"""
Фикстуры для тестов
"""

import pytest
import requests

from utils.endpoints import Endpoints
from helpers import register_new_courier_and_return_login_password


@pytest.fixture
def create_courier():
    """Фикстура для создания курьера и возврата его данных"""
    login, password, first_name = register_new_courier_and_return_login_password()
    courier_data = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    yield courier_data

    # После теста удаляем курьера
    response = requests.post(
        Endpoints.COURIER_LOGIN,
        data={"login": login, "password": password}
    )
    if response.status_code == 200:
        courier_id = response.json().get("id")
        if courier_id:
            requests.delete(Endpoints.courier_by_id(courier_id))


@pytest.fixture
def create_order():
    """Фикстура для создания заказа"""
    from utils.test_data import OrderData

    def _create_order(color=None):
        payload = OrderData.generate_order_payload(color)
        response = requests.post(Endpoints.ORDERS, json=payload)
        return response

    return _create_order


@pytest.fixture
def auth_courier(create_courier):
    """Фикстура для авторизации курьера"""
    courier_data = create_courier

    response = requests.post(
        Endpoints.COURIER_LOGIN,
        data={"login": courier_data["login"], "password": courier_data["password"]}
    )
    if response.status_code == 200:
        courier_data["id"] = response.json().get("id")

    return courier_data