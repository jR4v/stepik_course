# импортируем необходимые компоненты
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# указываем ссылку на страницу, где будет происходить тестирование  
link = "http://suninjuly.github.io/explicit_wait2.html"

# объявляем функцию для расчёта значения
def calc(x):
  return math.log(abs(12*math.sin(int(x))))

try:
    browser = webdriver.Firefox() # запускаем браузер
    browser.get(link) # переходим по ссылке
    
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    
    book = browser.find_element(By.ID, "book")
    book.click()
    
    x_element = browser.find_element(By.ID, "input_value") # поиск элемента, содержащего текстовое значение для переменной
    x = x_element.text # присваеваем текст из найденного элемента переменной
    y = calc(x) # объявляем переменную результату вычисления по функции
    
    # ищем текстовое поле и вставляем значение переменной «y»
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    
    # ищем на странице кнопку и нажатием отправляем ответ
    button = browser.find_element(By.ID, "solve")
    button.click()
    
finally:
    # вводим задержку, чтобы успеть скопировать полученный код-решение
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла (актуально при выполнении на Linux-системах)
    