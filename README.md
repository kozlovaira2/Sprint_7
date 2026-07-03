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
| `test_login_courier_success` | Успешная авторизация |
| `test_login_courier_missing_password` | Ошибка при авторизации без пароля |
| `test_login_courier_missing_login` | Ошибка при авторизации без логина |
| `test_login_courier_invalid_login` | Ошибка при неверном логине |
| `test_login_courier_invalid_password` | Ошибка при неверном пароле |
| `test_login_nonexistent_courier` | Ошибка при авторизации несуществующего пользователя |

#### Создание заказа (`test_create_order.py`)

| Тест | Описание |
|------|----------|
| `test_create_order_success` | Успешное создание заказа |
| `test_create_order_with_colors` | Создание заказа с разными цветами (параметризованный) |
| `test_create_order_without_color` | Создание заказа без указания цвета |
| `test_create_order_track_number` | Проверка корректности track-номера |

#### Список заказов (`test_orders_list.py`)

| Тест | Описание |
|------|----------|
| `test_get_orders_list` | Получение списка заказов |
| `test_order_structure_in_list` | Проверка структуры заказа в списке |


## Структура проекта  
Sprint_7/
├── pages/                          # Page Object Model
│   ├── __init__.py
│   ├── base_page.py                # Базовая страница (общие методы)
│   ├── main_page.py                # Главная страница
│   ├── order_page.py               # Страница заказа
│   ├── order_status_page.py        # Страница статуса заказа
│   └── dzen_page.py                # Страница Дзена
├── tests/                          # Тесты
│   ├── __init__.py
│   ├── test_order_flow.py          # Тесты оформления заказа
│   ├── test_order_status.py        # Тесты проверки статуса заказа
│   └── test_navigation.py          # Тесты навигации
├── utils/                          # Вспомогательные модули
│   ├── __init__.py
│   ├── urls.py                     # URL-адреса
│   ├── test_data.py                # Тестовые данные
│   └── helpers.py                  # Вспомогательные функции
├── allure_results/                 # Результаты тестов для Allure
├── conftest.py                     # Фикстуры pytest
├── data.py                         # Тестовые данные (обратная совместимость)
├── requirements.txt                # Зависимости проекта
├── .gitignore                      # Игнорируемые файлы
└── README.md                       # Документация проекта# Sprint_7
