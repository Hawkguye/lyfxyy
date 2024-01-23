from openai import OpenAI
from pathlib import Path
from pygame import mixer
import os
import time

os.environ["http_proxy"] = "http://127.0.0.1:4465"
os.environ["https_proxy"] = "http://127.0.0.1:4465"


client = OpenAI(
    api_key="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"
)

reply = input("Input: ")

output = input("output name: ")

speech_file_path = Path(__file__).parent / f"{output}.mp3"

voiceResponse = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=reply
)

voiceResponse.stream_to_file(speech_file_path)

print("Successfully outputed to " + str(speech_file_path))

mixer.init()
mixer.music.load(speech_file_path)
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)

