from datetime import datetime

from fastapi import APIRouter
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse
from sqlite3.dbapi2 import DatabaseError

from src.logic.database_helper import get_day_weather
from src.logic.env_import import SECRET_TOKEN
from src.models.weather_model import ErrorResponse
from src.models.weather_model import WeatherResponse
from src.logic.constants import DATE_FORMAT

router = APIRouter()


@router.get("/weather", response_model=WeatherResponse)
def weather_history_list(date: str, request: Request) -> JSONResponse:
    token = request.headers.get('x-token')
    if not token:
        response_json = jsonable_encoder(ErrorResponse(error="Missing header: x-token"))
        return JSONResponse(response_json, status_code=status.HTTP_400_BAD_REQUEST)
    else:
        if token != SECRET_TOKEN:
            response_json = jsonable_encoder(ErrorResponse(error="Bad header x-token value"))
            return JSONResponse(response_json, status_code=status.HTTP_403_FORBIDDEN)

    try:
        date_object = datetime.strptime(date, DATE_FORMAT).date()
    except ValueError:
        response_json = jsonable_encoder(
            ErrorResponse(error=f"Please type correct date format: {DATE_FORMAT}"))
        return JSONResponse(response_json, status_code=status.HTTP_400_BAD_REQUEST)

    try:

        history = get_day_weather(weather_date=date_object)
        response_json = jsonable_encoder(WeatherResponse(date=date,
                                                         history=history))
        return JSONResponse(response_json, status_code=status.HTTP_200_OK)
    except DatabaseError as db_err:
        response_json = jsonable_encoder(
            ErrorResponse(error=f"Database error: {db_err}"))
        return JSONResponse(response_json, status_code=status.HTTP_400_BAD_REQUEST)
