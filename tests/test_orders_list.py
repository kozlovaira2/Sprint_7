"""
Тесты для получения списка заказов
"""

import allure
import requests

from utils.endpoints import Endpoints
from utils.test_data import StatusCodes


@allure.epic("Заказы")
@allure.feature("Список заказов")
class TestOrdersList:
    
    @allure.title("Получение списка заказов")
    def test_get_orders_list(self):
        """Проверка, что возвращается список заказов"""
        response = requests.get(Endpoints.ORDERS)
        
        assert response.status_code == StatusCodes.OK
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)

    @allure.title("Проверка структуры заказа в списке")
    def test_order_structure_in_list(self):
        """Проверка структуры заказа в списке"""
        response = requests.get(Endpoints.ORDERS)
        
        assert response.status_code == StatusCodes.OK
        
        orders = response.json()["orders"]
        assert isinstance(orders, list)
        
        # Проверяем, что список не пустой
        assert len(orders) > 0, "Список заказов пуст"
        
        # Проверяем структуру первого заказа
        order = orders[0]
        required_fields = [
            "id", "firstName", "lastName", "address", 
            "metroStation", "phone", "rentTime", 
            "deliveryDate", "track", "color", "status"
        ]
        
        for field in required_fields:
            assert field in order, f"Поле {field} отсутствует в заказе"