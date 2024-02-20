from fastapi import status
from jwt.exceptions import ExpiredSignatureError

from beer4u.shared.domain import AlreadyExists, AuthenticationError, NotFound

EXCEPTION_TO_HTTP_STATUS_CODE = {
    Exception: status.HTTP_500_INTERNAL_SERVER_ERROR,
    AuthenticationError: status.HTTP_403_FORBIDDEN,
    ExpiredSignatureError: status.HTTP_403_FORBIDDEN,
    PermissionError: status.HTTP_403_FORBIDDEN,
    NotFound: status.HTTP_404_NOT_FOUND,
    AlreadyExists: status.HTTP_422_UNPROCESSABLE_ENTITY,
    ValueError: status.HTTP_400_BAD_REQUEST,
    TypeError: status.HTTP_400_BAD_REQUEST,
}
