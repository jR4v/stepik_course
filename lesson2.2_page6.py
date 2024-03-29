# импортируем необходимые компоненты
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

# объявляем функцию для расчёта значения
def calc(x):
  return math.log(abs(12*math.sin(int(x))))
  
# указываем ссылку на страницу, где будет происходить тестирование  
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Firefox() # запускаем браузер
    browser.get(link) # переходим по ссылке

    x_element = browser.find_element(By.ID, "input_value") # поиск элемента, содержащего текстовое значение для переменной
    x = x_element.text # присваеваем текст из найденного элемента переменной
    y = calc(x) # объявляем переменную результату вычисления по функции
    
    radio = browser.find_element(By.ID, "robotsRule") # находим радиокнопку
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio) # прокручиваем страницу, чтобы радиокнопка показалась на экране
    radio.click() # активируем радиокнопку
    
    # ищем текстовое поле и вставляем значение переменной «y»
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
       
    # находим и активируем чекбокс
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    
    # находим кнопку, прокручиваем страницу, чтобы кнопка оказалась на экране, нажимаем кнопку
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # вводим задержку, чтобы успеть скопировать полученный код-решение
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла (актуально при выполнении на Linux-системах)