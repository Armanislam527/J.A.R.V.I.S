from google.cloud import language_v1
import speech_recognition as sr
import pyttsx3
import os
import time

# Initialize credentials (replace with your service account key file path)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/keyfile.json"

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Initialize Language client
client = language_v1.LanguageServiceClient()


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


# Function to get the response from Google Cloud's Language API
def chat(query):
    document = language_v1.Document(
        content=query,
        type_=language_v1.Document.Type.PLAIN_TEXT,
    )

    try:
        # Analyze the sentiment of the text
        sentiment = client.analyze_sentiment(request={"document": document}).document_sentiment

        # Generate a simple response based on sentiment 
        if sentiment.score > 0.5:
            response = "That sounds positive!"
        elif sentiment.score < -0.5:
            response = "That sounds negative."
        else:
            response = "I understand."

        print(f"Jarvis: {response}")
        speak(response)

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
