from fastapi import APIRouter

from src.routes import weather_route
from src.routes import main_routes

api_routes = APIRouter()
api_routes.include_router(weather_route.router, tags=["Weather"])
api_routes.include_router(main_routes.router, tags=["Main"])
