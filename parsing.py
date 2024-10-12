from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv

driver = webdriver.Chrome()

# Откройте сайт
driver.get("https://divan.ru/category/divany-i-kresla")

# Время на загрузку страницы
time.sleep(5)  # Задержка для загрузки всех элементов страницы

# Создание CSV файла и запись заголовков
with open('sofa_prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Цена'])

    # Найдите элементы, содержащие информацию о диванах
    sofas = driver.find_elements(By.CLASS_NAME, '_Ud0k')
    # Итерация по найденным элементам
    for sofa in sofas:
        try:
            # Получение названия и цены

            price = sofa.find_element(By.CLASS_NAME, 'pY3d2').find_element(By.TAG_NAME, 'span').text
            print(f'Цена: {price}')

            # Запись в CSV файл
            writer.writerow([price])
        except Exception as e:
            print(f'Ошибка при извлечении данных: {e}')

# Закрытие браузера
driver.quit()