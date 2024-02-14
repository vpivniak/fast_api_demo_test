from workers.weather_worker import get_weather_temperature


def test_returned_type():
    """Check that weather api return data"""
    temperature = get_weather_temperature(city='Kyiv')
    assert type(temperature) == float, "returned type should be float"
