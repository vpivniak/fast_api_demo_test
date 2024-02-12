from datetime import date

import sqlite3
from contextlib import closing

from src.models.weather_model import WeatherModel


def insert_temperature(*, temperature: float, city: str, weather_date: date, weather_time: str, database_path: str):
    """Insert to the database weather data"""
    with closing(sqlite3.connect(database_path)) as conn:
        with conn:
            conn.execute(
                """
                INSERT INTO weather
                    (city, temperature, weather_date, time)
                VALUES
                    (?, ?, ?, ?)
                """,
                (city, temperature, weather_date, weather_time)
            )


def get_day_weather(*, weather_date: date, database_path: str) -> list[WeatherModel]:
    """Read weather history from database for the current day"""
    with closing(sqlite3.connect(database_path)) as conn:
        with conn:
            result = conn.execute(
                """
                SELECT rowid ,city, temperature, time
                FROM weather
                WHERE weather_date=?
                ORDER BY rowid
                """,
                (weather_date,)
            )
            temp_history = result.fetchall()

            return [WeatherModel(id=row[0], city=row[1], temperature=row[2], time=row[3]) for row in temp_history]
