import os
import subprocess
from subprocess import CalledProcessError


# Executables differ between Windows and other platforms
YT_DLP = "yt-dlp.exe" if os.name == "nt" else "yt-dlp"
FFMPEG = "ffmpeg.exe" if os.name == "nt" else "ffmpeg"
WHISPER_CLI = (
    r"D:\whisper.cpp\build\bin\Release\whisper-cli.exe"
    if os.name == "nt"
    else "whisper-cli"
)


def download_and_convert(url: str) -> None:
    """Download audio from YouTube, convert it and run whisper-cli.

    Temporary files are cleaned up even if any step fails.
    """

    audio_mp3 = "audio.mp3"
    audio_wav = "audio.wav"
    try:
        # Step 1: Download the audio from the YouTube video
        command1 = [YT_DLP, "-x", "--audio-format", "mp3", "-o", audio_mp3, url]
        subprocess.run(command1, check=True)

        # Step 2: Convert the audio to a different format
        command2 = [
            FFMPEG,
            "-i",
            audio_mp3,
            "-ar",
            "16000",
            "-ac",
            "1",
            "-b:a",
            "96K",
            "-acodec",
            "pcm_s16le",
            audio_wav,
        ]
        subprocess.run(command2, check=True)

        # Step 3: Run the whisper-cli executable
        command3 = [
            WHISPER_CLI,
            "-m",
            r"D:\whisper.cpp\models\ggml-large-v3-turbo.bin",
            "-l",
            "zh",
            "-osrt",
            "-f",
            audio_wav,
        ]
        subprocess.run(command3, check=True)
    except CalledProcessError as exc:
        print(f"An external command failed: {exc}")
    finally:
        # Delete temporary files if they exist
        for fname in (audio_mp3, audio_wav):
            if os.path.exists(fname):
                os.remove(fname)

if __name__ == "__main__":
    url = input("Enter the YouTube URL: ")
    download_and_convert(url)
