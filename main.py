from chatGPT import gpt


def main():
    chatgpt = gpt.GPT()
    print(chatgpt.get_response())


if __name__ == "__main__":
    main()