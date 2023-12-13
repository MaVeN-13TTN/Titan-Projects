import logging
import os
import re
from pytube import Playlist, YouTube
from tqdm import tqdm
from threading import Thread, Lock
import pytube.exceptions
from requests.exceptions import ConnectionError
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

MAX_RETRIES = 5

def download_video(video_url, storage_location, num_threads, block_size, lock):
    try:
        video = YouTube(video_url)
        video_title = video.title
        highest_resolution_stream = video.streams.get_highest_resolution()

        safe_video_title = "".join(
            c if c.isalnum() or c in [" ", "-", "_"] else "_" for c in video_title
        )
        video_path = os.path.join(storage_location, f"{safe_video_title}.mp4")

        retries = 0
        while retries < MAX_RETRIES:
            try:
                highest_resolution_stream.download(output_path=storage_location)
                break
            except (http.client.IncompleteRead, ConnectionError) as e:
                logging.warning(f"Retrying download due to error: {e}")
                retries += 1
                time.sleep(2 ** retries)

        logging.info(f"Downloaded video: {video_title}")

    except pytube.exceptions.PytubeError as e:
        logging.error(f"An error occurred while downloading video: {e}")

def download_playlist(playlist_url, storage_location, num_threads=8, block_size=4096):
    logger = logging.getLogger(__name__)

    try:
        playlist = Playlist(playlist_url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

        if not playlist.playlist_id:
            logger.error("Unexpected error parsing the playlist URL.")
            return

        playlist_title = playlist.title
        safe_playlist_title = "".join(
            c if c.isalnum() or c in [" ", "-", "_"] else "_" for c in playlist_title
        )
        storage_location = os.path.join(storage_location, safe_playlist_title)
        os.makedirs(storage_location, exist_ok=True)

        logger.info(f"Downloading playlist: {playlist_title}...")

        threads = []
        lock = Lock()

        for video_url in playlist.video_urls:
            video_thread = Thread(
                target=download_video,
                args=(video_url, storage_location, num_threads, block_size, lock),
            )
            threads.append(video_thread)
            video_thread.start()

        for thread in threads:
            thread.join()

        logger.info("Playlist download complete!")

    except pytube.exceptions.PytubeError as e:
        logger.error(f"An error occurred while downloading the playlist: {e}")

if __name__ == "__main__":
    playlist_url = input("Enter the URL of the YouTube playlist: ")
    download_location = input("Enter the download location: ").strip()
    download_playlist(playlist_url, download_location)
