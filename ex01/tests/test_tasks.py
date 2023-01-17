import pytest
from pathlib import Path

from srcs.tasks import DataFetchingTask
from models.fetching_model import ForecastResponse


@pytest.mark.parametrize('city', ['MOSCOW', 'LONDON', 'SPETERSBURG', 'NOVOSIBIRSK', 'KALININGRAD'])
def test_fetch_forecast(instantiate_api_client, city: str):
    forecast_response = DataFetchingTask(api_client=instantiate_api_client).fetch_forecast(city=city)
    assert isinstance(forecast_response, ForecastResponse) is True
    assert forecast_response.city == city


@pytest.mark.parametrize('city', ['MMMMOSCOW', 'LINDIN', 'asdzxc'])
def test_fetch_forecast_exception(instantiate_api_client, city: str):
    with pytest.raises(Exception):
        forecast_responses = DataFetchingTask(api_client=instantiate_api_client).fetch_forecast(city=city)
