from pytube import YouTube
import requests
from tqdm import tqdm
import os

def download_youtube_video(video_url, storage_location):
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}...")

        # Get the video stream URL
        video_url = video.url

        # Set up a progress bar
        response = requests.get(video_url, stream=True)
        total_size_in_bytes = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte

        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)

        # Download the video content and update the progress bar
        with open(os.path.join(storage_location, f"{yt.title}.mp4"), 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)

        # Close the progress bar
        progress_bar.close()

        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Input the YouTube video URL
    video_url = input("Enter the YouTube video URL: ")

    # Input the storage location for the downloaded video
    storage_location = input("Enter the storage location (absolute path): ")

    download_youtube_video(video_url, storage_location)
