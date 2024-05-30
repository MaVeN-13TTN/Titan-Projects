import logging
import os
from pytube import YouTube
import requests
from tqdm import tqdm
from urllib.parse import urlparse


def download_chunk(url, start, end, file):
    """
    Downloads a chunk of a file from a URL.

    Args:
        url: The URL of the file.
        start: The starting byte of the chunk.
        end: The ending byte of the chunk.
        file: The file object to write the downloaded data to.

    Returns:
        The number of bytes downloaded.
    """
    headers = {"Range": f"bytes={start}-{end}"}
    response = requests.get(url, headers=headers, stream=True)
    file.seek(start)
    file.write(response.content)
    return len(response.content)


def validate_url(url):
    """
    Checks if the provided URL is a valid YouTube video URL.

    Args:
        url: The URL to validate.

    Returns:
        True if the URL is valid, False otherwise.
    """
    return url.startswith("https://youtu.be/") or url.startswith(
        "https://www.youtube.com/watch?v="
    )


def download_youtube_video(video_url, storage_location, num_threads=8, block_size=4096):
    """
    Downloads a YouTube video to the specified location.

    Args:
        video_url: The URL of the YouTube video.
        storage_location: The location to save the downloaded video.
        num_threads: The number of threads to use for downloading.
        block_size: The size of each download chunk in bytes.
    """
    logger = logging.getLogger(__name__)

    # Validate the URL
    if not validate_url(video_url):
        print(f"Invalid YouTube video URL provided: {video_url}")
        logger.error("Invalid YouTube video URL provided.")
        return

    # Extract the video ID and sanitize the title
    parsed_url = urlparse(video_url)
    if parsed_url.netloc == "youtu.be":
        video_id = parsed_url.path[1:]
    elif parsed_url.netloc == "youtube.com" and parsed_url.path == "/watch":
        video_id = parsed_url.query.split("=")[1]
    else:
        logger.error("Unexpected error parsing the video URL.")
        return

    video_url = f"https://www.youtube.com/watch?v={video_id}"
    try:
        yt = YouTube(video_url)
        video = yt.streams.get_highest_resolution()
        video_title = yt.title

        # Sanitize the video title
        safe_video_title = "".join(
            c if c.isalnum() or c in [" ", "-", "_"] else "_" for c in video_title
        )
        file_path = os.path.join(storage_location, f"{safe_video_title}.mp4")

        logger.info(f"Downloading: {video_title}...")

        video_url = video.url
        response = requests.head(video_url)
        total_size_in_bytes = int(response.headers.get("content-length", 0))

        # Use `tqdm` for progress tracking
        progress_bar = tqdm(total=total_size_in_bytes, unit="iB", unit_scale=True)

        # Download video in chunks
        bytes_downloaded = 0
        with open(file_path, "wb") as file:
            with requests.get(video_url, stream=True) as req:
                req.raise_for_status()
                for chunk in req.iter_content(chunk_size=block_size):
                    if chunk:
                        file.write(chunk)
                        bytes_downloaded += len(chunk)
                        progress_bar.update(len(chunk))

        progress_bar.close()
        logger.info("Download complete!")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    video_url = input("Enter the YouTube video URL: ")
    storage_location = input("Enter the storage location (absolute path): ")

    download_youtube_video(video_url, storage_location)
