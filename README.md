# Sprint_7 - Тестирование API сервиса «Яндекс.Самокат»

## Описание проекта
Проект содержит автоматизированные тесты для API сервиса Яндекс Самокат (https://qa-scooter.praktikum-services.ru).  
Тесты покрывают основные сценарии работы с курьерами и заказами.

## Технологии
- Python 3.9+
- Selenium WebDriver
- pytest
- Allure
- Firefox

## Установка и запуск  
1) Перед работой с репозиторием необходимо установить зависимости:
``` shell
pip3 install -r requirements.txt
```
2) Для запуска всех тестов из директории tests можно использовать:
```shell
pytest tests/ -v --alluredir=allure_results 
```
3) Посмотреть отчет Allure в веб версии по запущенным тестам:
``` shell
allure serve allure_results
```

## Что проверяется  

#### Создание курьера (`test_create_courier.py`)

| Тест | Описание |
|------|----------|
| `test_create_courier_success` | Успешное создание курьера |
| `test_create_duplicate_courier_error` | Ошибка при создании дублирующего курьера |
| `test_create_courier_missing_fields` | Ошибка при отсутствии обязательных полей |
| `test_create_courier_existing_login` | Ошибка при использовании существующего логина |
| `test_create_courier_success_response` | Проверка формата успешного ответа |

#### Авторизация курьера (`test_login_courier.py`)

| Тест | Описание |
|------|----------|
| `test_courier_log_in` | Успешная авторизация |
| `test_courier_log_negative` | Ошибка при неверном логине или пароле |
| `test_courier_log_with_empty_login` | Ошибка при авторизации с пустым логином |
| `test_courier_log_with_empty_password` | Ошибка при авторизации с пустым паролем |

#### Создание заказа (`test_create_order.py`)

| Тест | Описание |
|------|----------|
| `test_create_order_success` | Успешное создание заказа |
| `test_create_order_with_colors` | Создание заказа с разными цветами |
| `test_create_order_without_color` | Создание заказа без указания цвета |
| `test_create_order_track_number` | Проверка корректности track-номера |

#### Список заказов (`test_orders_list.py`)

| Тест | Описание |
|------|----------|
| `test_get_orders_list` | Получение списка заказов |
| `test_order_structure_in_list` | Проверка структуры заказа в списке |


## Структура проекта  
 
tests/ — тесты создания курьера, создания заказа, авторизации курьера, списка заказов 
utils/ — вспомогательные модули 
helpers.py - вспомогательные функции 
conftest.py — фикстуры  
data.py — тестовые данные   
allure-report/ — cгенерированный Allure-отчёт