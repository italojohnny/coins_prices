from pydantic import BaseModel, BaseSettings


class MainAppConfig(BaseSettings):
    date_range: int

    class Config:
        env_prefix = 'mainapp_'


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
    main_app: MainAppConfig = MainAppConfig()
    postgres: PostgresConfig = PostgresConfig()
