import requests
import allure


@allure.epic("KinopoiskApi")
@allure.severity("blocker")
class KinopoiskApi:

    def __init__(self, url):
        self.url = url
        self.headers = {"X-API-KEY": 'FEXNZZF-P8DMTPB-NM9XMSJ-5Z791A4'}

    @allure.step("Api. Получить фильм по названию {query}")
    def search_film_by_name(self, page: int, limit: int, query: str) -> dict:
        """ Осуществляет поиск фильма по названию

            Принимает параметры: page - количество страниц,
            limit - количество найденных фильмов,
            query - название фильма для поиска
        """
        params = {
            'page': page,
            'limit': limit,
            'query': query
        }
        resp = requests.get(
            self.url + 'v1.4/movie/search', params=params, headers=self.headers)
        return resp

    @allure.step("Api. Получить фильм по {id}")
    def search_film_by_id(self, id: int):
        """ Осуществляет поиск фильма по id.

            Принимает параметр id фильма.
        """
        resp = requests.get(
            self.url + 'v1.4/movie/' + str(id), headers=self.headers)
        return resp.json()

    @allure.step("Api. Получить актера по имени {query}")
    def search_actor_by_name(self, page: int, limit: int, query: str) -> dict:
        """ Осуществляет поиск актера по имени.

            Принимает параметры: page - количество страниц,
            limit - количество найденных фильмов,
            query - имя/фамилия актера
        """
        params = {
            'page': page,
            'limit': limit,
            'query': query
        }
        resp = requests.get(
            self.url + 'v1.4/person/search', params=params, headers=self.headers)
        return resp.json()

    @allure.step("Api. Получить фильм по нескольким фильтрам")
    def free_search_film(
        self, selectFields: str, year: str, countries_name: str, genres_name: str, persons_id: int) -> dict:
        """ Осуществляет универсальный поиск фильма
            по нескольким параметрам.

            Принимает парамерты:
            selectFields - Список полей требуемых в ответе,
            year - Поиск по году,
            countries.name - Поиск по жанрам,
            genres.name - Поиск по странам,
            persons.id - Поиск по ID актера
        """
        params = {
            'selectFields': selectFields,
            'year': year,
            'countries.name': countries_name,
            'genres.name': genres_name,
            'persons.id': persons_id
        }
        resp = requests.get(
            self.url + 'v1.4/movie', params=params, headers=self.headers)
        return resp.json()

    @allure.step("Api. Получить актера по {id}")
    def search_actor_by_id(self, id) -> dict:
        """ Осуществляет поиск актера по id.

            Принимает параметр id актера
        """
        resp = requests.get(
            self.url + 'v1.4/person/' + str(id), headers=self.headers)
        return resp.json()
