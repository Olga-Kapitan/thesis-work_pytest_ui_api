from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import allure
from time import sleep


@allure.epic("KinopoiskUI")
@allure.severity("blocker")
class KinopoickUI:

    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.kinopoisk.ru/"
        self.__driver = driver

    @allure.step("UI. Перейти на страницу расширенного поиска")
    def advanced_search(self):
        """ Осуществляет переход на страницу с расширенным поиском"""
        self.__driver.get(self.__url)
        self.__driver.find_element(
            By.CSS_SELECTOR, '[aria-label="Расширенный поиск"]').click()

    @allure.step("UI. Заполнить основную форму поиска фильма")
    def fill_form_search_main(self, title: str, year: str, country: str, genre: str):
        """ Заполнение основной формы поиска

            Принимает параметры: title - название фильма,
            year - год выпуска фильма,
            country - страна,
            genre - жанр

        """
        self.__driver.find_element(
            By.CSS_SELECTOR, "#find_film").send_keys(title)
        self.__driver.find_element(By.CSS_SELECTOR, "#year").send_keys(year)
        Select(self.__driver.find_element(
            By.CSS_SELECTOR, "#country")).select_by_visible_text(country)
        self.__driver.execute_script("window.scrollBy(0, 350)")
        Select(self.__driver.find_element(
            By.XPATH, ".//*[@id='m_act[genre]']")).select_by_visible_text(genre)
        self.__driver.find_element(
            By.CSS_SELECTOR, "input[class='el_18 submit nice_button']").click()

    @allure.step("UI. Заполнить форму поиска фильма по создателям")
    def fill_form_search_by_creators(self, select_cr1, creators1: str, select_cr2, creators2=''):
        """ Заполнение формы поиска по создателям.
        
            Принимает параметры: select_cr1/select_cr2 - выбор кинопрофессии,
            creators1/creators2 - имя человека к професии
        """
        sleep(5)
        self.__driver.execute_script("window.scrollBy(0, 500)")
        sleep(5)
        Select(self.__driver.find_element(
            By.CSS_SELECTOR, "#cr_search_field_1_select")).select_by_visible_text(select_cr1)
        self.__driver.find_element(
            By.CSS_SELECTOR, "#cr_search_field_1").send_keys(creators1)
        Select(self.__driver.find_element(
            By.CSS_SELECTOR, "#cr_search_field_2_select")).select_by_visible_text(select_cr2)
        self.__driver.find_element(
            By.CSS_SELECTOR, "#cr_search_field_2").send_keys(creators2)
        sleep(5)
        self.__driver.find_element(
            By.CSS_SELECTOR, "input#btn_search_6").click()
        sleep(5)

    @allure.step("UI. Заполнить форму поиска информации по создателям")
    def search_info_creators(self, name: str):
        """ Заполнение формы поиска информации кинозвезд
        
            Принимает параметр имя кинозвезды
        """
        sleep(2)
        self.__driver.execute_script("window.scrollBy(0, 1000)")
        self.__driver.find_element(
            By.CSS_SELECTOR, "#find_people").send_keys(name)
        self.__driver.find_element(
            By.CSS_SELECTOR, "input[class='el_8 submit nice_button']").click()

    @allure.step("UI. Заполнить форму поиска по ключевому слову")
    def search_fiml_by_word(self, word1: str):
        """ Заполнение формы поиска по ключевому слову.
        
            Принимает параметр слово для поиска.
        """
        self.__driver.execute_script("window.scrollBy(0, 1200)")
        self.__driver.find_element(
            By.CSS_SELECTOR, "#find_keyword").send_keys(word1)
        self.__driver.find_element(
            By.CSS_SELECTOR, "#keyword_search>input.submit.nice_button").click()

    @allure.step("UI. Заполнить форму поиска по студии производителю")
    def search_by_studios(self, studios: str):
        """ Заполнение формы для поиска студий произодителей.
        
            Принимает параметр название студии производителя
        """
        self.__driver.execute_script("window.scrollBy(0, 2000)")
        self.__driver.find_element(
            By.CSS_SELECTOR, "#find_studio").send_keys(studios)
        self.__driver.find_element(
            By.CSS_SELECTOR, "#studio_search>input.submit.nice_button").click()
