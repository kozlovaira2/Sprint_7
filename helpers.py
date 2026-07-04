"""
Вспомогательные функции для тестов
"""

import random
import string
import requests

from utils.endpoints import Endpoints
from utils.test_data import CourierData


def generate_random_string(length):
    """Генерирует случайную строку из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def generate_courier_data():
    """Генерирует данные для курьера без создания"""
    login = CourierData.generate_random_login()
    password = CourierData.generate_random_password()
    first_name = CourierData.generate_random_first_name()
    return login, password, first_name


def create_courier_request(login, password, first_name):
    """Отправляет запрос на создание курьера"""
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return requests.post(Endpoints.COURIER, data=payload)


def login_courier_request(login, password):
    """Отправляет запрос на авторизацию курьера"""
    payload = {"login": login, "password": password}
    return requests.post(Endpoints.COURIER_LOGIN, data=payload)


def delete_courier(courier_id):
    """Удаляет курьера по ID"""
    requests.delete(Endpoints.courier_by_id(courier_id))