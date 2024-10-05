#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#pip install python-dotenv requests
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import os
import requests
from dotenv import load_dotenv

load_dotenv()

METEOMATICS_USERNAME = os.getenv("METEOMATICS_USERNAME")
METEOMATICS_PASSWORD = os.getenv("METEOMATICS_PASSWORD")

def test_meteomatics_request():
    base_url = "https://api.meteomatics.com"

    #parametrii pt test
  
    lat, lon = "52.520008", "13.404954"
    start_date = "2024-10-01T00:00:00Z"
    end_date = "2024-10-02T00:00:00Z"
    parameters = "t_2m:C"
    
    api_url = f"{base_url}/{start_date}--{end_date}:PT1H/{parameters}/{lat},{lon}/json"
    
    response = requests.get(api_url, auth=(METEOMATICS_USERNAME, METEOMATICS_PASSWORD))
    
    if response.status_code == 200:
        return "200 OK"    #200ok daca te poti conecta
    else:
        return f"Error: {response.status_code} - {response.text}"  

result = test_meteomatics_request()
print(result)

