import sys
from pathlib import Path
from unittest.mock import patch, call

sys.path.append(str(Path(__file__).resolve().parent.parent))
import main


def test_download_and_convert_invokes_tools_and_cleans_files():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    with patch("main.subprocess.run") as mock_run, \
         patch("main.os.remove") as mock_remove, \
         patch("main.os.path.exists", return_value=True), \
         patch("main.YT_DLP", "yt-dlp.exe"), \
         patch("main.FFMPEG", "ffmpeg.exe"), \
         patch("main.WHISPER_CLI", "whisper-cli.exe"):
        main.download_and_convert(url)

    # subprocess.run should be called three times with the expected executables
    assert mock_run.call_count == 3
    assert mock_run.call_args_list[0].args[0][0] == "yt-dlp.exe"
    assert mock_run.call_args_list[1].args[0][0] == "ffmpeg.exe"
    assert mock_run.call_args_list[2].args[0][0] == "whisper-cli.exe"

    # temporary files should be removed
    assert mock_remove.call_args_list == [call("audio.mp3"), call("audio.wav")]

