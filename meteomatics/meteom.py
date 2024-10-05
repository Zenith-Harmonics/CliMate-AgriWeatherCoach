import os
import requests
from dotenv import load_dotenv


class Meteomatics:
    def __init__(self):
        load_dotenv()
        self.METEOMATICS_USERNAME = os.getenv("METEOMATICS_USERNAME")
        self.METEOMATICS_PASSWORD = os.getenv("METEOMATICS_PASSWORD")
        self.base_url = "https://api.meteomatics.com"

    def request(self):
        base_url = "https://api.meteomatics.com"

        lat, lon = "52.520008", "13.404954"

        start_date = "2024-10-01T00:00:00Z"
        end_date = "2024-10-02T00:00:00Z"
        parameters = "t_2m:C"

        api_url = f"{self.base_url}/{start_date}--{end_date}:PT1H/{parameters}/{lat},{lon}/json"

        response = requests.get(api_url, auth=(self.METEOMATICS_USERNAME, self.METEOMATICS_PASSWORD))

        if response.status_code == 200:
            return response
        else:
            return f"Error: {response.status_code} - {response.text}"


