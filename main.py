from chatGPT import gpt
from functions import JSON_response

def main():
    # Initialize GPT model instance
    chatgpt = gpt.GPT()

    # Greet the user as "CliMate" and ask how you can help
    response = chatgpt.get_response("You are CliMate, an agri-weather coach. Greet the user and ask how you can help them.")
    response = "CliMate: " + response
    print(response)

    # Input loop to receive user queries
    while True:
        user_input = input("User: ")

        # Ask if the input is related to precipitation
        response = chatgpt.get_response(f"{user_input}, is this text related to precipitation? Respond with 'yes' or 'no'.")
        print(response)

        if response.lower().strip() == "yes":
            print("CliMate: Yes, it seems to be related to precipitation.")
        else:
            # If not precipitation-related, give a shorter response about inability to help
            response = chatgpt.get_response(
                f"You are CliMate, an agri-weather coach. Respond to the user that you can't help with their request: {user_input}, in a concise manner."
            )
            response = "CliMate: " + response
            print(response)

if __name__ == "__main__":
    main()
