"""
Эндпоинты API Яндекс Самокат
"""

from .urls import BASE_URL, API_VERSION

class Endpoints:
    """Класс с эндпоинтами API"""
    
    # Курьеры
    COURIER = f"{BASE_URL}{API_VERSION}/courier"
    COURIER_LOGIN = f"{BASE_URL}{API_VERSION}/courier/login"
    COURIER_ORDERS = f"{BASE_URL}{API_VERSION}/courier/orders"
    
    # Заказы
    ORDERS = f"{BASE_URL}{API_VERSION}/orders"
    ORDER_TRACK = f"{BASE_URL}{API_VERSION}/orders/track"
    
    @staticmethod
    def courier_by_id(courier_id):
        """Получить URL для курьера по ID"""
        return f"{BASE_URL}{API_VERSION}/courier/{courier_id}"
    
    @staticmethod
    def order_by_id(order_id):
        """Получить URL для заказа по ID"""
        return f"{BASE_URL}{API_VERSION}/orders/{order_id}"
    
    @staticmethod
    def order_by_track(track):
        """Получить URL для заказа по трек-номеру"""
        return f"{BASE_URL}{API_VERSION}/orders/track?t={track}"
    
    @staticmethod
    def courier_orders(courier_id):
        """Получить URL для заказов курьера"""
        return f"{BASE_URL}{API_VERSION}/courier/orders?courierId={courier_id}"
    
    @staticmethod
    def accept_order(order_id, courier_id):
        """Получить URL для принятия заказа"""
        return f"{BASE_URL}{API_VERSION}/orders/accept?orderId={order_id}&courierId={courier_id}"
    
    @staticmethod
    def cancel_order(order_id):
        """Получить URL для отмены заказа"""
        return f"{BASE_URL}{API_VERSION}/orders/cancel?orderId={order_id}"
    
    @staticmethod
    def finish_order(order_id):
        """Получить URL для завершения заказа"""
        return f"{BASE_URL}{API_VERSION}/orders/finish?orderId={order_id}"