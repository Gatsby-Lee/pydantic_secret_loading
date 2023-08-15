from fastapi import FastAPI
from pydantic import BaseSettings

app = FastAPI()

class BaseConfig(BaseSettings):

    my_secret: str

    class Config:
        case_sensitive = True
        secrets_dir = "/run/secrets"

APP_SETTING = BaseConfig()


@app.get("/")
async def root():
    return {"data": APP_SETTING}

