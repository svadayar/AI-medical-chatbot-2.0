import os
import pygame
from gtts import gTTS
from elevenlabs.client import ElevenLabs

# Step1a: Setup Text to Speech–TTS–model with gTTS
def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)

    pygame.mixer.init()
    pygame.mixer.music.load(output_filepath)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Step1b: Setup Text to Speech–TTS–model with ElevenLabs
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    from elevenlabs.client import ElevenLabs

    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio_stream = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )

    # Write the streamed audio chunks to a file
    with open(output_filepath, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)

    # Play using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(output_filepath)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Main section
input_text = "Hello, this is AI speaking from both gTTS and ElevenLabs!"

# Using gTTS
# output_filepath_gtts = "gtts_output.mp3"
# text_to_speech_with_gtts(input_text, output_filepath_gtts)

# Using ElevenLabs
output_filepath_elevenlabs = "elevenlabs_output.mp3"
text_to_speech_with_elevenlabs(input_text, output_filepath_elevenlabs)