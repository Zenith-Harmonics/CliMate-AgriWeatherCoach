from chatGPT import gpt


def main():
    chatgpt = gpt.GPT()

    response = chatgpt.get_response("You are CliMAte, an agri weather coach and now you greet the user and ask him how can you help it")
    print(response)


if __name__ == "__main__":
    main()