# импортируем необходимые компоненты
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

main_link = "https://suninjuly.github.io/find_link_text" # указываем ссылку на страницу, где будет происходить тестирование  
link_text = str(math.ceil(math.pow(math.pi, math.e)*10000)) # объявляем переменную равную результату вычисления


try:
    browser = webdriver.Firefox() # запускаем браузер
    browser.get(link) # переходим по ссылке

    # находим ссылку с числом, равным значению переменной, и нажимаем
    link = browser.find_element(By.LINK_TEXT, link_text)
    link.click()
    
    # заполняем формы и отправляем
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
   # вводим задержку, чтобы успеть скопировать полученный код-решение
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла (актуально при выполнении на Linux-системах)