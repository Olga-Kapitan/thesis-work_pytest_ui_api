from Pages.api_class import KinopoiskApi
import allure
import pytest

api_poisk = KinopoiskApi("https://api.kinopoisk.dev/")

@allure.id("Kinopoisk - 1")
@allure.story("Поиск информации о фильмах и актерах")
@allure.feature("READ")
@allure.title("Получение фильма по названию")
@pytest.mark.api_tests
# @pytest.mark.parametrize()
def test_search_film_by_name():
    body = api_poisk.search_film_by_name(1, 1, 'The Gentlemen')['docs'][0]
    assert body['alternativeName'] == 'The Gentlemen'


@allure.id("Kinopoisk - 2")
@allure.story("Поиск информации о фильмах и актерах")
@allure.feature("READ")
@allure.title("Получение фильма по id-фильма")
@pytest.mark.api_tests
def test_search_film_by_id():
    id_film = api_poisk.search_film_by_name(1, 1, 'The Gentlemen')['docs'][0]['id']
    body = api_poisk.search_film_by_id(id_film)
    assert body['name'] == 'Джентльмены'


@allure.id("Kinopoisk - 3")
@allure.story("Поиск информации о фильмах и актерах")
@allure.feature("READ")
@allure.title("Получение актера по имени")
@pytest.mark.api_tests
def test_search_actor_by_name():
    actor = api_poisk.search_actor_by_name(1, 1, 'Дэниэл Рэдклифф')['docs'][0]
    assert actor['enName'] == 'Daniel Radcliffe'
    assert actor['sex'] == 'Мужской'


@allure.id("Kinopoisk - 4")
@allure.story("Поиск информации о фильмах и актерах")
@allure.feature("READ")
@allure.title("Получение фильма по фильтрам")
@pytest.mark.api_tests
def test_free_search_film():
    id_actor = api_poisk.search_actor_by_name(1, 1, 'Дэниэл Рэдклифф')['docs'][0]['id']
    list_film = api_poisk.free_search_film('name', '2001-2011', 'США', 'фэнтези', id_actor)
    one_film = list_film['docs'][4]
    assert one_film['name'] == 'Гарри Поттер и философский камень'


@allure.id("Kinopoisk - 5")
@allure.story("Поиск информации о фильмах и актерах")
@allure.feature("READ")
@allure.title("Получение актера по id")
@pytest.mark.api_tests
def test_search_actor_by_id():
    id_actor = api_poisk.search_actor_by_name(1, 1, 'Дэниэл Рэдклифф')['docs'][0]['id']
    info_actor = api_poisk.search_actor_by_id(id_actor)
    assert info_actor['name'] == 'Дэниэл Рэдклифф'
    assert info_actor['id'] == id_actor
