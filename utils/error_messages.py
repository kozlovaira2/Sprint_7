"""
Сообщения об ошибках API
"""

class ErrorMessages:
    """Сообщения об ошибках API"""
    
    # Ошибки курьеров
    MISSING_FIELD = "Недостаточно данных для создания учетной записи"
    COURIER_EXISTS = "Этот логин уже используется. Попробуйте другой."
    AUTH_FAILED = "Учетная запись не найдена"
    MISSING_AUTH_FIELDS = "Недостаточно данных для входа"
    
    # Ошибки заказов
    ORDER_NOT_FOUND = "Заказ не найден"
    ORDER_ALREADY_TAKEN = "Заказ уже взят"
    INVALID_ORDER_DATA = "Неверные данные заказа"
    
    # Общие ошибки
    UNAUTHORIZED = "Требуется авторизация"
    FORBIDDEN = "Доступ запрещен"
    INTERNAL_ERROR = "Внутренняя ошибка сервера"
    
    @staticmethod
    def get_all_messages():
        """Получить все сообщения об ошибках"""
        return [
            ErrorMessages.MISSING_FIELD,
            ErrorMessages.COURIER_EXISTS,
            ErrorMessages.AUTH_FAILED,
            ErrorMessages.MISSING_AUTH_FIELDS,
            ErrorMessages.ORDER_NOT_FOUND,
            ErrorMessages.ORDER_ALREADY_TAKEN,
            ErrorMessages.INVALID_ORDER_DATA
        ]