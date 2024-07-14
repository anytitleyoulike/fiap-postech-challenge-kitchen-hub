from starlette.requests import Request
from starlette.responses import JSONResponse

from src.core.domain.exceptions import (
    NotFoundError, OperationalException
)


def register_exceptions(app):

    @app.exception_handler(NotFoundError)
    async def not_found_handler(request: Request, exc: NotFoundError):
        return JSONResponse(
            status_code=400,
            content={"message": str(exc)},
        )

    @app.exception_handler(OperationalException)
    async def operational_handler(request: Request, exception: OperationalException):
        return JSONResponse(
            status_code=400,
            content={"message": str(exception)}
        )