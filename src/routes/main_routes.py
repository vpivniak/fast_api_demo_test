from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from starlette import status

from src.models.base import BaseResponse

router = APIRouter()


@router.get("/")
def read_root():
    response_json = jsonable_encoder(BaseResponse(message="Hello LDIT"))
    return JSONResponse(response_json, status_code=status.HTTP_200_OK)


@router.get("/healthcheck")
def healthcheck():
    response_json = jsonable_encoder(BaseResponse(message="Server alive!"))
    return JSONResponse(response_json, status_code=status.HTTP_200_OK)
