import subprocess
import os

class VideoConverter:
    def __init__(self, input_file, output_file):
        if not isinstance(input_file, str) or not isinstance(output_file, str):
            raise TypeError("input_file and output_file must be strings")
        
        self.input_file = input_file
        self.output_file = output_file

    def convert_to_mp3(self):
        try:
            # Command to convert the file
            command = ['ffmpeg', '-i', self.input_file, '-q:a', '0', '-map', 'a', self.output_file]
            print(f"Executing command: {' '.join(command)}")
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            print(f"FFmpeg output:\n{result.stdout}")
            print(f"FFmpeg error:\n{result.stderr}")
            print(f"Conversion successful: {self.output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error during conversion with FFmpeg: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        # Delete the downloaded video file after conversion
        if os.path.exists(self.input_file):
            try:
                print(f"Attempting to delete the file: {self.input_file}")
                os.remove(self.input_file)
                print(f"File deleted: {self.input_file}")
            except Exception as e:
                print(f"Error deleting the file: {e}")
