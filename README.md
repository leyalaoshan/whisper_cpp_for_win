# whisper_cpp_for_win
whisper.cpp for windows


以下是你的內容轉換為 Markdown 格式：

# Windows 11 安裝 Whisper.cpp 使用我的腳本製作 SRT YouTube 字幕

## 1. 安裝 Choco

打開 **Terminal (PowerShell 管理員)**，執行以下指令：

```powershell
Set-ExecutionPolicy Bypass -Scope CurrentUser -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

重新打開 Terminal。

⸻

2. 安裝 CMake

choco install cmake



⸻

3. 安裝 Git

choco install git -y



⸻

4. 安裝 Visual Studio Code

可選擇安裝：

choco install vscode



⸻

5. 安裝 Visual Studio 2022

choco install visualstudio2022community --package-parameters "--add Microsoft.VisualStudio.Workload.NativeDesktop --includeRecommended"

初始化 Visual Studio 2022

& "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64



⸻

6. 安裝 CUDA

從 官網 下載並安裝。

⸻

7. 安裝 Miniconda

從 官網 下載並安裝。
安裝完成後執行：

conda init

重啟 Terminal。

⸻

8. 下載 Whisper.cpp 檔案

cd D:
git clone https://github.com/ggerganov/whisper.cpp.git
cd whisper.cpp



⸻

9. 下載模型

models\download-ggml-model.cmd ggml-large-v3-turbo.bin



⸻

10. 編譯檔案

cmake -S . -B build -DGGML_CUDA=ON
cd D:\whisper.cpp\build
cmake --build . --config Release



⸻

11. 創建 Conda 虛擬環境

conda create --name whisper python=3.9
conda activate whisper

安裝依賴：

pip install yt-dlp
choco install ffmpeg



⸻

12. 執行

python main.py
