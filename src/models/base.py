from pydantic import BaseModel
from pydantic import Extra


class BaseResponse(BaseModel, extra='forbid'):
    message: str
