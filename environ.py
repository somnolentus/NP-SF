from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv('EMAIL')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
DJANGO_SK = os.getenv('DJANGO_SK')
