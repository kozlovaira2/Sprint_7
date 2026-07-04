"""
Вспомогательные утилиты для тестов
"""

from .urls import BASE_URL, API_VERSION
from .endpoints import Endpoints
from .test_data import CourierData, OrderData, StatusCodes, Headers, Users
from .error_messages import ErrorMessages

__all__ = [
    'BASE_URL',
    'API_VERSION',
    'Endpoints',
    'CourierData',
    'OrderData',
    'StatusCodes',
    'Headers',
    'Users',
    'ErrorMessages'
]