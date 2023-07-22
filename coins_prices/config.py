from pydantic import BaseModel, BaseSettings


class PostgresConfig(BaseSettings):
    host: str
    port: str
    db: str
    user: str
    password: str

    class Config:
        env_prefix = 'postgres_'


class Config(BaseModel):
    postgres: PostgresConfig = PostgresConfig()
