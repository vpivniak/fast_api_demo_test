from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from fastapi import FastAPI
import argparse
import logging
import uvicorn

from src.routes import api_routes
from src.logic.constants import EVERY_MINUTE_CRON
from workers.weather_worker import set_weather

app = FastAPI()
app.include_router(api_routes)

scheduler = BlockingScheduler()
parser = argparse.ArgumentParser()
logger = logging.getLogger(__name__)

# run application
parser.add_argument('-r', '--app', required=False, action='store_true')

# run worker
parser.add_argument('-w', '--worker', required=False, action='store_true')

if __name__ == "__main__":
    args = parser.parse_args()

    if args.app:
        logger.info("App is running")
        uvicorn.run(
            app="main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
        )
    elif args.worker:
        logger.info("Worker is running")
        scheduler.add_job(set_weather, CronTrigger.from_crontab(EVERY_MINUTE_CRON))
        scheduler.start()
    else:
        logger.error("Use -r flag for to app or use -w flag to run worker")
