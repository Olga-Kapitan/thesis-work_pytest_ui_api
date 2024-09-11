from Pages.api_class import KinopoiskApi
import allure
import pytest


api_poisk = KinopoiskApi("https://api.kinopoisk.dev/")

@allure.epic("KinopoiskApi")
@allure.severity("blocker")
@allure.id("Kinopoisk - 1")
@allure.story("Поиск информации о фильмах и актерах")
@allure.feature("READ")
@allure.title("Получение фильма по названию")
@pytest.mark.api_tests
def test_search_film_by_name():
    with allure.step("Получить фильм через Api"):
        responce = api_poisk.search_film_by_name(1, 1, 'The Gentlemen')
        body = responce.json()['docs'][0]
    with allure.step("Проверить статус код ответа через Api"):
        assert responce.status_code == 200
    with allure.step("Проверить корректность данных через Api"):
        assert body['alternativeName'] == 'The Gentlemen'


@allure.epic("KinopoiskApi")
@allure.severity("blocker")
@allure.id("Kinopoisk - 2")
@allure.story("Поиск информации о фильмах и актерах")
@allure.feature("READ")
@allure.title("Получение фильма по id-фильма")
@pytest.mark.api_tests
def test_search_film_by_id():
    with allure.step("Получить id фильма через Api"):
        id_film = api_poisk.search_film_by_name(
            1, 1, 'The Gentlemen')['docs'][0]['id']
    with allure.step("Получить фильм по {id_film} через Api"):
        body = api_poisk.search_film_by_id(id_film)
    with allure.step("Проверить данные через Api"):
        assert body['name'] == 'Джентльмены'


@allure.epic("KinopoiskApi")
@allure.severity("blocker")
@allure.id("Kinopoisk - 3")
@allure.story("Поиск информации о фильмах и актерах")
@allure.feature("READ")
@allure.title("Получение актера по имени")
@pytest.mark.api_tests
def test_search_actor_by_name():
    with allure.step("Получить актера через Api"):
        actor = api_poisk.search_actor_by_name(1, 1, 'Дэниэл Рэдклифф')['docs'][0]
    with allure.step("Проверить корректность данных через Api"):
        assert actor['enName'] == 'Daniel Radcliffe'
        assert actor['sex'] == 'Мужской'


@allure.epic("KinopoiskApi")
@allure.severity("blocker")
@allure.id("Kinopoisk - 4")
@allure.story("Поиск информации о фильмах и актерах")
@allure.feature("READ")
@allure.title("Получение фильма по фильтрам")
@pytest.mark.api_tests
def test_free_search_film():
    with allure.step("Получить id актера через Api"):
        id_actor = api_poisk.search_actor_by_name(
            1, 1, 'Дэниэл Рэдклифф')['docs'][0]['id']
    with allure.step("Получить фильм по нескольким параметрам через Api"):
        list_film = api_poisk.free_search_film(
            'name', '2001-2011', 'США', 'фэнтези', id_actor)
        one_film = list_film['docs'][4]
    with allure.step("Проверить корректность данных через Api"):
        assert one_film['name'] == 'Гарри Поттер и философский камень'


@allure.epic("KinopoiskApi")
@allure.severity("blocker")
@allure.id("Kinopoisk - 5")
@allure.story("Поиск информации о фильмах и актерах")
@allure.feature("READ")
@allure.title("Получение актера по id")
@pytest.mark.api_tests
def test_search_actor_by_id():
    with allure.step("Получить id актера через Api"):
        id_actor = api_poisk.search_actor_by_name(
            1, 1, 'Дэниэл Рэдклифф')['docs'][0]['id']
    with allure.step("Получить актера по {id_actor} через Api"):
        info_actor = api_poisk.search_actor_by_id(id_actor)
    with allure.step("Проверить корректность данных через Api"):
        assert info_actor['name'] == 'Дэниэл Рэдклифф'
        assert info_actor['id'] == id_actor
