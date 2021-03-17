from app.app_factory import create_app
import os


app = create_app(os.getenv("APP_ENVIROMENT"))