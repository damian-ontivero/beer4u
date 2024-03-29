from fastapi import Request, Response, status

from .controller import Controller


class HealthCheckController(Controller):

    def run(self, request: Request) -> Response:
        return Response(
            content="Beer4U API is up!",
            status_code=status.HTTP_200_OK,
            media_type="text/plain",
        )
