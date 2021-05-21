from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


#бъявляем метод для суммирования
def calc(x, y):
  return str(int(x)+int(y))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем значение для переменной х
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    # считываем значение для переменной y
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    # вызываем метод для суммирования
    s = calc(x, y)

    # используем специальный класс Select из библиотеки WebDriver
    # инициализируем новый объект, передав в него WebElement с тегом Select
    # ищем вариант из списка с помощью метода select_by_value(value)
    # это лучше  вверх (как и сделал)from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(s)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка