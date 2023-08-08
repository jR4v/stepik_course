# импортируем необходимые компоненты
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# указываем ссылку на страницу, где будет происходить тестирование
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Firefox() # запускаем браузер
    browser.get(link) # переходим по ссылке

    # input* — поиск и подстановка значений в текстовые поля
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("John")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Doe")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("john@doe.name")
    
    file_input = browser.find_element(By.NAME, "file") # находим форму прикрепления файла
    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'lesson2.2_page8_file.txt') # добавляем к пути имя файла 
    file_input.send_keys(file_path) # прикрепляем файл
    
    # ищем на странице кнопку и нажатием отправляем файл
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # вводим задержку, чтобы успеть скопировать полученный код-решение
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла (актуально при выполнении на Linux-системах)