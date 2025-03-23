import subprocess
import os

def download_and_convert(url):
    # Step 1: Download the audio from the YouTube video
    command1 = ["yt-dlp.exe", "-x", "--audio-format", "mp3", "-o", "audio.mp3", url]
    subprocess.run(command1, check=True)

    # Step 2: Convert the audio to a different format
    command2 = ["ffmpeg.exe", "-i", "audio.mp3", "-ar", "16000", "-ac", "1", "-b:a", "96K", "-acodec", "pcm_s16le", "audio.wav"]
    subprocess.run(command2, check=True)

    # Step 3: Run the whisper-cli executable
    command3 = ["D:\\whisper.cpp\\build\\bin\\Release\\whisper-cli.exe", "-m", "D:\\whisper.cpp\\models\\ggml-large-v3-turbo.bin", "-l", "zh", "-osrt", "-f", "audio.wav"]
    subprocess.run(command3, check=True)

    # Step 4: Delete temporary files
    os.remove("audio.mp3")
    os.remove("audio.wav")

if __name__ == "__main__":
    url = input("Enter the YouTube URL: ")
    download_and_convert(url)