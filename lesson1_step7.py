from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
img = browser.find_element(By.CSS_SELECTOR, "[src='images/chest.png']")
x = img.get_attribute("valuex")
print(x)
y = calc(x)
answer = browser.find_element(By.ID, "answer")
answer.send_keys(y)
checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()
radio = browser.find_element(By.ID, "robotsRule")
radio.click()
# Отправляем заполненную форму
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()
