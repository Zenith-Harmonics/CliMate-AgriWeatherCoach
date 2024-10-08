# **CliMate: An Agri-Weather Coach**

This is a simple demonstration project developed for the **NASA Space Apps Challenge 2024**. The goal is to connect a conversational AI (Large Language Model) with a weather API to provide weather-related insights for agricultural purposes.

In an experimental approach, we tried to let ChatGPT handle as much of the process as possible by leveraging its natural language understanding and task automation capabilities. The key idea was to minimize manual coding and intervention while maximizing the AI’s ability to interpret user requests, fetch data, and generate actionable insights.

## **Project Overview**

**CliMate** is an agri-weather assistant that allows users to ask weather-related questions and get useful information based on real-time data. By combining the power of a natural language model and weather data, CliMate helps users make informed farming decisions.

## **Features**
- Provides weather data for a specific location.
- Offers insights related to precipitation and flooding risks.
- Simple conversation-based interaction.

## **Tech Stack**
- **Python**: Main programming language.
- **OpenAI API**: For the Large Language Model (LLM).
- **METEOMATICS API**: For retrieving weather data.

## **Setup and Installation**

### **Requirements**
- Python 3.8 or higher.
- API keys for OpenAI (ChatGPT) and METEOMATICS.

### **Steps**
1. Create a `.env` file and add your API keys:
    ```
    METEOMATICS_USERNAME=your_meteomatics_username
    METEOMATICS_PASSWORD=your_meteomatics_password
    CHATGPT_API_KEY=your_chatgpt_api_key
    ```

2. Run the program:
    ```bash
    python main.py
    ```

## **How It Works**

1. Start the program and interact with the CliMate assistant.
2. Enter a location (city and country), and the assistant will fetch weather data.
3. Get insights based on precipitation levels for farming.

## **Contributing**

This project is for demonstration purposes, but contributions are welcome! Feel free to fork, make changes, and submit a pull request.

## **License**

This project is licensed under the MIT License.
