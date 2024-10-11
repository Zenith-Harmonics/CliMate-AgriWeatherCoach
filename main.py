import json
import os
from dotenv import load_dotenv
from functions import JSON_response
from chatGPT_service import chatgpt_handler
from functions import test_functions

class Meteomatics_Service:

    def __init__(self):
        load_dotenv()
        self.METEOMATICS_USERNAME = os.getenv("METEOMATICS_USERNAME")
        self.METEOMATICS_PASSWORD = os.getenv("METEOMATICS_PASSWORD")
        self.CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")
        self.chatgpt = chatgpt_handler.ChatGPT(self.CHATGPT_API_KEY)
        self.conversation_status = {
            'city': None,
            'country': None,
            'topic': None,
        }
        self.conversation_topics = ['precipitation', 'soil moisture']

    def print_response(self, response: str):
        """Formats and prints the bot response."""
        formatted_response = "CliMate: " + response + "\n"
        print(formatted_response)

    def get_input(self) -> str:
        """Gets input from the user via console."""
        return input("User: ")

    def generate_chatgpt_prompt(self, user_input: str) -> str:
        """Generate a prompt for ChatGPT based on user input and conversation status."""
        prompt = f"""
            You are a chatbot assisting a user with weather information.
            Here is the user's input: "{user_input}"
            Here is the current conversation status: {self.conversation_status}
            And here is a list of topics available: {self.conversation_topics}.

            Based on this, provide a JSON response with:
            - City
            - Country
            - The topic if the user's input is related to discussion topics if not set to none
            - Ask the user only for the missing conversation statuses
            - Update the conversation status
            - Use 'None' instead of null

            Format the response in JSON like this:
            {{
                "city": "<city>",
                "country": "<country>",
                "topic": "<topic>",
                "message": "<message for user>"
            }}
            """
        return prompt

    def update_conversation_status(self, response: dict):
        """Update the conversation status based on the response."""
        self.conversation_status.update(response)

    def handle_weather_data(self, city: str, country: str):
        """Fetch and process weather data based on city and country."""
        lat, lon = JSON_response.get_lat_lon(city, country)

        # Define the date range for fetching the weather data
        date1 = "2020-01-01T00:00:00Z"
        date2 = "2021-01-01T00:00:00Z"

        # Fetch precipitation data from METEOMATICS API
        json_data = JSON_response.get_precipitation_data(lat, lon, date1, date2, 
                                                         self.METEOMATICS_USERNAME, 
                                                         self.METEOMATICS_PASSWORD)

        # Extract precipitation values from the response
        values = [date_entry['value'] for item in json_data['data'] 
                  for coordinate in item['coordinates'] 
                  for date_entry in coordinate['dates']]

        # Calculate the average precipitation and determine flood risk
        if sum(values) / len(values) < 2:
            self.print_response(
                "Based on the precipitation data gathered from your location, the risk of flooding is low, "
                "which creates favorable conditions for farming. You can proceed with confidence, as the "
                "current weather patterns support a stable environment for agricultural activities."
            )
        else:
            self.print_response(
                "Based on the precipitation data gathered from your location, the risk of flooding is high, "
                "which creates unfavorable conditions for farming. Exercise caution, as the current weather "
                "patterns indicate potential disruptions to agricultural activities."
            )

    def run(self):
        # Initial greeting
        prompt = "You are CliMate, an agri-weather coach. Greet the user and ask how you can help them. (short)"
        response = self.chatgpt.generate_response(prompt)
        self.print_response(response)

        # Main loop
        while True:
            user_input = self.get_input()
            prompt = self.generate_chatgpt_prompt(user_input)
            response = self.chatgpt.generate_response(prompt)

            # Convert the response from JSON string to Python dictionary
            response_dict = json.loads(response.strip())
            self.update_conversation_status(response_dict)

            # Check if any required information is missing
            missing = [key for key, value in response_dict.items() if value == 'None']

            if not missing:
                # All information provided, proceed with fetching weather data
                self.handle_weather_data(response_dict['city'], response_dict['country'])
            else:
                # Ask the user for missing information
                self.print_response(response_dict['message'])


if __name__ == "__main__":
    meteomatics=Meteomatics_Service()
    meteomatics.run()

