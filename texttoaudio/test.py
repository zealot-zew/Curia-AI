'''this version of text to audio is very slow need to be 
optimised using gpu in the future, probably using cuda'''

import whisper

# Load model (small/medium/large for better accuracy)
model = whisper.load_model("small")

# Transcribe an audio file
result = model.transcribe("TestAudio.mp3")

print("Transcribed Text:\n", result["text"])