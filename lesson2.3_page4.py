# импортируем необходимые компоненты
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# указываем ссылку на страницу, где будет происходить тестирование
link = "http://suninjuly.github.io/alert_accept.html"

# объявляем функцию для расчёта значения
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    browser = webdriver.Firefox() # запускаем браузер
    browser.get(link) # переходим по ссылке
    
    # поиск и нажатие кнопки
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    alert = browser.switch_to.alert # переключаем фокус на всплывающее окно
    alert.accept() # нажимаем кнопку во всплывающем окне
    
    # добавляем задержку, чтобы перед выполнением следующего действия успела прогрузиться страница
    time.sleep(1)
    
    x_element = browser.find_element(By.ID, "input_value") # поиск элемента, содержащего текстовое значение для переменной
    x = x_element.text # присваеваем текст из найденного элемента переменной
    y = calc(x) # объявляем переменную результату вычисления по функции
    
    # ищем текстовое поле и вставляем значение переменной «y»
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    
    # ищем на странице кнопку и нажатием отправляем ответ
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()  

finally:
    # вводим задержку, чтобы успеть скопировать полученный код-решение
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла (актуально при выполнении на Linux-системах)