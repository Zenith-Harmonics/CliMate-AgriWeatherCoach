import json
from http.client import responses

from anyio.abc import value
from jiter.jiter import from_json

import functions.test_functions
from API_test import METEOMATICS_USERNAME
from functions import JSON_response
from dotenv import load_dotenv
import os
from chatGPT_service import chatgpt_handler
from functions import test_functions
load_dotenv()

METEOMATICS_USERNAME = os.getenv("METEOMATICS_USERNAME")
METEOMATICS_PASSWORD = os.getenv("METEOMATICS_PASSWORD")
CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")


def print_response(respone:str):
    response = "CliMate: " + respone + "\n"
    print(response)


def get_input():
    user_input = input("User: ")
    return user_input


def main():
    chatgpt = chatgpt_handler.ChatGPT(CHATGPT_API_KEY)

    conversation_topics = ['precipitation']

    conversation_status = {
        'city':None,
        'country':None,
        'topic':None,
    }

    prompt = "You are CliMate, an agri-weather coach. Greet the user and ask how you can help them.(short)"
    response = chatgpt.generate_response(prompt)
    print_response(response)

    while True:
        user_input = get_input()

        if conversation_status['topic'] is None:
            prompt  = f"This is the user's input: {user_input}"
            prompt += f"If the user input is related to one of the topics: {str(conversation_topics)}, return the name of the topic if not return None"
            response = chatgpt.generate_response(prompt)

            if response != 'None':
                conversation_status['topic'] = response

        if conversation_status['city'] is None:
            prompt = f"This is the user's input: {user_input}"
            prompt += f"If the user is saying about his city return only the city if not, return None"
            response = chatgpt.generate_response(prompt)

            if response != 'None':
                conversation_status['city'] = response

        if conversation_status['country'] is None:
            prompt = f"This is the user's input: {user_input}"
            prompt += f"If the user is saying about his country return only the country if not, return None"
            response = chatgpt.generate_response(prompt)

            if response != 'None':
                conversation_status['country'] = response

        missing_list = []
        for key in conversation_status.keys():
            if conversation_status[key] is None:
                missing_list.append(key)

        if len(missing_list) > 0:
            prompt = f"As CliMate the AgriWeather Coach you  ask the user to provide this informations:  {missing_list}"
            response = chatgpt.generate_response(prompt)
            print_response(response)
        else:
            pass

        




        """
        prompt  = f"This is the conversation status {str(conversation_status)}."
        prompt += f"This is the user input '{user_input}'"
        prompt += f"Using user input, complete and return the conversation_status JSON."
        prompt += f"If user is asking for something related to {str(conversation_topics)}, set server request to the specific topic, if not set gpt_message to something friendly"
        prompt += f"If server_request is not None and the user_info is incomplete set gpt_response with a question about the data needed."
        """




    """
    # Initialize GPT model instance
    chatgpt = chatgpt_handler.ChatGPT(os.getenv("CHATGPT_API_KEY"))

    # Greet the user as "CliMate" and ask how you can help
    response = chatgpt.generate_response("You are CliMate, an agri-weather coach. Greet the user and ask how you can help them.(short)")
    response = "CliMate: " + response
    print(response)

    # Input loop to receive user queries
    while True:
        user_input = input("\nUser: ")

        # Ask if the input is related to precipitation
        response = chatgpt.generate_response(f"{user_input}, is this text related to precipitation? Respond with 'yes' or 'no'.")

        if response.lower().strip() == "yes":
            response = chatgpt.generate_response(
                f"Ask user about his country and city")
            response = "\nCliMate: " + response

            print(response)

            user_input = input("\nUser: ")

            response = chatgpt.generate_response(
                f"'{user_input}', which city appears in the text? respond 'city country' ")


            response = response.split()

            lat, lon = JSON_response.get_lat_lon(response[0], response[1])

            date1 = "2020-01-01" + "T00:00:00Z"
            date2 = "2021-01-01" + "T00:00:00Z"

            json_data = JSON_response.get_precipitation_data(lat, lon, date1, date2, USERNAME, METEOMATICS_PASSWORD)
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
    """





if __name__ == "__main__":
    main()
    #JSON_response.main()