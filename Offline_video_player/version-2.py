import os
import tkinter as tk
from tkinter import filedialog
import pygame
import traceback

# Function to initialize sound and handle potential errors
def init_sound():
    try:
        pygame.mixer.init()
        # Optional: Set desired audio output device (if applicable)
        # pygame.mixer.set_numchannels(desired_channels)
        return True
    except pygame.error as e:
        print(f"Error initializing sound: {e}")
        return False

# Function to load videos from the specified directory
def load_videos(directory):
    videos = []
    for file in os.listdir(directory):
        if file.endswith((".mp4", ".avi", ".mkv")):
            videos.append(file)
    return videos

# Function to handle video selection
def play_selected_video(event):
    index = video_list.curselection()[0]
    selected_video = video_list.get(index)
    video_path = os.path.join(download_directory, selected_video)
    play_video(video_path)

# Function to play the selected video
def play_video(video_path):
    try:
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Offline YouTube Video Player')
        pygame.mixer.music.load(video_path)
        pygame.mixer.music.play()
    except pygame.error as e:
        print("Error playing video:", e)


# Function to handle directory selection button click event
def select_directory_button_clicked():
    global download_directory
    download_directory = filedialog.askdirectory()
    if download_directory:
        videos = load_videos(download_directory)
        for video in videos:
            video_list.insert("end", video)

# Main function to create GUI and interact with the user
def main():
    global video_list, download_directory

    # Set up GUI
    root = tk.Tk()
    root.geometry("1000x800")
    root.title("Offline YouTube Video Player")

    # Directory Selection Section
    select_directory_button = tk.Button(root, text="Select Video Directory", command=select_directory_button_clicked)
    select_directory_button.pack()

    # Video List Section
    video_list_label = tk.Label(root, text="Select a video to play:")
    video_list_label.pack()
    video_list = tk.Listbox(root, selectmode="SINGLE")
    video_list.bind("<<ListboxSelect>>", play_selected_video)
    video_list.pack()

    root.mainloop()

if __name__ == "__main__":
    main()