# YouTube to MP3 Downloader

## Description

This application allows you to download YouTube videos and convert them to MP3 format. It features a simple graphical user interface (GUI) built with Tkinter for easy operation.

## Features

- Enter a YouTube URL to download the video.
- Select an output folder to save the downloaded video and converted MP3.
- Automatically convert the downloaded video to MP3 format using FFmpeg.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
Navigate to the project directory:

    ```bash
cd your-repo-name
Create a virtual environment (optional but recommended):
    ```
    ```bash
python -m venv venv
Activate the virtual environment:
    ```
On Windows:

    ```bash
 
venv\Scripts\activate
On macOS/Linux:

 ```bash
source venv/bin/activate
Install the required dependencies:
```
 ```bash
pip install -r requirements.txt
Ensure you have FFmpeg installed. If not, download and install it from FFmpeg's official site. Update the ffmpeg_location in downloader.py if necessary.
```