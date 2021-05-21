from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


# бъявляем метод для функции
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем значение для переменной х
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    s = calc(x)

    # ищем элемент и поднимаем его в верх для "прокрутки" скрытых элементов
    input1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(s)

    # находим и отмечаем необходимые поля
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка