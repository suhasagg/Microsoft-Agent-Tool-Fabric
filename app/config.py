from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    env:str="dev"
    jwt_secret:str="change-me"
    redis_url:str="redis://localhost:6379/0"
    tool_timeout_seconds:float=30
    max_tool_results:int=8
    sandbox_enabled:bool=True
    model_config=SettingsConfigDict(env_file=".env",extra="ignore")
settings=Settings()
