"""
Базовые URL-адреса для API
"""

# Основные URL
BASE_URL = "https://qa-scooter.praktikum-services.ru"
API_VERSION = "/api/v1"

# Полные URL-адреса эндпоинтов
COURIER_URL = f"{BASE_URL}{API_VERSION}/courier"
COURIER_LOGIN_URL = f"{BASE_URL}{API_VERSION}/courier/login"
ORDERS_URL = f"{BASE_URL}{API_VERSION}/orders"
ORDER_TRACK_URL = f"{BASE_URL}{API_VERSION}/orders/track"
ACCEPT_ORDER_URL = f"{BASE_URL}{API_VERSION}/orders/accept"
CANCEL_ORDER_URL = f"{BASE_URL}{API_VERSION}/orders/cancel"
FINISH_ORDER_URL = f"{BASE_URL}{API_VERSION}/orders/finish"

# Методы API
HTTP_METHODS = {
    'GET': 'GET',
    'POST': 'POST',
    'PUT': 'PUT',
    'DELETE': 'DELETE',
    'PATCH': 'PATCH'
}