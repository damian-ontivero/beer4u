from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .exception import EXCEPTION_TO_HTTP_STATUS_CODE
from .routers import beer_router, health_check_router, store_router

app = FastAPI(
    title="Beer4U API",
    description="All the endpoints to interact with the Beer4U API.",
    version="0.1.0",
    root_path="/api/v1",
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers
app.include_router(router=health_check_router)
# app.include_router(router=beer_router)
# app.include_router(router=store_router)


# Setups the exception handler
@app.exception_handler(Exception)
def exception_handler(request: Request, exception: Exception):
    return JSONResponse(
        content={"message": str(exception)},
        status_code=EXCEPTION_TO_HTTP_STATUS_CODE.get(
            exception.__class__, 500
        ),
    )
