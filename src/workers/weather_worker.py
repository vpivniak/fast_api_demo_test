from datetime import date
import time

from requests.exceptions import RequestException
from sqlite3.dbapi2 import DatabaseError
import logging
import requests

from src.logic.env_import import WEATHER_KEY
from src.logic.env_import import CITY
from src.logic.database_helper import insert_temperature
from src.logic.constants import TIME_FORMAT

logger = logging.getLogger(__name__)


def get_weather_temperature(*, city: str) -> float | None:
    """Read temperature"""
    http_call_timeout = 10  # in seconds
    weather_api = "http://api.openweathermap.org/data/2.5/weather"

    payload = {'q': city,
               'units': 'metric',
               'appid': WEATHER_KEY}

    try:
        response = requests.get(weather_api, params=payload, timeout=http_call_timeout)
        if response:
            temperature = response.json()['main']['temp']

            return temperature

    except RequestException as req_err:
        logger.error(f"REQUEST EXCEPTION {req_err}")
    except KeyError as key_err:
        logger.error(f"No key in weather response {key_err}")


def set_weather():
    """Read temperature from API and insert date to the database"""
    try:
        temperature = get_weather_temperature(city=CITY)
        if temperature:
            insert_temperature(temperature=temperature,
                               city=CITY,
                               weather_date=date.today(),
                               weather_time=time.strftime(TIME_FORMAT),)
    except DatabaseError as db_err:
        logger.error(f"DATABASE ERROR in worker: {db_err}")
