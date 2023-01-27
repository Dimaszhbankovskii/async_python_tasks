import json
from concurrent.futures import ThreadPoolExecutor

from srcs.api_client import YandexWeatherAPI

from models.fetching_model import ForecastResponse

from srcs.tasks import DataFetchingTask

from srcs.utils import CITIES

api_client: YandexWeatherAPI = YandexWeatherAPI()

if __name__ == '__main__':
    with ThreadPoolExecutor() as pool_threads:
        responses = pool_threads.map(
            DataFetchingTask(api_client).fetch_forecast,
            CITIES.keys()
        )

    forecast_responses: list[ForecastResponse] = list(responses)
