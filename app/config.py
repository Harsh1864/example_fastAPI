from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    database_hostname : str = "localhost"
    database_port : int = 5432
    database_password : str = "Harsh6567"
    database_name : str = "fastapi1"
    database_username : str = "postgres"
    secret_key : str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    algorithm : str = "HS256"
    ACCESS_TOKEN_EXPIRE_HOURS : int = 24

    

setting = Setting()