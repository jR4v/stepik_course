# импортируем необходимые компоненты
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# указываем ссылку на страницу, где будет происходить тестирование
link = "https://suninjuly.github.io/selects1.html"

# объявляем функцию для расчёта значения
def value(x, y):
    return int(x) + int(y)

try:
    browser = webdriver.Firefox() # запускаем браузер
    browser.get(link) # переходим по ссылке
    
    # находим элементы и получаем из них значения для подстановку в функцию
    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    
    sum = value(x, y) # присваиваем результат вычисления переменной        
            
    select = Select(browser.find_element(By.TAG_NAME, "select")) # находим и активируем раскрывающийся список
    select.select_by_value(str(sum)) # в списке выбираем соответсвующее значение
    
    # ищем на странице кнопку и нажатием отправляем решение
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    # вводим задержку, чтобы успеть скопировать полученный код-решение
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла (актуально при выполнении на Linux-системах)