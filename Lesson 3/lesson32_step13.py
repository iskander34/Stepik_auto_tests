import unittest

class TestLearnUT(unittest.TestCase):
    def test_link1(self):

        from selenium import webdriver
        import time

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector("div.first_block div.form-group.first_class input.form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("div.first_block div.form-group.second_class input.form-control.second")
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_css_selector("div.first_block div.form-group.third_class input.form-control.third")
        input3.send_keys("ivan@ivanov.org")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Assert!")

    def test_link2(self):

        from selenium import webdriver
        import time

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector("div.first_block div.form-group.first_class input.form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("div.first_block div.form-group.second_class input.form-control.second")
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_css_selector("div.first_block div.form-group.third_class input.form-control.third")
        input3.send_keys("ivan@ivanov.org")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Assert!")

if __name__ == "__main__":
    unittest.main()