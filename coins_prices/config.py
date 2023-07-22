from pydantic import BaseModel, BaseSettings


class ProjectConfig(BaseSettings):
    debug: bool
    secret: str
    language: str
    timezone: str

    class Config:
        env_prefix = 'project_'


class PostgresConfig(BaseSettings):
    host: str
    port: str
    db: str
    user: str
    password: str

    class Config:
        env_prefix = 'postgres_'


class Config(BaseModel):
    project: ProjectConfig = ProjectConfig()
    postgres: PostgresConfig = PostgresConfig()
