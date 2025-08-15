from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
from api import predict, healthy
from core.config import APP_NAME, VERSION, API_SECRET_KEY

app = FastAPI(title=APP_NAME, version=VERSION, description="Disaster Tweets Classification API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

api_key_header = APIKeyHeader(name= "X-API-KEY")
async def verify_api_key(api_key:str = Depends(api_key_header)):
    if api_key != API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Forbidden: Invalid API Key")
    return api_key

app.include_router(healthy.router, dependencies=[Depends(verify_api_key)])
app.include_router(predict.router, dependencies=[Depends(verify_api_key)])