from fastapi import APIRouter, Depends, status

from src.apps.beer.api.v1.dependecy_injection.container import container

from ..controllers import HealthCheckController

router = APIRouter(tags=["Health check"])


@router.get("/", response_model=str, status_code=status.HTTP_200_OK)
def health_check():
    controller: HealthCheckController = container.get("HealthCheckController")
    return controller.run(request=None)
