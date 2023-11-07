from pytube import  YouTube

def download_youtube_video(video_url, storage_location):
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}...")

        # Download the video to the specified storage location
        video.download(storage_location)
        print("Download complete!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Input the YouTube video URL
    video_url = input("Enter the YouTube video URL: ")

    # Input the storage location for the downloaded video
    storage_location = input("Enter the storage location (absolute path): ")

    download_youtube_video(video_url, storage_location)
