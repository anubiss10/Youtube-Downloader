import tkinter as tk
from tkinter import filedialog, messagebox
from downloader import YouTubeDownloader
from converter import VideoConverter
import os

class YouTubeDownloaderApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("YouTube to MP3 Downloader")
        self.create_widgets()

    def create_widgets(self):
        # Label and entry field for the URL
        self.url_label = tk.Label(self.window, text="YouTube URL:")
        self.url_label.pack()

        self.url_entry = tk.Entry(self.window, width=50)
        self.url_entry.pack()

        # Button to select the output folder
        self.output_label = tk.Label(self.window, text="Output Folder:")
        self.output_label.pack()

        self.output_path_button = tk.Button(self.window, text="Select Folder", command=self.select_output_path)
        self.output_path_button.pack()

        self.output_path_label = tk.Label(self.window, text="")
        self.output_path_label.pack()

        # Button to start download and conversion
        self.download_button = tk.Button(self.window, text="Download and Convert", command=self.download_and_convert)
        self.download_button.pack()

    def select_output_path(self):
        self.output_path = filedialog.askdirectory()
        self.output_path_label.config(text=self.output_path)

    def download_and_convert(self):
        url = self.url_entry.get()
        if not url or not hasattr(self, 'output_path'):
            messagebox.showwarning("Warning", "Please enter a valid URL and select an output folder.")
            return

        # Download the video
        downloader = YouTubeDownloader(url)
        video_file = downloader.download_video(self.output_path)

        if video_file:
            try:
                # Convert the file to MP3
                mp3_file = os.path.splitext(video_file)[0] + ".mp3"
                converter = VideoConverter(video_file, mp3_file)
                converter.convert_to_mp3()

                if os.path.exists(mp3_file):
                    messagebox.showinfo("Success", f"Download and conversion completed: {mp3_file}")
                else:
                    raise FileNotFoundError(f"MP3 file was not created correctly: {mp3_file}")

            except Exception as e:
                messagebox.showerror("Conversion Error", f"Error during conversion: {e}")
        else:
            messagebox.showerror("Error", "Error downloading the video.")

    def run(self):
        self.window.mainloop()
