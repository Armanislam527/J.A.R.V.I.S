import os
import speech_recognition as sr
import webbrowser
import subprocess
import sys
import datetime


# Function to speak out the given text
def say(text):
    os.system(f"espeak '{text}'")


# Function to take voice input and convert it to text
def takecomand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Listening...")
        try:
            print("Recognizing...")
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-us")
            print(f"User said: {query}")
            return query  # Return the recognized text
        except sr.UnknownValueError:
            print("Sorry, I could not understand that.")
            return None  # Return None if speech recognition fails
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
            return None


# Main execution
if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am Jarvis A.I.")
    sites = [
        ["YouTube", "https://youtube.com"],
        ["Wikipedia", "https://wikipedia.org"],
        ["Google", "https://google.com"],
        ["Facebook", "https://facebook.com"],
        ["Twitter", "https://twitter.com"],
        ["Instagram", "https://instagram.com"],
        ["LinkedIn", "https://linkedin.com"],
        ["Reddit", "https://reddit.com"],
        ["Amazon", "https://amazon.com"],
        ["eBay", "https://ebay.com"],
        ["Netflix", "https://netflix.com"],
        ["Hulu", "https://hulu.com"],
        ["Twitch", "https://twitch.tv"],
        ["Spotify", "https://spotify.com"],
        ["Stack Overflow", "https://stackoverflow.com"],
        ["GitHub", "https://github.com"],
        ["Coursera", "https://coursera.org"],
        ["Khan Academy", "https://khanacademy.org"],
        ["Udemy", "https://udemy.com"],
        ["Duolingo", "https://duolingo.com"],
        ["BBC", "https://bbc.com"],
        ["CNN", "https://cnn.com"],
        ["The New York Times", "https://nytimes.com"],
        ["The Guardian", "https://theguardian.com"],
        ["National Geographic", "https://nationalgeographic.com"],
        ["Pinterest", "https://pinterest.com"],
        ["Medium", "https://medium.com"],
        ["Quora", "https://quora.com"],
        ["IMDb", "https://imdb.com"],
        ["Rotten Tomatoes", "https://rottentomatoes.com"],
        ["Microsoft", "https://microsoft.com"],
        ["Apple", "https://apple.com"],
        ["Adobe", "https://adobe.com"],
        ["Dropbox", "https://dropbox.com"],
        ["Zoom", "https://zoom.us"],
        ["Slack", "https://slack.com"],
        ["WhatsApp", "https://whatsapp.com"],
        ["Telegram", "https://telegram.org"],
        ["Discord", "https://discord.com"],
        ["PayPal", "https://paypal.com"],
        ["Stripe", "https://stripe.com"],
        ["WordPress", "https://wordpress.com"],
        ["Blogger", "https://blogger.com"],
        ["Fiverr", "https://fiverr.com"],
        ["Upwork", "https://upwork.com"],
        ["Canva", "https://canva.com"],
        ["Pixabay", "https://pixabay.com"],
        ["Pexels", "https://pexels.com"],
        ["Unsplash", "https://unsplash.com"],
        ["Behance", "https://behance.net"],
        ["Dribbble", "https://dribbble.com"],
        ["DeviantArt", "https://deviantart.com"],
        ["SoundCloud", "https://soundcloud.com"],
        ["Bandcamp", "https://bandcamp.com"],
        ["Crunchyroll", "https://crunchyroll.com"],
        ["Vimeo", "https://vimeo.com"],
        ["TED", "https://ted.com"],
        ["WolframAlpha", "https://wolframalpha.com"],
        ["NASA", "https://nasa.gov"],
        ["World Health Organization", "https://who.int"],
        ["CDC", "https://cdc.gov"],
        ["UNICEF", "https://unicef.org"],
        ["UNESCO", "https://unesco.org"],
        ["GitLab", "https://gitlab.com"],
        ["Bitbucket", "https://bitbucket.org"],
        ["OpenAI", "https://openai.com"],
        ["Mozilla", "https://mozilla.org"],
        ["DuckDuckGo", "https://duckduckgo.com"],
        ["Yandex", "https://yandex.com"],
        ["Baidu", "https://baidu.com"],
        ["AliExpress", "https://aliexpress.com"],
        ["Etsy", "https://etsy.com"],
        ["Walmart", "https://walmart.com"],
        ["Target", "https://target.com"],
        ["Best Buy", "https://bestbuy.com"],
        ["Dropbox", "https://dropbox.com"],
        ["WeTransfer", "https://wetransfer.com"],
        ["Mega", "https://mega.nz"],
        ["Box", "https://box.com"],
        ["Coursera", "https://coursera.org"],
        ["EdX", "https://edx.org"],
        ["Udacity", "https://udacity.com"],
        ["Codecademy", "https://codecademy.com"],
        ["DataCamp", "https://datacamp.com"],
        ["Kaggle", "https://kaggle.com"],
        ["HackerRank", "https://hackerrank.com"],
        ["Codeforces", "https://codeforces.com"],
        ["LeetCode", "https://leetcode.com"],
        ["Cloudflare", "https://cloudflare.com"],
        ["Heroku", "https://heroku.com"],
        ["DigitalOcean", "https://digitalocean.com"],
        ["AWS", "https://aws.amazon.com"],
        ["Google Cloud", "https://cloud.google.com"],
        ["Azure", "https://azure.microsoft.com"],
        ["Weather.com", "https://weather.com"],
        ["AccuWeather", "https://accuweather.com"]
    ]
    # Listen for command and speak the recognized text
    while True:
        print("Say the word you want to speal it out by computer")
        s = takecomand()
        if s is None:  # Skip if the command is invalid
            continue
        site_opened = False
        for site in sites:
            if site[0].lower() in s.lower():
                say(f"Opening {site[0]}, Sir...")
                webbrowser.open(site[1])
                site_opened = True
                break  # Exit the loop after opening a site
        if site_opened:
            continue
        if "exit" in (s or "").lower() or "stop" in (s or "").lower() or "close" in (s or ""):
            print("Goodbye, Sir.")
            say("Goodbye, Sir.")
            break
        if "Open video".lower() in s:
            musicpath = "/home/arman/arman/github/firstrep/audio.mp3"
            # opener="open" if sys.platform =="darwin" else "xdg-open"
            # subprocess.call([opener, musicpath])
            os.system(f"open {musicpath}")
        if "the time" in s:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            sec = datetime.datetime.now().strftime("%S")
            say(f"Sir time is (hour) hr (min) minutes (sec) seconds")  # say(query)
            os.system("google-chrome https://www.google.com")
        if "Open terminal" in (s or "").lower():
            os.system("gnome-terminal")
say(s)
