"""
Фикстуры для тестов
"""

import pytest
import requests

from utils.endpoints import Endpoints
from helpers import generate_courier_data, create_courier_request, login_courier_request, delete_courier


@pytest.fixture
def create_courier():
    """Фикстура для создания курьера и возврата его данных"""
    login, password, first_name = generate_courier_data()
    
    response = create_courier_request(login, password, first_name)
    
    courier_data = {
        "login": login,
        "password": password,
        "firstName": first_name,
        "status_code": response.status_code
    }

    yield courier_data

    # После теста удаляем курьера
    courier_id = login_courier_request(login, password).json().get("id")
    delete_courier(courier_id)


@pytest.fixture
def create_order():
    """Фикстура для создания заказа"""
    from utils.test_data import OrderData
    
    def _create_order(color=None):
        return OrderData.create_order_request(color)
    
    return _create_order