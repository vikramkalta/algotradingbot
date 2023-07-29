import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

BASE_URL = 'https://api-fxpractice.oanda.com/'
ACCOUNT_ID = '101-004-26396988-001'
UPWARD_TREND_THRESHOLD = 1.5
DIP_THRESHOLD = -2.25
PROFIT_THRESHOLD = 1.25
STOP_LOSS_THRESHOLD = -2.00

# Access the environment variables
AUTH_TOKEN = os.getenv('AUTH_TOKEN')