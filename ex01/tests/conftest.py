import pytest

from srcs.api_client import YandexWeatherAPI


@pytest.fixture()
def instantiate_api_client() -> YandexWeatherAPI:
    return YandexWeatherAPI()
