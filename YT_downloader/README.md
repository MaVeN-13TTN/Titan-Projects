# YouTube Video Downloader

This Python script allows you to download YouTube videos with ease. It utilizes the `pytube` library to interact with YouTube's API and `requests` for downloading content in chunks. The progress of the download is displayed using the `tqdm` library.

## Features

- **Threaded Downloading:** The script employs multiple threads to download video chunks concurrently, enhancing download speed.
- **URL Validation:** Ensures that the provided URL is a valid YouTube video URL.
- **Sanitized Filenames:** Video titles are sanitized to ensure compatibility with file systems.
- **Progress Tracking:** Utilizes the `tqdm` library to display a progress bar for visualizing the download progress.

## Prerequisites

Make sure to install the required libraries before running the script. You can install them using the following:

```bash
pip install pytube requests tqdm
```

## Usage

1. Run the script.
2. Enter the YouTube video URL when prompted.
3. Provide the absolute path for the storage location.
4. Enjoy your downloaded video!

## Example

```python
python youtube_downloader.py
```

## Notes

- The script assumes a valid internet connection and may not work with restricted or private videos.
- Always respect YouTube's terms of service and copyright laws when downloading videos.

**Disclaimer:** This script is for educational purposes only. Downloading copyrighted material without permission may violate terms of service and copyright laws. Use it responsibly and ethically.