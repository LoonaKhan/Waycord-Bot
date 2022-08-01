"""
Loads the environment variables
"""
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
KEY = os.getenv('KEY')
INVITE_LINK = os.getenv('INVITE_LINK')