import os
from dotenv import load_dotenv

load_dotenv()

Settings = {"AMADEUS_CLIENT_ID": os.getenv("AMADEUS_CLIENT_ID"),
             "AMADEUS_SECRET": os.getenv("AMADEUS_SECRET")}