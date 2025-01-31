import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
IMEI_CHECK_API_URL = os.getenv("IMEI_CHECK_API_URL")
IMEI_CHECK_API_TOKEN = os.getenv("IMEI_CHECK_API_TOKEN")