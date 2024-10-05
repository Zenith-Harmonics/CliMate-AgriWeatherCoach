import os
from dotenv import load_dotenv
import requests
from datetime import datetime
from geopy.geocoders import Nominatim

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


def getPrecipitationForDateRange(data, start_date, end_date):

    try:
        total_precipitation = 0
        start_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_dt = datetime.strptime(end_date, '%Y-%m-%d')

        for parameter_data in data['data']:
            if parameter_data['parameter'] == 'precip_1h:mm':
                for location in parameter_data['coordinates']:
                    for entry in location['dates']:
                        entry_date = datetime.strptime(entry['date'][:10], '%Y-%m-%d') 
                        if start_dt <= entry_date <= end_dt:
                            total_precipitation += entry['value']

        return total_precipitation

    except KeyError:
        raise ValueError("Precipitation data not found in the response")



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

    precip_df = getPrecipitationForDateRange(data, start_date, end_date)


if __name__ == "__main__":
    main()

