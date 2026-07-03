"""
Тестовые данные (для обратной совместимости)
"""

from utils.test_data import CourierData, OrderData, StatusCodes, Headers
from utils.error_messages import ErrorMessages
from utils.endpoints import Endpoints

# Экспортируем для обратной совместимости
__all__ = [
    'CourierData',
    'OrderData', 
    'StatusCodes',
    'Headers',
    'ErrorMessages',
    'Endpoints'
]