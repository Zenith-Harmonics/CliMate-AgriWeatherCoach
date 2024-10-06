from anyio.abc import value
from jiter.jiter import from_json

import functions.test_functions
from chatGPT import gpt
from functions import JSON_response
from dotenv import load_dotenv
import os
from functions import test_functions
load_dotenv()

USERNAME = os.getenv("METEOMATICS_USERNAME")
PASSWORD = os.getenv("METEOMATICS_PASSWORD")

def main():
    # Initialize GPT model instance
    chatgpt = gpt.GPT()

    # Greet the user as "CliMate" and ask how you can help
    response = chatgpt.get_response("You are CliMate, an agri-weather coach. Greet the user and ask how you can help them.(short)")
    response = "CliMate: " + response
    print(response)

    # Input loop to receive user queries
    while True:
        user_input = input("\nUser: ")

        # Ask if the input is related to precipitation
        response = chatgpt.get_response(f"{user_input}, is this text related to precipitation? Respond with 'yes' or 'no'.")

        if response.lower().strip() == "yes":
            response = chatgpt.get_response(
                f"Ask user about his country and city")
            response = "\nCliMate: " + response

            print(response)

            user_input = input("\nUser: ")

            response = chatgpt.get_response(
                f"'{user_input}', which city appears in the text? respond 'city country' ")


            response = response.split()

            lat, lon = JSON_response.get_lat_lon(response[0], response[1])

            date1 = "2020-01-01" + "T00:00:00Z"
            date2 = "2021-01-01" + "T00:00:00Z"

            json_data = JSON_response.get_precipitation_data(lat, lon, date1, date2, USERNAME, PASSWORD)
            with open('jsonfile', 'w') as file:
                file.write(str(json_data))
            values = []
            for item in json_data['data']:
                for coordinate in item['coordinates']:
                    for date_entry in coordinate['dates']:
                        values.append(date_entry['value'])

            if sum(values) / len(values) < 2:
                print()
                print("CliMate: Based on the precipitation data gathered from your location, the risk of flooding is low, which creates favorable conditions for farming.\nYou can proceed with confidence, as the current weather patterns support a stable environment for agricultural activities.")


        else:
            # If not precipitation-related, give a shorter response about inability to help
            response = chatgpt.get_response(
                f"You are CliMate, an agri-weather coach. Respond to the user that you can't help with their request: {user_input}, in a concise manner."
            )
            response = "CliMate: " + response






if __name__ == "__main__":
    main()
    #JSON_response.main()