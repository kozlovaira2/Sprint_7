"""
Вспомогательные функции для тестов
"""

import random
import string
import requests

from utils.urls import BASE_URL
from utils.test_data import CourierData
from utils.endpoints import Endpoints

def generate_random_string(length):
    """Генерирует случайную строку из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def register_new_courier_and_return_login_password():
    """Регистрирует нового курьера и возвращает список [login, password, first_name]"""
    login_pass = []
    
    # Используем данные из utils
    login = CourierData.generate_random_login()
    password = CourierData.generate_random_password()
    first_name = CourierData.generate_random_first_name()
    
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    
    response = requests.post(Endpoints.COURIER, data=payload)
    
    if response.status_code == 201:
        login_pass.extend([login, password, first_name])
    
    return login_pass

def get_courier_id(login, password):
    """Получает ID курьера по логину и паролю"""
    response = requests.post(
        Endpoints.COURIER_LOGIN,
        data={"login": login, "password": password}
    )
    if response.status_code == 200:
        return response.json().get("id")
    return None

def delete_courier(courier_id):
    """Удаляет курьера по ID"""
    if courier_id:
        requests.delete(Endpoints.courier_by_id(courier_id))

def generate_order_payload(color=None):
    """Генерирует данные для создания заказа"""
    from utils.test_data import OrderData
    return OrderData.generate_order_payload(color)