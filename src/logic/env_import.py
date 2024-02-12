import os
import sys
import logging

from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

absent_env_vars = []
absent_env_files = []

# Environment
CITY = os.environ['CITY'] \
    if "CITY" in os.environ else absent_env_vars.append('CITY')

WEATHER_KEY = os.environ['WEATHER_KEY'] \
    if "WEATHER_KEY" in os.environ else absent_env_vars.append('WEATHER_KEY')

DATABASE_PATH = os.environ['DATABASE_PATH'] \
    if "DATABASE_PATH" in os.environ else absent_env_vars.append('DATABASE_PATH')

SECRET_TOKEN = os.environ['SECRET_TOKEN'] \
    if "SECRET_TOKEN" in os.environ else absent_env_vars.append('SECRET_TOKEN')

if not os.path.exists(DATABASE_PATH):
    absent_env_files.append("ldit.db")

if absent_env_vars or absent_env_files:
    logger.error("Cannot run app:")
    if absent_env_vars:
        logger.error("Absent environment variables:")
        logger.error(', '.join(absent_env_vars))

    if absent_env_files:
        logger.error("Absent files:")
        logger.error(', '.join(absent_env_files))
    sys.exit(1)

else:
    logger.info('All environment parameters has been checked!')
