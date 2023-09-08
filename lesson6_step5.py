from selenium import webdriver
from selenium.webdriver.commom.by import By
import math

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Chrome()

try:
    browser.get(link)

    chislo = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    chislo.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Vitaly")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Marin")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Omsk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
