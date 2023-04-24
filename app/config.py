from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    MONGO_INITDB_DATABASE: str

    CLIENT_ORIGIN: str


    class Config:
        env_file = './secrets.env'

settings = Settings()
