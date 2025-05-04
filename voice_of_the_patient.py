import logging
import pyaudio
import wave
import soundfile as sf

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=5, phrase_time_limit=None):
    """
    Function to record audio from the microphone and save it as a WAV file using soundfile.

    Args:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Maximum time to record (in seconds).
    phrase_time_limit (int): Maximum time for the phrase to be recorded (in seconds).
    """
    try:
        # Initialize PyAudio
        p = pyaudio.PyAudio()

        # Define audio stream parameters
        format = pyaudio.paInt16  # 16-bit audio
        channels = 1  # Mono
        rate = 44100  # Sample rate (44.1 kHz)
        frames_per_buffer = 1024  # Number of frames per buffer

        logging.info("Opening audio stream...")
        stream = p.open(format=format,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=frames_per_buffer)

        frames = []
        logging.info("Recording...")

        # Record audio for the specified timeout
        for _ in range(0, int(rate / frames_per_buffer * timeout)):
            data = stream.read(frames_per_buffer)
            frames.append(data)

        logging.info("Recording complete.")

        # Stop and close the audio stream
        stream.stop_stream()
        stream.close()

        # Convert frames to raw audio data
        raw_data = b''.join(frames)

        # Write the raw audio data to a temporary WAV file
        with wave.open('temp_recorded_audio.wav', 'wb') as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(format))
            wf.setframerate(rate)
            wf.writeframes(raw_data)

        # Now, read the temporary WAV file using soundfile and save it to the final file path
        data, samplerate = sf.read('temp_recorded_audio.wav')

        # Write the audio to the final file path as a WAV file
        sf.write(file_path, data, samplerate)

        logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Usage
audio_filepath = "patient_voice_test_for_patient.wav"
record_audio(file_path=audio_filepath)


#Step2: Setup Speech to text–STT–model for transcription
# Step 2: Setup Speech-to-Text (STT) using Groq's Whisper Model
import os
import logging
from groq import Groq

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set your Whisper model and API key (ensure this is set properly)
stt_model = "whisper-large-v3"
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")  # Or hardcode temporarily for testing

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    """
    Transcribe an audio file using Groq's Whisper model.
    
    Args:
        stt_model (str): The Whisper model to use.
        audio_filepath (str): Path to the audio file.
        GROQ_API_KEY (str): Your Groq API key.
    
    Returns:
        str: The transcribed text.
    """
    try:
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is not set. Please set it in your environment or hardcode it.")

        if not os.path.exists(audio_filepath):
            raise FileNotFoundError(f"Audio file not found at {audio_filepath}")

        client = Groq(api_key=GROQ_API_KEY)
        logging.info(f"Transcribing audio using model '{stt_model}'...")

        with open(audio_filepath, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model=stt_model,
                file=audio_file,
                language="en"
            )

        logging.info("Transcription complete.")
        return transcription.text

    except Exception as e:
        logging.error(f"Transcription failed: {e}")
        return None

# Example usage
audio_filepath = "patient_voice_test_for_patient.wav"
transcribed_text = transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY)

if transcribed_text:
    print("\n Transcribed Text:\n", transcribed_text)
else:
    print("\n  Failed to transcribe audio.")