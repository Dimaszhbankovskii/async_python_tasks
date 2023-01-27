import pytest

from srcs.api_client import YandexWeatherAPI
from models.fetching_model import (ForecastResponse,
                                   DailyForecast)

@pytest.fixture()
def instantiate_api_client() -> YandexWeatherAPI:
    return YandexWeatherAPI()


@pytest.fixture()
def instantiate_city_forecast() -> ForecastResponse:
    return ForecastResponse.parse_file('city_forecast.json')


@pytest.fixture()
def instantiate_daily_forecast() -> DailyForecast:
    return DailyForecast.parse_file('data_daily_forecast.json')
