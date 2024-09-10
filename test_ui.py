from Pages.ui_class import KinopoickUI
from Pages.ui_check import Check
import pytest
import allure


@allure.id("Kinopoisk - UI - 1")
@allure.story("Расширенный поиск информации о фильмах и актерах")
@allure.feature("READ")
@allure.title("Получение фильма по основному поиску")
@pytest.mark.ui_tests
def test_search_main(chrome_browser):
    ui_poisk = KinopoickUI(chrome_browser)
    with allure.step("Перейти на страницу с расширенным поиском"):
        ui_poisk.advanced_search()
    with allure.step("Получить фильм по основному поиску. UI"):
        ui_poisk.fill_form_search_main('Джентльмены', '2019', 'США', 'криминал')
    with allure.step("Получить название фильма. UI"):
        title_che = Check(chrome_browser)
        title = title_che.check_title_search_main()
    with allure.step("Проверить корректность данных. UI"):
        assert 'Джентльмены' in title


@allure.id("Kinopoisk - UI - 2")
@allure.story("Расширенный поиск информации о фильмах и актерах")
@allure.feature("READ")
@allure.title("Получение фильма по создателям")
@pytest.mark.ui_tests
@pytest.mark.xfail
def test_search_by_creators(chrome_browser):
    ui_poisk = KinopoickUI(chrome_browser)
    with allure.step("Перейти на страницу с расширенным поиском"):
        ui_poisk.advanced_search()
    with allure.step("Получить фильм по создателям. UI"):
        ui_poisk.fill_form_search_by_creators(
            'Актер', 'Мэттью Макконахи', 'Режиссер', 'Гай Ричи')
    with allure.step("Получить название фильма. UI"):
        title_che = Check(chrome_browser)
        title = title_che.check_title_film_by_creators()
    with allure.step("Проверить корректность данных. UI"):
        assert 'Джентльмены' in title


@allure.id("Kinopoisk - UI - 3")
@allure.story("Расширенный поиск информации о фильмах и актерах")
@allure.feature("READ")
@allure.title("Получение информации о создателе")
@pytest.mark.ui_tests
def test_search_info_creators(chrome_browser):
    ui_poisk = KinopoickUI(chrome_browser)
    with allure.step("Перейти на страницу с расширенным поиском"):
        ui_poisk.advanced_search()
    with allure.step("Получить информацию по кинозвезде. UI"):
        ui_poisk.search_info_creators('Мэттью Макконахи')
    with allure.step("Получить имя кинозвезды. UI"):
        title_che = Check(chrome_browser)
        title = title_che.check_title_creators()
    with allure.step("Проверить корректность данных. UI"):
        assert 'Мэттью Макконахи' in title


@allure.id("Kinopoisk - UI - 4")
@allure.story("Расширенный поиск информации о фильмах и актерах")
@allure.feature("READ")
@allure.title("Получение фильма по ключевому слову")
@pytest.mark.ui_tests
def test_search_fiml_by_word(chrome_browser):
    ui_poisk = KinopoickUI(chrome_browser)
    with allure.step("Перейти на страницу с расширенным поиском"):
        ui_poisk.advanced_search()
    with allure.step("Получить фильмы по ключевому слову. UI"):
        ui_poisk.search_fiml_by_word('Енот')
    with allure.step("Получить введенное слово. UI"):
        title_che = Check(chrome_browser)
        title = title_che.check_word()
    with allure.step("Проверить корректность данных. UI"):
        assert 'Енот' in title


@allure.id("Kinopoisk - UI - 5")
@allure.story("Расширенный поиск информации о фильмах и актерах")
@allure.feature("READ")
@allure.title("Получение информации по студии производителю")
@pytest.mark.ui_tests
def test_search_by_studios(chrome_browser):
    ui_poisk = KinopoickUI(chrome_browser)
    with allure.step("Перейти на страницу с расширенным поиском"):
        ui_poisk.advanced_search()
    with allure.step("Получить название студии. UI"):
        ui_poisk.search_by_studios("Walt Disney Pictures")
    with allure.step("Получить студию произодителя. UI"):
        title_che = Check(chrome_browser)
        title = title_che.check_title_studios()
    with allure.step("Проверить корректность данных. UI"):
        assert "Walt Disney Pictures" in title
