# YouTube Video Downloader

This Python script allows you to download individual YouTube videos using the PyTube library. It supports multithreaded downloading for faster performance. Additionally, it provides an option to download videos in chunks using the `requests` library.

## Requirements

- Python 3
- PyTube library
- tqdm library
- requests library

## Usage

1. Install the required libraries:

   ```bash
   pip install pytube tqdm requests
   ```

2. Run the script:

   ```bash
   python youtube_video_downloader.py
   ```

3. Enter the YouTube video URL when prompted.

4. Enter the desired storage location (absolute path) when prompted.

5. The script will download the video to the specified location.

## Configuration

- Modify the `num_threads` and `block_size` parameters in the `download_youtube_video` function for customized multithreading settings.
- Adjust the logging level and format in the `logging.basicConfig` line based on your preferences.

## Troubleshooting

If you encounter issues while using the script, consider the following troubleshooting tips:

1. **Invalid URL:** Ensure that the provided YouTube video URL is correct and follows the standard format.

2. **Internet Connection:** The script relies on a stable internet connection. Check your internet connection if the download fails.

3. **Library Versions:** Make sure you have the latest versions of the required libraries. You can update them using the following command:

    ```bash
    pip install --upgrade pytube requests tqdm
    ```

## Library Overview

- **PyTube:** A Python library for downloading YouTube videos. It provides an easy-to-use interface to interact with YouTube's API.

- **Requests:** A popular Python library for making HTTP requests. It is used in this script for downloading video content in chunks.

- **tqdm:** A library for adding progress bars to your Python scripts. It enhances the user experience by visually tracking the download progress.

## Disclaimer

This script is for educational purposes only. Downloading copyrighted material without permission may violate terms of service and copyright laws. Use it responsibly and ethically.

# YouTube Playlist Downloader

This Python script allows you to download entire YouTube playlists using the PyTube library. It provides a multithreaded approach to efficiently download videos concurrently from a given playlist URL.

## Requirements

- Python 3
- PyTube library

## Usage

1. Install the required libraries:

   ```bash
   pip install pytube
   ```

2. Run the script:

   ```bash
   python youtube_playlist_downloader.py
   ```

3. Enter the YouTube playlist URL when prompted.

4. Enter the desired download location when prompted.

5. The script will download all videos from the playlist to the specified location.

## Configuration

- Adjust the `MAX_RETRIES` constant to control the maximum number of download retries in case of errors.
- Modify the `num_threads` and `block_size` parameters in the `download_playlist` function for customized multithreading settings.

## Disclaimer

This script is for educational purposes only. Respect YouTube's terms of service and copyright policies when using this tool.

## Notes

- The script assumes a valid internet connection and may not work with restricted or private videos.
- Always respect YouTube's terms of service and copyright laws when downloading videos.