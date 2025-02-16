import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class AvitoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.service = Service(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.get("http://tech-avito-intern.jumpingcrab.com/")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_create_advertisement(self):
        """Тест на создание объявления"""
        create_button = self.driver.find_element(By.XPATH, "//button[text()='Создать']")
        create_button.click()

        self.driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Компьютер")
        self.driver.find_element(By.XPATH, "//input[@name='price']").send_keys("100000")
        self.driver.find_element(By.XPATH, "//input[@name='description']").send_keys("Игровой компьютер")
        self.driver.find_element(By.XPATH, "//input[@name='imageUrl']").send_keys("https://i.pinimg.com/736x/50/7d/b6/507db6131a8e4eedf75cb783fe97c456.jpg")

        time.sleep(1)
        save_button = self.driver.find_element(By.XPATH, "//button[text()='Сохранить']")
        save_button.click()

        time.sleep(2)
        self.assertTrue(self.driver.find_element(By.XPATH, "//div[contains(text(), 'Компьютер')]"))

    def test_edit_advertisement(self):
        """Тест на редактирование объявления"""
        ad_selection = self.driver.find_element(By.CSS_SELECTOR, ".css-1w07v7s > .css-1cickmn:first-child > a")
        time.sleep(2)
        ad_selection.click()

        time.sleep(1)
        edit_ad = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div.chakra-container.css-1lle71m > div > div.css-nb383z > svg")
        edit_ad.click()

        time.sleep(1)
        image_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='imageUrl']")
        image_field.clear()
        image_field.send_keys("url(Picture)")

        name_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='name']")
        name_field.clear()
        name_field.send_keys("Подушка")

        price_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='price']")
        price_field.clear()
        price_field.send_keys("1337")

        description_field = self.driver.find_element(By.CSS_SELECTOR, "textarea[name='description']")
        description_field.clear()
        description_field.send_keys("Очень мягкая подушенция")

        time.sleep(1)
        confirm_button = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div.chakra-container.css-1lle71m > div > div.css-nb383z > svg")
        time.sleep(2)
        confirm_button.click()

        time.sleep(2)
        self.driver.get("http://tech-avito-intern.jumpingcrab.com/")

    def test_search_advertisement(self):
        """Тест на поиск объявления"""
        search_field = self.driver.find_element(By.CSS_SELECTOR, "input.chakra-input.css-1owg1hr")
        search_field.send_keys("Компьютер")

        search_button = self.driver.find_element(By.CSS_SELECTOR, "button.chakra-button.css-1oamcjg")
        time.sleep(2)
        search_button.click()

        time.sleep(2)
        self.assertTrue(self.driver.find_element(By.XPATH, "//div[contains(text(), 'Компьютер')]"))

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
