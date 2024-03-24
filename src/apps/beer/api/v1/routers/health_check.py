from fastapi import APIRouter, status

from ..controllers import HealthCheckController
from ..dependecy_injection import container

router = APIRouter(tags=["Health check"])


@router.get("/", response_model=str, status_code=status.HTTP_200_OK)
def health_check():
    controller: HealthCheckController = container.get("HealthCheckController")
    return controller.run(request=None)
