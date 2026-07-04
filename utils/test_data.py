"""
Тестовые данные для API тестов
"""

import random
import string
import requests

from utils.endpoints import Endpoints


class StatusCodes:
    """HTTP статус-коды"""
    
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    CONFLICT = 409
    INTERNAL_SERVER_ERROR = 500


class CourierData:
    """Данные для тестирования курьеров"""
    
    DEFAULT_LOGIN = "test_courier"
    DEFAULT_PASSWORD = "123456"
    DEFAULT_FIRST_NAME = "TestUser"
    
    INVALID_LOGIN = "invalid_user"
    INVALID_PASSWORD = "wrong_password"
    EMPTY_STRING = ""
    
    @staticmethod
    def generate_random_login():
        """Генерация случайного логина"""
        return ''.join(random.choices(string.ascii_lowercase, k=10))
    
    @staticmethod
    def generate_random_password():
        """Генерация случайного пароля"""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    
    @staticmethod
    def generate_random_first_name():
        """Генерация случайного имени"""
        return ''.join(random.choices(string.ascii_lowercase, k=8))


class OrderData:
    """Данные для тестирования заказов"""
    
    FIRST_NAME = "Test"
    LAST_NAME = "User"
    ADDRESS = "Test Address 123"
    METRO_STATION = 4
    PHONE = "+79001234567"
    RENT_TIME = 5
    DELIVERY_DATE = "2026-07-10"
    COMMENT = "Test comment"
    
    COLOR_OPTIONS = [
        (["BLACK"], "black_only"),
        (["GREY"], "grey_only"),
        (["BLACK", "GREY"], "both_colors"),
        ([], "no_color")
    ]
    
    @staticmethod
    def generate_order_payload(color=None):
        """Генерация данных для создания заказа"""
        return {
            "firstName": OrderData.FIRST_NAME,
            "lastName": OrderData.LAST_NAME,
            "address": OrderData.ADDRESS,
            "metroStation": OrderData.METRO_STATION,
            "phone": OrderData.PHONE,
            "rentTime": OrderData.RENT_TIME,
            "deliveryDate": OrderData.DELIVERY_DATE,
            "comment": OrderData.COMMENT,
            "color": color if color is not None else []
        }
    
    @staticmethod
    def create_order_request(color=None):
        """Отправляет запрос на создание заказа"""
        payload = OrderData.generate_order_payload(color)
        return requests.post(Endpoints.ORDERS, json=payload)


class Users:
    """Тестовые данные для авторизации"""
    
    data_negative = {
        "login": "invalid_user",
        "password": "wrong_password"
    }
    
    data_with_empty_login = {
        "login": "",
        "password": "123456"
    }
    
    data_with_empty_password = {
        "login": "test_courier",
        "password": ""
    }