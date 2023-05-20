import os

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer

api_keys = [
    os.getenv('API_KEY')
]
auth_scheme = HTTPBearer()


def authorization(api_key: str = Depends(auth_scheme)):
    if api_key.credentials not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
