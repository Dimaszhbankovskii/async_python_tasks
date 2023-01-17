from pydantic import BaseModel, validator


class HourlyForecast(BaseModel):
    """
    Класс для почасового прогноза погоды для города
    hour: время в часах
    temp: температура
    condition: состояние погоды
    """
    hour: int
    temp: int
    condition: str


class DailyForecast(BaseModel):
    """
    Класс для ежедневного прогноза погоды для города
    data: дата в формате дд-мм
    hours: почасовой прогноз погоды
    """
    date: str
    hours: list[HourlyForecast]

    @validator('date')
    def parse_data_to_format(cls, date: str):
        """гггг-мм-дд ==> дд-мм"""
        tmp: list[str] = date.split('-')
        return '{}-{}'.format(tmp[-1], tmp[-2])


class ForecastResponse(BaseModel):
    """
    Класс для общего прогноза погоды для города
    city: название города
    forecasts: ежедневный прогноз погоды
    """
    city: str
    forecasts: list[DailyForecast]
