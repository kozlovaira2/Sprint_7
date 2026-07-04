"""
Тесты для создания заказа
"""

import pytest
import allure

from utils.test_data import OrderData, StatusCodes


@allure.epic("Заказы")
@allure.feature("Создание заказа")
class TestCreateOrder:
    
    @allure.title("Создание заказа - успешный сценарий")
    def test_create_order_success(self):
        """Проверка успешного создания заказа"""
        response = OrderData.create_order_request()
        
        assert response.status_code == StatusCodes.CREATED
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)

    @allure.title("Создание заказа с разными вариантами цвета")
    @pytest.mark.parametrize("color, color_name", OrderData.COLOR_OPTIONS)
    def test_create_order_with_colors(self, color, color_name):
        """Параметризованный тест создания заказа с цветами"""
        with allure.step(f"Создание заказа с цветами: {color_name}"):
            response = OrderData.create_order_request(color)
            
            assert response.status_code == StatusCodes.CREATED
            assert "track" in response.json()

    @allure.title("Создание заказа без указания цвета")
    def test_create_order_without_color(self):
        """Проверка создания заказа без указания цвета"""
        response = OrderData.create_order_request()
        
        assert response.status_code == StatusCodes.CREATED
        assert "track" in response.json()

    @allure.title("Проверка корректности track-номера в ответе")
    def test_create_order_track_number(self):
        """Проверка, что track - это положительное число"""
        response = OrderData.create_order_request()
        
        assert response.status_code == StatusCodes.CREATED
        track = response.json()["track"]
        assert track > 0
        assert isinstance(track, int)