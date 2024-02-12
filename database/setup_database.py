import os
import sys

import sqlite3
from contextlib import closing

absent_env_vars = []

DATABASE_PATH = os.environ['DATABASE_PATH'] \
    if "DATABASE_PATH" in os.environ else absent_env_vars.append('DATABASE_PATH')

if absent_env_vars:
    print("Absent environment variables:")
    print(', '.join(absent_env_vars))

    sys.exit(1)


def create_table(*, database_path: str):
    with closing(sqlite3.connect(database_path)) as conn:
        with conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS weather (
                    city TEXT NOT NULL,
                    temperature REAL NOT NULL,
                    weather_date TEXT NOT NULL,
                    time TEXT NOT NULL
                )
                """
            )


if __name__ == '__main__':
    create_table(database_path=DATABASE_PATH)
