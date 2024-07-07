from flask import Flask, render_template, request, jsonify
import os
import re
from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY", "your secret api code")
client = OpenAI(api_key=api_key)

app = Flask(__name__)

def transcribe_audio_with_whisper(file_path):
    audio_file = open(file_path, "rb")
    transcription = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
    )
    return transcription

def create_mermaid_diagram(inputText):
    response = client.chat.completions.create(
        model="gpt-4",
        response_format={ "type": "text" },
        messages=[
            {"role": "system", "content": "You are an expert in converting text descriptions into Mermaid.js diagrams. Based on the input, choose the most appropriate diagram type (e.g., flowchart, sequence diagram, class diagram, etc.) and generate the corresponding Mermaid code. Only provide the Mermaid code without any additional explanations."},
            {"role": "user", "content": inputText}])
    
    return response.choices[0].message.content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_audio', methods=['POST'])
def process_audio():
    try:
        audio_file = request.files['audioFile']
        temp_audio_path = '/tmp/uploaded_audio.wav'
        audio_file.save(temp_audio_path)
        transcription = transcribe_audio_with_whisper(temp_audio_path)
        os.remove(temp_audio_path)
        return jsonify({'transcription': transcription}), 200

    except Exception as e:
        print(f"Error processing audio: {str(e)}")
        return jsonify({'error': str(e)}), 500
    
@app.route('/generate_diagram', methods=['POST'])
def generate_diagram():
    try:
        input_text = request.form.get('text')

        if not input_text:
            raise ValueError("Input text is missing or empty")

        mermaid_code = create_mermaid_diagram(input_text)
        cleaned_mermaid_code = re.sub(r'^```mermaid\s*|\s*```\s*$', '', mermaid_code, flags=re.MULTILINE)

        return jsonify({'mermaid_code': cleaned_mermaid_code}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
