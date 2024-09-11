from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure


class Check:

    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step("UI. Проверка названия фильма основного поиска")
    def check_title_search_main(self):
        """ Возвращает название найденного фильма
            при основном поиске
        """
        return self.__driver.find_element(By.CSS_SELECTOR, "div>h1>span").text

    @allure.step("UI. Проверка названия фильма по создателям")
    def check_title_film_by_creators(self):
        """ Возвращает название найденного фильма
            при поиске по создателям
        """
        return self.__driver.find_element(By.CSS_SELECTOR, "p.name").text

    @allure.step("UI. Проверка имени актера")
    def check_title_creators(self):
        """ Возвращает имя актера
            при поиске информации о создателях
        """
        return self.__driver.find_element(By.CSS_SELECTOR, "h1").text

    @allure.step("UI. Проверка слова для поиска")
    def check_word(self):
        """ Возвращает написанное слово для поиска"""
        return self.__driver.find_element(By.CSS_SELECTOR, "td.news").text

    @allure.step("UI. Проверка названии студии производителя")
    def check_title_studios(self):
        """ Возвращает название студии производителя"""
        return self.__driver.find_element(
            By.CSS_SELECTOR, "td.news>a.all").text
