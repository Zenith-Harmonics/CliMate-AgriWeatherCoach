from chatGPT import gpt
from meteomatics import meteom

def main():
    chatgpt = gpt.GPT()
    meteo = meteom.Meteomatics()

    #response = chatgpt.get_response("You are CliMAte, an agri weather coach and now you greet the user and ask him how can you help it")
    print(meteo.request())


if __name__ == "__main__":
    main()