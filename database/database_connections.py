import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.aio import connect as async_connect
from mysql.connector.pooling import PooledMySQLConnection

from src.logic.env_import import MYSQL_DATABASE
from src.logic.env_import import MYSQL_PASSWORD
from src.logic.env_import import MYSQL_USER

PORT = 3306
HOST = "database"


async def get_async_db_connection() -> MySQLConnectionAbstract:
    """Connect to a MySQL server and get a async connection."""
    return await async_connect(user=MYSQL_USER,
                               password=MYSQL_PASSWORD,
                               database=MYSQL_DATABASE,
                               port=PORT,
                               host=HOST)


def get_sync_db_connection() -> PooledMySQLConnection:
    """Connect to a MySQL server and get a sync connection."""
    return mysql.connector.connect(user=MYSQL_USER,
                                   password=MYSQL_PASSWORD,
                                   database=MYSQL_DATABASE,
                                   port=PORT,
                                   host=HOST)
