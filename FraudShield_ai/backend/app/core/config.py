# --- config.py ---
# This file handles configuration settings for the application.
# It loads sensitive data like API keys from environment variables.


import os
from dotenv import load_dotenv


# Load environment variables from a .env file at the project root
load_dotenv()


class Settings:
   """
   Main settings class to hold all environment variables and configurations.
   """
   # B2B API Security
   # Expects a comma-separated string of keys in the .env file.
   # e.g., ALLOWED_API_KEYS=key1,key2,key3
   ALLOWED_API_KEYS: list[str] = os.getenv("ALLOWED_API_KEYS", "").split(',')


   # News API Key for data ingestion
   NEWS_API_KEY: str = os.getenv("NEWS_API_KEY")


# Create a single, importable instance of the settings
settings = Settings()
