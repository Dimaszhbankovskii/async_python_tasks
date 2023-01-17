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

    # with open('city_forecast_response.json', 'w') as outfile:
    #     json.dump(forecast_responses, outfile)

    # print(forecast_responses[0].city)
    # print(forecast_responses[0].forecasts[0].date)
    # print(forecast_responses[0].forecasts[0].hours)
    # print(forecast_responses[0].forecasts[0].hours[0].hour)
    # print(forecast_responses[0].forecasts[0].hours[0].temp)
    # print(forecast_responses[0].forecasts[0].hours[0].condition)

    # for forecast in forecast_responses:
    #     print(forecast.city)
