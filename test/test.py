import requests
import logging

url = "http://localhost:8000/get_form"
logging.basicConfig(level=logging.INFO)

logging.info("Тест 1. Совпали все поля и типы данных")
response = requests.post(
    url,
    json={
        "field_name_1": "ivan@mail.ru", "field_name_2": "+79999999999", "field_name_3": "07.12.2024"
    })
logging.info(f"Ожидание: название шаблона. Результат тестирования: {response.json()}")

logging.info("Тест 2. Совпали все поля и тип данных, но в запросе меньше на один элемент")
response = requests.post(
    url,
    json={
        "field_name_1": "ivan@mail.ru", "field_name_3": "2024-12-07"
    })
logging.info(f"Ожидание: название шаблона. Результат тестирования: {response.json()}")

logging.info('Тест 3. Совпали все поля, ошибка в валидации "phone": отсутствует символ "+"')
response = requests.post(
    url,
    json={
        "field_name_1": "ivan@mail.ru", "field_name_2": "79999999999", "field_name_3": "07.12.2024"
    })
logging.info(f"Ожидание: возврат json с валидированными типами данных. Результат тестирования: {response.json()}")

logging.info('Тест 4. Совпали все поля, ошибка в валидации "phone": превышено количество цифр в номере')
response = requests.post(
    url,
    json={
        "field_name_1": "ivan@mail.ru", "field_name_2": "+799999999999", "field_name_3": "07.12.2024"
    })
logging.info(f"Ожидание: возврат json с валидированными типами данных. Результат тестирования: {response.json()}")

logging.info('Тест 5. Совпали все поля, ошибка в валидации "email": отсутствует "@"')
response = requests.post(
    url,
    json={
        "field_name_1": "ivanmail.ru", "field_name_2": "+79999999999", "field_name_3": "07.12.2024"
    })
logging.info(f"Ожидание: возврат json с валидированными типами данных. Результат тестирования: {response.json()}")

logging.info('Тест 6. Совпали все поля, ошибка в валидации "email": отсутствует "."')
response = requests.post(
    url,
    json={
        "field_name_1": "ivan@mail,ru", "field_name_2": "+79999999999", "field_name_3": "07.12.2024"
    })
logging.info(f"Ожидание: возврат json с валидированными типами данных. Результат тестирования: {response.json()}")

logging.info('Тест 7. Совпали все поля, ошибка в валидации "даты": формат "2021 01 01"')
response = requests.post(
    url,
    json={
        "field_name_1": "ivan@mail,ru", "field_name_2": "+79999999999", "field_name_3": "2024 12 07"
    })
logging.info(f"Ожидание: возврат json с валидированными типами данных. Результат тестирования: {response.json()}")
