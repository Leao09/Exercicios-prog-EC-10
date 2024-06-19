from fastapi import Depends, Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordBearer
from db import User
from auth.jwt_handler import decodeJWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="acess_token")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decodeJWT(token)
    if not payload:
        raise credentials_exception

    user_id: str = payload.get("user_id")
    roles: str = payload.get("roles")
    if user_id is None or roles is None:
        raise credentials_exception

    user = await User.objects.get(id=user_id)
    if user is None:
        raise credentials_exception
    return user


class jwtBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(jwtBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(jwtBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Token inválido ou expirado.")
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=403, detail="Token inválido ou expirado.")

    def verify_jwt(self, jwttoken: str):
        isTokenValid: bool = False
        payload = decodeJWT(jwttoken)
        if payload:
            isTokenValid = True
        return isTokenValid
    
    def role_verification(required_role: str):
        def role_verifier(user: User = Depends(get_current_user)):
            if user.roles != required_role:
                raise HTTPException(
                    status_code=403,
                    detail="Operation not permitted"
                )
            return user
        return role_verifier