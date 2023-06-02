import json
from urllib.request import urlopen

from services.logger import logger
from srcs.utils import CITIES, ERR_MESSAGE_TEMPLATE


class YandexWeatherAPI:
    """
    Базовый класс для осуществления запросов в YandexWeatherAPI
    """

    @staticmethod
    def _do_request(url: str) -> dict:
        """
        Метод осуществления запроса

        :param str url: ссылка
        :return dict: данные полученные по ссылке
        """
        try:
            with urlopen(url) as response:
                data = response.read().decode("utf-8")
                data = json.loads(data)
                logger.info(f'Success request forecast on {url}')
            if response.status != 200:
                raise Exception(f"Error during execute request. {response.status}: {response.reason}")
            return data
        except Exception as ex:
            logger.error(f'Unsuccess request. Request url -> {url}. Status code -> {response.status}. Exception: {ex}')
            raise Exception(ERR_MESSAGE_TEMPLATE)

    @staticmethod
    def _get_url_by_city_name(city_name: str) -> str:
        """
        Получение ссылки на прогноз погоды из словаря ссылок CITIES

        :param str city_name: название города
        :return str: ссылка на прогноз погоды
        """
        try:
            return CITIES[city_name]
        except KeyError:
            raise Exception(f"Please check that city {city_name} exists")

    def get_forecasting(self, city_name: str) -> dict:
        """
        Получение прогноза погоды для города по названию

        :param str city_name: название города
        :return dict: данные прогноза погоды
        """
        city_url: str = self._get_url_by_city_name(city_name)
        return self._do_request(city_url)
