from pydantic import BaseSettings


class Settings(BaseSettings):
  app_name: str = "Awesome Api Tutorial"
  admin_email: str 
   
   
  class Config: 
    env_file = ".env"