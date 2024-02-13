from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from fastapi.responses import JSONResponse

from beer4u.shared.infrastructure.ui.api.v1.exception import (
    EXCEPTION_TO_HTTP_STATUS_CODE,
)
from beer4u.shared.infrastructure.ui.api.v1.schema import MessageResponseSchema


@asynccontextmanager
async def lifespan(app: FastAPI):
    register_query_handlers()
    register_command_handlers()
    yield

app = FastAPI(
    title="Beer4U API",
    description="All the endpoints to interact with the Beer4U API.",
    version="0.1.0",
    lifespan=lifespan,
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
app.include_router(router=)


# Setups the exception handler
@app.exception_handler(Exception)
def exception_handler(request: Request, exception: Exception):
    return JSONResponse(
        content={"message": str(exception)},
        status_code=EXCEPTION_TO_HTTP_STATUS_CODE.get(
            exception.__class__, 500
        ),
    )


@app.get("/", tags=["Health check"], response_model=MessageResponseSchema)
def health_check():
    return JSONResponse(content={"message": "Component API is up!"})