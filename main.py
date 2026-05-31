import os
import subprocess
import requests

# === CONFIGURATION ===
ROOT_DIR = r"F:\Path\To\Your\Video\Folders" # Change this to your folder root
AUDIO_STREAM_INDEX = 0

# Adjust time range to extract from each video
START_TIME = "00:25:00"
END_TIME = "00:35:00"

OUTPUT_MP3 = "output.mp3"

# IMPORTANT: Get your own CSRF token from https://accentgenerator.com
CSRF_TOKEN = 'your-own-token-here'
API_URL = 'https://accentgenerator.com/detectLanguageTranslate/'

VIDEO_EXTENSIONS = ('.mkv', '.mp4', '.avi', '.mov')

GREEN = '\033[92m'
RESET = '\033[0m'

def extract_audio(video_path, output_path):
    """Uses ffmpeg to extract a 29-minute audio segment to MP3."""
    cmd = [
        "ffmpeg",
        "-ss", START_TIME,
        "-to", END_TIME,
        "-i", video_path,
        "-map", f"0:a:{AUDIO_STREAM_INDEX}",
        "-b:a", "192k",
        "-vn",
        output_path,
        "-y"
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        print(f"Error extracting audio from {video_path}")
        return False

def detect_language(file_path):
    """Sends the audio file to the API and prints language detection results."""
    try:
        with open(file_path, 'rb') as f:
            files = {
                'audioFile': (os.path.basename(file_path), f, 'audio/mpeg')
            }

            headers = {
                'Referer': 'https://accentgenerator.com/ai-detect-language/',
                'Origin': 'https://accentgenerator.com',
                'User-Agent': 'Mozilla/5.0',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': CSRF_TOKEN
            }

            cookies = {
                'csrftoken': CSRF_TOKEN
            }

            response = requests.post(API_URL, files=files, headers=headers, cookies=cookies)
            result = response.json()

            print(f"{GREEN}Language Detected: {result.get('languageName')} ({result.get('languageCode')}){RESET}")
            print("Transcript:")
            print(result.get('translatedText'))
            print(f"From File: {file_path}\n")

    except Exception as e:
        print(f"Language detection failed for {file_path}")
        print("Exception:", e)

def process_folder(folder_path):
    """Processes only the first valid video file in a folder."""
    for file in os.listdir(folder_path):
        if file.lower().endswith(VIDEO_EXTENSIONS):
            video_path = os.path.join(folder_path, file)
            print(f"\n=== Extracting from: {video_path} ===")
            if extract_audio(video_path, OUTPUT_MP3):
                detect_language(OUTPUT_MP3)
                try:
                    os.remove(OUTPUT_MP3)
                except Exception as e:
                    print("Could not delete temporary audio:", e)
            break  # Only process the first video file

def scan_and_process(root):
    for dirpath, _, _ in os.walk(root):
        process_folder(dirpath)

if __name__ == "__main__":
    scan_and_process(ROOT_DIR)
