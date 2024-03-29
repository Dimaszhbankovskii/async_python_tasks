CITIES: dict[str, str] = {
    "MOSCOW": "https://code.s3.yandex.net/async-module/moscow-response.json",
    "PARIS": "https://code.s3.yandex.net/async-module/paris-response.json",
    "LONDON": "https://code.s3.yandex.net/async-module/london-response.json",
    "BERLIN": "https://code.s3.yandex.net/async-module/berlin-response.json",
    "BEIJING": "https://code.s3.yandex.net/async-module/beijing-response.json",
    "KAZAN": "https://code.s3.yandex.net/async-module/kazan-response.json",
    "SPETERSBURG": "https://code.s3.yandex.net/async-module/spetersburg-response.json",
    "VOLGOGRAD": "https://code.s3.yandex.net/async-module/volgograd-response.json",
    "NOVOSIBIRSK": "https://code.s3.yandex.net/async-module/novosibirsk-response.json",
    "KALININGRAD": "https://code.s3.yandex.net/async-module/kaliningrad-response.json",
    "ABUDHABI": "https://code.s3.yandex.net/async-module/abudhabi-response.json",
    "WARSZAWA": "https://code.s3.yandex.net/async-module/warszawa-response.json",
    "BUCHAREST": "https://code.s3.yandex.net/async-module/bucharest-response.json",
    "ROMA": "https://code.s3.yandex.net/async-module/roma-response.json",
    "CAIRO": "https://code.s3.yandex.net/async-module/cairo-response.json",
}

ERR_MESSAGE_TEMPLATE: str = "Something wrong."
CLEAR_WEATHER_SIGNS: tuple = ('clear', 'partly-cloudy', 'cloudy', 'overcast')

MIN_MAJOR_PYTHON_VER: int = 3
MIN_MINOR_PYTHON_VER: int = 9

RESULT_FILE_NAME: str = 'report.json'


def check_python_version():
    """Функция проверки версии интерпретатора Python"""
    import sys

    if sys.version_info.major < MIN_MAJOR_PYTHON_VER or \
    sys.version_info.minor < MIN_MINOR_PYTHON_VER:
        raise Exception("Please use python version >= {}.{}".format(
            MIN_MAJOR_PYTHON_VER, MIN_MINOR_PYTHON_VER))


def calculate_average(iterable_data: list[float]) -> float:
    try:
        return round(sum(iterable_data) / len(iterable_data), 2)
    except ZeroDivisionError:
        return 0
