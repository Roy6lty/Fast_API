from fastapi import HTTPException, Header, status

async def get_token(x_token: str = Header()):
    if x_token != 'fake-super-secret-token':
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail = 'Token Invaild')
    return x_token

async def get_query_token(token:str):
    if token != 'jessica':
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, details = 'no_jessica')
