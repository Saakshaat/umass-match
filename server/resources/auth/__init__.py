from fastapi import Depends

from .jwt_middleware import get_jwks, JWTMiddleware

auth_middleware = JWTMiddleware(get_jwks())
auth_dependency = Depends(auth_middleware)
