import openai
import speech_recognition as sr
import pyttsx3
import os
import time

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set OpenAI API key
openai.api_key = "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"  # Replace with your OpenAI API key


# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to listen to the microphone
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return None


# Function to get the response from OpenAI's API
def chat(query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}],
            temperature=0.7,
            max_tokens=150
        )
        answer = response['choices'][0]['message']['content'].strip()
        print(f"Jarvis: {answer}")
        speak(answer)
    except openai.error.InvalidRequestError as e:
        print(f"Error with OpenAI API request: {e}")
        speak("Sorry, I encountered an error with the request.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        speak("Sorry, something went wrong.")


# Main function to run the assistant
def main():
    print("Welcome to Jarvis A.I")
    speak("Welcome to Jarvis A.I. How can I assist you today?")
    while True:
        query = listen()
        if query:
            if "stop" in query or "exit" in query:
                print("Goodbye!")
                speak("Goodbye!")
                break
            chat(query)
        time.sleep(1)


# Run the program
if __name__ == "__main__":
    main()
