from jose import jwt
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(hours=1)

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def verify_token(token: str):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    
def get_current_user_id(token: str):
    payload = verify_token(token)
    return payload["user_id"]