import pytest
from pathlib import Path

from srcs.tasks import (DataFetchingTask,
                        DataCalculationTask)
from models.fetching_model import ForecastResponse
from models.calculation_model import (ForecastCalculation,
                                      AggregatedForecastIndicator,
                                      DailyForecastIndicator)


@pytest.mark.parametrize('city', ['MOSCOW', 'LONDON', 'SPETERSBURG', 'NOVOSIBIRSK', 'KALININGRAD'])
def test_fetch_forecast(instantiate_api_client, city: str):
    forecast_response = DataFetchingTask(api_client=instantiate_api_client).fetch_forecast(city=city)
    assert isinstance(forecast_response, ForecastResponse) is True
    assert forecast_response.city == city


@pytest.mark.parametrize('city', ['MMMMOSCOW', 'LINDIN', 'asdzxc'])
def test_fetch_forecast_exception(instantiate_api_client, city: str):
    with pytest.raises(Exception):
        forecast_responses = DataFetchingTask(api_client=instantiate_api_client).fetch_forecast(city=city)


def test_calculate_daily_forecast_indicator(instantiate_city_forecast, instantiate_daily_forecast):
    calculator = DataCalculationTask(city_forecast=instantiate_city_forecast)
    daily_forecast_indicator = calculator._calculate_daily_forecast_indicator(daily_forecast=instantiate_daily_forecast)
    assert isinstance(daily_forecast_indicator, DailyForecastIndicator) is True
    assert daily_forecast_indicator.daily_average_temperature == 17.73
    assert daily_forecast_indicator.daily_amount_rainless_time == 7


def test_calculate_aggregated_forecast_indicator(instantiate_city_forecast):
    calculator = DataCalculationTask(city_forecast=instantiate_city_forecast)
    aggregated_forecast_indicator = calculator._calculate_aggregated_forecast_indicator()
    assert isinstance(aggregated_forecast_indicator, AggregatedForecastIndicator) is True
    assert aggregated_forecast_indicator.average_temperature == 13.75
    assert aggregated_forecast_indicator.amount_rainless_time == 8.0
