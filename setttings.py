from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())

CONNECTION_STRING = os.environ.get("CONNECTION_STRING")
SECRET_KEY = os.environ.get("SECRET_KEY")