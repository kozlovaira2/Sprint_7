"""
Тестовые данные для API тестов
"""

import random
import string


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
    
    SUCCESS_CODES = [200, 201, 202, 204]
    CLIENT_ERROR_CODES = [400, 401, 403, 404, 409]
    SERVER_ERROR_CODES = [500, 502, 503, 504]


class CourierData:
    """Данные для тестирования курьеров"""
    
    # Базовые тестовые данные
    DEFAULT_LOGIN = "test_courier"
    DEFAULT_PASSWORD = "123456"
    DEFAULT_FIRST_NAME = "TestUser"
    
    # Невалидные данные
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
    
    @staticmethod
    def generate_courier_payload():
        """Генерация полных данных для создания курьера"""
        return {
            "login": CourierData.generate_random_login(),
            "password": CourierData.generate_random_password(),
            "firstName": CourierData.generate_random_first_name()
        }
    
    @staticmethod
    def get_valid_courier_data():
        """Получить валидные данные курьера"""
        return {
            "login": CourierData.DEFAULT_LOGIN,
            "password": CourierData.DEFAULT_PASSWORD,
            "firstName": CourierData.DEFAULT_FIRST_NAME
        }


class OrderData:
    """Данные для тестирования заказов"""
    
    # Базовые данные для заказа
    FIRST_NAME = "Test"
    LAST_NAME = "User"
    ADDRESS = "Test Address 123"
    METRO_STATION = 4
    PHONE = "+79001234567"
    RENT_TIME = 5
    DELIVERY_DATE = "2026-07-10"
    COMMENT = "Test comment"
    
    # Варианты цветов для параметризации
    COLOR_OPTIONS = [
        (["BLACK"], "black_only"),
        (["GREY"], "grey_only"),
        (["BLACK", "GREY"], "both_colors"),
        ([], "no_color")
    ]
    
    # Дополнительные варианты
    COLOR_BLACK = ["BLACK"]
    COLOR_GREY = ["GREY"]
    COLOR_BOTH = ["BLACK", "GREY"]
    COLOR_NONE = []
    
    @staticmethod
    def generate_order_payload(color=None):
        """Генерация данных для создания заказа"""
        payload = {
            "firstName": OrderData.FIRST_NAME,
            "lastName": OrderData.LAST_NAME,
            "address": OrderData.ADDRESS,
            "metroStation": OrderData.METRO_STATION,
            "phone": OrderData.PHONE,
            "rentTime": OrderData.RENT_TIME,
            "deliveryDate": OrderData.DELIVERY_DATE,
            "comment": OrderData.COMMENT
        }
        if color is not None:
            payload["color"] = color
        return payload
    
    @staticmethod
    def get_invalid_order_data():
        """Получить невалидные данные для заказа"""
        return {
            "firstName": "",  # Пустое имя
            "lastName": "User",
            "address": "Test",
            "metroStation": -1,  # Неверная станция
            "phone": "123",  # Неверный телефон
            "rentTime": 0,  # Некорректное время
            "deliveryDate": "2020-01-01",  # Прошлая дата
            "comment": ""
        }


class Users:
    """Тестовые данные для авторизации"""
    
    # Данные для проверки неверного логина/пароля
    data_negative = {
        "login": "invalid_user",
        "password": "wrong_password"
    }
    
    # Данные для проверки авторизации с пустым логином
    data_with_empty_login = {
        "login": "",
        "password": "123456"
    }
    
    # Данные для проверки авторизации с пустым паролем
    data_with_empty_password = {
        "login": "test_courier",
        "password": ""
    }


class Headers:
    """Заголовки HTTP запросов"""
    
    DEFAULT = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    AUTH_HEADER = "Authorization"
    CONTENT_TYPE = "Content-Type"
    ACCEPT = "Accept"
    
    @staticmethod
    def get_auth_header(token):
        """Получить заголовок авторизации"""
        return {Headers.AUTH_HEADER: f"Bearer {token}"}