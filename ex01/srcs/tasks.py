from srcs.api_client import YandexWeatherAPI

from models.fetching_model import (ForecastResponse,
                                   DailyForecast,
                                   HourlyForecast)
from models.calculation_model import (ForecastCalculation,
                                      AggregatedForecastIndicator,
                                      DailyForecastIndicator)
from srcs.utils import CLEAR_WEATHER_SIGNS, calculate_average


class DataFetchingTask:
    """
    Класс для получения прогноза погоды для города по YandexWeatherAPI
    """

    __slots__ = ('api_client',)

    def __init__(self, api_client: YandexWeatherAPI) -> None:
        self.api_client = api_client

    def fetch_forecast(self, city: str) -> ForecastResponse:
        response = self.api_client.get_forecasting(city)
        return ForecastResponse(
            city=city,
            forecasts=[
                DailyForecast(**forecast) for forecast
                in response.get('forecasts') if forecast.get('hours')
            ]
        )


class DataCalculationTask:
    """
    Класс для вычисления средней температуры и получения информации об осадках
    за определенный промежуток времени для города
    """

    __slots__ = ('_city_forecast',)

    LOWER_LIMIT_TIME: int = 9
    UPPER_LIMIT_TIME: int = 19

    def __init__(self, city_forecast: ForecastResponse) -> None:
        self._city_forecast: ForecastResponse = city_forecast

    def _calculate_daily_forecast_indicator(self, daily_forecast: DailyForecast) \
            -> DailyForecastIndicator:
        """"""
        hourly_forecast: list[HourlyForecast] = [
            hour_forecast for hour_forecast in daily_forecast.hours
            if self.LOWER_LIMIT_TIME <= hour_forecast.hour <= self.UPPER_LIMIT_TIME
        ]
        daily_temperatures: list[float] = []
        daily_rainless_time: float = 0.0
        for forecast in hourly_forecast:
            if forecast.condition in CLEAR_WEATHER_SIGNS:
                daily_rainless_time += 1
            daily_temperatures.append(forecast.temp)
        return DailyForecastIndicator(
            date=daily_forecast.date,
            daily_average_temperature=calculate_average(daily_temperatures),
            daily_amount_rainless_time=daily_rainless_time
        )

    def _calculate_aggregated_forecast_indicator(self) -> AggregatedForecastIndicator:
        """"""
        aggregated_indicators = AggregatedForecastIndicator()
        for daily_forecast in self._city_forecast.forecasts:
            pass

        return aggregated_indicators
