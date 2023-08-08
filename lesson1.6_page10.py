# импортируем необходимые компоненты
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    # указываем ссылку на страницу, где будет происходить тестирование  
    link = "https://suninjuly.github.io/registration2.html"
    
    browser = webdriver.Firefox() # запускаем браузер
    browser.get(link) # переходим по ссылке

    # находим и заполняем поля
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input3.send_keys("ivb@none.com")
    input4 = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
    input4.send_keys("999888")
    input5 = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
    input5.send_keys("Adress Unknown")
    
    # отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную «welcome_text» текст из элемента «welcome_text_elt»
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
# не забываем оставить пустую строку в конце файла (актуально при выполнении на Linux-системах)