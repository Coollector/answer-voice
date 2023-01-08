import keyboard # module for detecting keyboard input
import speech_recognition as sr # module for speech recognition
import pyttsx3 # module for text-to-speech
import openai # module for accessing OpenAI API

# Set up the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()
openai.api_key = "YOUR API KEY HERE"
while True:
    print("waiting")
    # Wait for a keyboard combination to be pressed
    keyboard.wait('shift+alt+a')
    print("recording")
    # Record 5 seconds of audio from the default microphone
    with sr.Microphone() as source:
        audio = r.listen(source)
    # Transcribe the audio into English text
    text = r.recognize_google(audio, language='en-US')
    print("recorded: "+text)

    # Use the OpenAI API to get an answer to the text
    answer = openai.Completion.create(engine="text-davinci-003", prompt=text, max_tokens=1024, n=1,stop=None,temperature=0.5).choices[0].text

    # Read the answer out loud
    engine.say(answer)
    engine.runAndWait()
