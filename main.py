from openai import OpenAI

from config import API_KEY

client = OpenAI(api_key=API_KEY)

def speechToText():
    audio_file = open("test.mp3", "rb")
    transcript = client.audio.transcriptions.create(
        file=audio_file,
        model="whisper-1",
        response_format="verbose_json",
        timestamp_granularities=["word"]
    )
    print(transcript.words)
    for word_info in transcript.words:
        print(word_info['word'])

if __name__ == '__main__':
    speechToText()

