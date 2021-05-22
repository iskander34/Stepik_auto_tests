from selenium import webdriver
import time
import math


# объявляем метод для функции
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим и нажимаем кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # переходим на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # считываем значение для переменной х
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    s = calc(x)

    # находим поле для ответа и вставляем посчитанный ответ
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(s)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка