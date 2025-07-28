# 🎧 Audio Language Scanner

**Audio Language Scanner** is a Python tool that extracts a segment of audio from video files and uses [AccentGenerator](https://accentgenerator.com/) to detect the spoken language and provide a transcript.

---

## 🛠 Features

- Extracts audio from video formats: `.mp4`, `.mkv`, `.avi`, `.mov`
- Converts selected time segment to `.mp3` using FFmpeg
- Sends audio to AccentGenerator API
- Detects spoken language
- Returns translated transcript

---

## 📁 How It Works

- The script **recursively scans all subfolders** inside your specified root directory.
- It **only processes the first valid video file** found in each folder.
- The audio segment (e.g. minute 25–35) is extracted using `ffmpeg`.
- The output `.mp3` file is sent to AccentGenerator.com for detection and translation.

---

## 📂 Folder Structure Example

```
ROOT_DIR/
├── Movie1/
│   └── SomeFile.mkv     ← ✅ This file will be processed
├── Movie2/
│   ├── Cover.jpg         ← ❌ Ignored
│   └── Film.mp4          ← ✅ First valid video gets processed
```

> ⚠️ Only one video per folder is scanned — make sure each movie folder contains **one target video** as the first detectable file.

---

## ⚙️ Configuration

Open `main.py` and edit the following lines:

```python
# 👇 Path to your video collection
ROOT_DIR = r"F:\Path\To\Your\Video\Folders"

# ⏱️ Audio time range (HH:MM:SS)
START_TIME = "00:25:00"
END_TIME = "00:35:00"

# 🔐 CSRF Token from AccentGenerator.com
CSRF_TOKEN = 'your-own-token-here'
```

---

## 🔐 How to Get CSRF Token

1. Visit: [https://accentgenerator.com/ai-detect-language/](https://accentgenerator.com/ai-detect-language/)
2. Upload a small `.mp3` file
3. Open Developer Tools > Network tab
4. Find the request to `/detectLanguageTranslate/`
5. Copy the `csrftoken` from the **Headers** or **Cookies**

---

## ▶️ Usage

### ✅ Step 1: Install Dependencies

Make sure FFmpeg is installed and available in your system's PATH.  
Then install the required Python modules:

```bash
pip install -r requirements.txt
```

### ✅ Step 2: Run the Script

```bash
python main.py
```

### 💬 Example Output

```bash
=== Extracting from: F:\Movies\German\SomeMovie.mkv ===
Language Detected: German (de)
Transcript:
Hallo, willkommen bei diesem Film. Dies ist ein Beispieltext.
From File: output.mp3
```

---

## 📦 Requirements

- Python 3.6 or higher
- FFmpeg installed (`ffmpeg -version`)
- Internet connection
- Valid CSRF token from AccentGenerator

---

## 🧪 Tested On

- ✅ Windows 10/11
- ✅ Python 3.10
- ✅ PyCharm IDE

---

## 🪪 License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for full details.

> You must include attribution to the original project:  
> **"Audio Language Scanner by Ibrahim Irusham Rashad"** in your documentation or user interface if you distribute this software or any derivative work.

---

## 🙏 Acknowledgments

- [FFmpeg](https://ffmpeg.org/) — for the powerful audio/video toolkit
- [AccentGenerator](https://accentgenerator.com/) — for language detection and transcription service

> This project is not affiliated with or endorsed by AccentGenerator.com or FFmpeg. This tool is for educational and personal use only.
