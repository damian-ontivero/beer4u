from fastapi import APIRouter, status

from ..controllers import HealthCheckController

router = APIRouter(tags=["Health check"])


@router.get("/", response_model=str, status_code=status.HTTP_200_OK)
def health_check():
    controller = HealthCheckController()

    return controller.run(request=None)
