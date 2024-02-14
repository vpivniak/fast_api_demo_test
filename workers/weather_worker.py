from datetime import date

from mysql.connector.errors import DatabaseError
from mysql.connector.errors import InterfaceError
from mysql.connector.errors import PoolError
from requests.exceptions import RequestException
import logging
import requests

from database.database_connections import get_sync_db_connection
from src.logic.constants import EVERY_MINUTE_CRON
from src.logic.constants import TIME_FORMAT
from src.logic.database_helper import insert_temperature
from src.logic.env_import import CITY
from src.logic.env_import import WEATHER_KEY

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
            return response.json()['main']['temp']

    except RequestException as req_err:
        logger.error(f"REQUEST EXCEPTION {req_err}")
    except KeyError as key_err:
        logger.error(f"No key in weather json response {key_err}")


def set_weather():
    """Read temperature from API and insert date to the database"""
    try:
        temperature = get_weather_temperature(city=CITY)
        logger.error(f"temperature: {temperature}")
        print(f"temperature: {temperature}")
        if temperature:
            connection = get_sync_db_connection()

            insert_temperature(temperature=temperature,
                               city=CITY,
                               weather_date=date.today(),
                               connection=connection)
            connection.close()
    except (DatabaseError, InterfaceError, PoolError) as db_err:
        logger.error(f"DATABASE ERROR - in worker: {db_err}")
