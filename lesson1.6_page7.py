# импортируем необходимые компоненты
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Firefox() # запуск браузера
    browser.get("http://suninjuly.github.io/huge_form.html") # переход по ссылке
    
    # находим все поля с тегом «input» и с помощью цикла заполняем
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("—")
    
    # отправляем форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла (актуально при выполнении на Linux-системах)