import os
import time
from datetime import datetime

import sqlite3
from contextlib import closing
import pytest

from database.setup_database import create_table
from tests.helper.envs import TEST_DATABASE_PATH
from src.logic.database_helper import insert_temperature
from src.logic.database_helper import get_day_weather
from src.logic.constants import DATE_FORMAT
from src.models.weather_model import WeatherModel


def rm_db_file(*, database_path: str):
    """Delete database file"""
    if os.path.exists(database_path):
        os.remove(database_path)


@pytest.fixture
def tear_down(request):
    """Clean up database file before and after"""
    rm_db_file(database_path=TEST_DATABASE_PATH)

    def finalizer():
        rm_db_file(database_path=TEST_DATABASE_PATH)

    # Register the finalizer to ensure cleanup
    request.addfinalizer(finalizer)


def test_setup_table(tear_down):
    """Check creation database file and table in it."""
    create_table(database_path=TEST_DATABASE_PATH)

    with closing(sqlite3.connect(TEST_DATABASE_PATH)) as conn:
        with conn:
            result = conn.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
            tables = result.fetchall()

    table_names = [table[0] for table in tables]
    is_present = any(name == "weather" for name in table_names)

    assert is_present, "weather table should present in database"


def test_insert_and_select(tear_down):
    """"""
    create_table(database_path=TEST_DATABASE_PATH)

    date_str = '2022-02-12'
    date_object = datetime.strptime(date_str, DATE_FORMAT).date()

    time_str = '14:00:00'

    test_weather = WeatherModel(id=1,
                                city='London',
                                temperature=2.01,
                                time=time_str)

    insert_temperature(temperature=2.01,
                       city='London',
                       weather_date=date_object,
                       weather_time=time_str,
                       database_path=TEST_DATABASE_PATH)

    weather_list = get_day_weather(weather_date=date_object,
                                   database_path=TEST_DATABASE_PATH)

    is_created = any(test_weather == weather for weather in weather_list)
    assert is_created, "weather data should present in database"
