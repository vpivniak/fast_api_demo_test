from typing import List

from pydantic import BaseModel


class WeatherModel(BaseModel, extra='forbid'):
    id: int
    city: str
    temperature: float
    time: str


class WeatherResponse(BaseModel, extra='forbid'):
    date: str
    history: List[WeatherModel]


class ErrorResponse(BaseModel, extra='forbid'):
    error: str
