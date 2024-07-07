# Voice2Diagram
A web application that converts spoken language or uploaded audio files into visual diagrams using AI-powered transcription and diagram generation.

## Features

- Audio recording directly from the browser and audio file upload support (Whisper API: .mp3, .mp4, .mpeg, .mpga , .m4a, and .wav)
- Conversion of transcribed text to Mermaid.js diagram code
- Live editing of diagram code with instant visual updates

## Requirements
- OpenAI API Key

## Setup

1. Clone the repository
2. Install the required packages: `pip install -r requirements.txt`
4. Set up your OpenAI API key:
- Create a `.env` file in the project root
- Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`
4. Run the Flask application
- `python app.py`
5. Open a web browser and navigate to `http://localhost:5000`


## Usage
1. **Record Audio**: Click the "Record Audio" button to start recording. Click again to stop. Make sure to allow the usage of your microphone from the browser.
2. **Upload Audio**: Alternatively, use the file upload option as an audio file input.
3. **Process Audio**: Click "Process Audio" to transcribe the audio to text.
4. **Generate Diagram**: The transcribed text will appear in the text area where it can be double-checked and edited. Click "Generate Diagram" to create a MermaidJS diagram from this text.
5. **Edit Diagram**: You can edit the Mermaid code directly in the text area. The diagram will update in real-time. most of the time.
