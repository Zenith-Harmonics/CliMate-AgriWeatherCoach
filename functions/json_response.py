import os
from dotenv import load_dotenv
import requests
from datetime import datetime
from geopy.geocoders import Nominatim  #pip install geopy


load_dotenv()

USERNAME = os.getenv("METEOMATICS_USERNAME")
PASSWORD = os.getenv("METEOMATICS_PASSWORD")

def get_lat_lon(city, country):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(f"{city}, {country}")
    if location:
        return location.latitude, location.longitude
    else:
        print("Location not found!")
        return None, None

def get_precipitation_data(lat, lon, start_date, end_date, username, password):
    base_url = "https://api.meteomatics.com"
    parameters = "precip_1h:mm"  
    time_range = f"{start_date}--{end_date}:PT1H" 

    url = f"{base_url}/{time_range}/{parameters}/{lat},{lon}/json"

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        data = response.json()
        print("API Response: ", data)

def main():
    city = input("Enter city name: ")
    country = input("Enter country name: ")

    lat, lon = get_lat_lon(city, country)
    if lat is None or lon is None:
        return  

    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    try:
        start_date = f"{start_date}T00:00:00Z"
        end_date = f"{end_date}T23:59:59Z"
    except Exception as e:
        print(f"Error in date format: {e}")
        return

    precip_df = get_precipitation_data(lat, lon, start_date, end_date, USERNAME, PASSWORD)


if __name__ == "__main__":
    main()

