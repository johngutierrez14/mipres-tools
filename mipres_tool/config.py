import os
from dotenv import load_dotenv

load_dotenv()

API_URL_JUNTA_MEDICA = os.getenv("API_URL_JUNTA_MEDICA")
API_URL_PRESCRIPCION = os.getenv("API_URL_PRESCRIPCION")
TOKEN = os.getenv("TOKEN")
NIT = os.getenv("NIT")