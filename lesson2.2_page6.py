from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return math.log(abs(12*math.sin(int(x))))
  
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Firefox()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
       
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
        
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла