# AI Medical Chatbot 2.0

AI Medical Chatbot 2.0 is an advanced conversational assistant designed to simulate interactions between patients and doctors.
It leverages speech-to-text, image analysis, and text-to-speech technologies to provide medical insights based on user input.

## Features

- **Voice Interaction**: Converts patient speech to text for processing.
- **Image Analysis**: Analyzes medical images to provide diagnostic suggestions.
- **Doctor Simulation**: Generates responses that mimic a professional doctor's advice.
- **Speech Output**: Converts the doctor's textual response back to speech for the patient.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [pipenv](https://pipenv.pypa.io/en/latest/) for managing virtual environments

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/svadayar/AI-medical-chatbot-2.0.git
   cd AI-medical-chatbot-2.0
   ```

2. **Install dependencies**:

   ```bash
   pipenv install
   ```

3. **Activate the virtual environment**:

   ```bash
   pipenv shell
   ```

## Usage

To run the chatbot application:

```bash
python gradio_app.py
```

This will launch a Gradio interface where you can interact with the chatbot by providing voice input and medical images.

## Project Structure

```
AI-medical-chatbot-2.0/
├── brain_of_the_doctor.py
├── voice_of_the_patient.py
├── voice_of_the_doctor.py
├── gradio_app.py
├── Pipfile
├── Pipfile.lock
├── .env
├── AI chatbot documentation.docx
├── sample_audio_files/
│   ├── patient_voice_test_for_patient.wav
│   └── temp_recorded_audio.wav
├── sample_image_files/
│   └── acne.jpeg
└── output_audio_files/
    ├── elevenlabs_output.mp3
    ├── elevenlabs_testing_autoplay.mp3
    ├── final.mp3
    ├── gtts_output.mp3
    └── gtts_testing.mp3
```

- **brain_of_the_doctor.py**: Handles image encoding and analysis.
- **voice_of_the_patient.py**: Manages speech-to-text conversion.
- **voice_of_the_doctor.py**: Handles text-to-speech conversion.
- **gradio_app.py**: Main application file that integrates all components using Gradio.
- **.env**: Contains environment variables such as API keys.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For more details, visit the [GitHub repository](https://github.com/svadayar/AI-medical-chatbot-2.0).
