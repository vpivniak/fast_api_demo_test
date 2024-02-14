import os
import sys
import logging

logger = logging.getLogger(__name__)

absent_env_vars = []

# Environment
CITY = os.getenv('CITY') \
    if "CITY" in os.environ else absent_env_vars.append('CITY')

WEATHER_KEY = os.getenv('WEATHER_KEY') \
    if "WEATHER_KEY" in os.environ else absent_env_vars.append('WEATHER_KEY')

SECRET_TOKEN = os.getenv('SECRET_TOKEN') \
    if "SECRET_TOKEN" in os.environ else absent_env_vars.append('SECRET_TOKEN')

if absent_env_vars:
    logger.error("Cannot run app:")
    logger.error("Absent environment variables:")
    logger.error(', '.join(absent_env_vars))
    sys.exit(1)
else:
    logger.info('All environment parameters has been checked!')
