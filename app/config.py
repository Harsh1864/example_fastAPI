from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    DATABASE_HOSTNAME : str = "localhost"
    DATABASE_PORT : int = 5432
    DATABASE_PASSWORD : str = "Harsh6567"
    DATABASE_NAME : str = "fastapi1"
    DATABASE_USERNAME : str = "postgres"
    SECRET_KEY : str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM : str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 24

    

setting = Setting()