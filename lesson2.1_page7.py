# импортируем необходимые компоненты
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

# объявляем функцию для расчёта значения
def calc(x):
  return math.log(abs(12*math.sin(int(x))))

# указываем ссылку на страницу, где будет происходить тестирование    
link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Firefox() # запускаем браузер
    browser.get(link) # переходим по ссылке

    x_element = browser.find_element(By.ID, "treasure") # поиск элемента, содержащего текстовое значение для переменной
    x = x_element.get_attribute("valuex") # получение текстового значения из аттрибута
    y = calc(x) # объявляем переменную результату вычисления по функции

    # ищем текстовое поле и вставляем значение переменной «y»
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    
    # находим и активируем чекбокс
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    
    # находим и активируем радиокнопку
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    
    # находим и нажимаем кнопку отправки решения
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # вводим задержку, чтобы успеть скопировать полученный код-решение
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла (актуально при выполнении на Linux-системах)