import json
from urllib.request import urlopen

from services.logger import logger
from srcs.utils import CITIES, ERR_MESSAGE_TEMPLATE


class YandexWeatherAPI:
    """
    Base class for requests
    """

    @staticmethod
    def _do_request(url: str):
        """Base request method"""
        try:
            with urlopen(url) as response:
                data = response.read().decode("utf-8")
                data = json.loads(data)
                logger.info(f'Success request forecast on {url}')
            if response.status != 200:
                raise Exception(
                    f"Error during execute request. \
                    {response.status}: {response.reason}"
                )
            return data
        except Exception as ex:
            logger.error(f'Unsuccess request. Request url -> {url}.\
                Status code -> {response.status}. Exception: {ex}')
            raise Exception(ERR_MESSAGE_TEMPLATE)

    @staticmethod
    def _get_url_by_city_name(city_name: str) -> str:
        try:
            return CITIES[city_name]
        except KeyError:
            raise Exception(f"Please check that city {city_name} exists")

    def get_forecasting(self, city_name: str):
        """
        :param city_name: key as str
        :return: response data as json
        """
        city_url = self._get_url_by_city_name(city_name)
        return self._do_request(city_url)
