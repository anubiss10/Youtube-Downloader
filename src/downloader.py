import yt_dlp as youtube_dl

class YouTubeDownloader:
    def __init__(self, url):
        self.url = url

    def download_video(self, output_path):
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{output_path}/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'ffmpeg_location': './ffmpeg/bin',  # Specify the location of ffmpeg here
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(self.url, download=True)
                video_file = ydl.prepare_filename(info_dict)
                return video_file
        except Exception as e:
            print(f"Error downloading the video: {e}")
            return None
