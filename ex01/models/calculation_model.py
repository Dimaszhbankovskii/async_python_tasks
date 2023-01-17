from pydantic import BaseModel


class DailyForecastIndicator(BaseModel):
    """
    Класс для
    """
    date: str
    daily_average_temperature: float
    daily_amount_rainless_time: float


class AggregatedForecastIndicator(BaseModel):
    """
    Класс для
    """
    daily_forecast_indicators: list[DailyForecastIndicator] = []
    average_temperature: float | None = None
    amount_rainless_time: float | None = None


class ForecastCalculation(BaseModel):
    """
    Класс для расчитанных данных по прогнозу погоды для города
    """
    city: str
    aggregated_indicators: AggregatedForecastIndicator
