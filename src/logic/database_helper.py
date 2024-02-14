from datetime import date
import logging

import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection

from src.models.weather_model import WeatherModel

logger = logging.getLogger(__name__)


def insert_temperature(*,
                       temperature: float,
                       city: str,
                       weather_date: date,
                       connection: PooledMySQLConnection):
    """Insert to the database weather data"""
    cur = connection.cursor()
    try:
        cur.execute(
            """
            INSERT INTO weather
                (city, temperature, weather_date)
            VALUES
                (%s, %s, %s)
            """,
            [city, temperature, weather_date]
        )
        connection.commit()
    except mysql.connector.Error as err:
        logger.error("DATABASE ERROR - inserting record:", err)
    finally:
        cur.close()


async def get_day_weather(*, weather_date: date, connection: MySQLConnectionAbstract) -> list[WeatherModel]:
    """Read weather history from database for the current day"""
    async with await connection.cursor(buffered=True) as cur:
        await cur.execute(
            """
            SELECT id ,city, temperature
            FROM weather
            WHERE weather_date=%s
            ORDER BY id
            """,
            [weather_date]
        )
        histories = await cur.fetchall()

        return [WeatherModel(id=row[0], city=row[1], temperature=row[2]) for row in histories]
