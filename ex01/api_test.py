def check_python_version():
    from srcs.utils import check_python_version

    check_python_version()


def check_api():
    from srcs.api_client import YandexWeatherAPI

    CITY_NAME_FOR_TEST = "MOSCOW"

    ywAPI = YandexWeatherAPI()
    data = ywAPI.get_forecasting(CITY_NAME_FOR_TEST)
    info = data.get("info")
    print(info)


if __name__ == "__main__":
    check_python_version()
    check_api()
