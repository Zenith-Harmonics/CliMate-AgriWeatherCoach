import os
from dotenv import load_dotenv
from functions import JSON_response
from chatGPT_service import chatgpt_handler
import json

class EnvironmentLoader:

    def __init__(self):
        load_dotenv()  # Load environment variables from .env file
        
        self.meteomatics_username = os.getenv("METEOMATICS_USERNAME")
        self.meteomatics_password = os.getenv("METEOMATICS_PASSWORD")
        self.chatgpt_api_key = os.getenv("CHATGPT_API_KEY")
        
        self.start_date = "2020-01-01T00:00:00Z"
        self.end_date = "2021-01-01T00:00:00Z"

    def get_credentials(self):
        return {
            "METEOMATICS_USERNAME": self.meteomatics_username,
            "METEOMATICS_PASSWORD": self.meteomatics_password,
            "CHATGPT_API_KEY": self.chatgpt_api_key,
            "START_DATE": self.start_date,
            "END_DATE": self.end_date,
        }

    def call_meteomatics_api(self, lat, lon):
        json_data = JSON_response.get_precipitation_data(
            lat, lon, self.start_date, self.end_date, 
            self.meteomatics_username, self.meteomatics_password
        )
        return json_data

