import os
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
from moviepy.editor import VideoFileClip


# Function to save the file
def save_file():
    input_directory = filedialog.askdirectory(title="Select where to save")
    path_label.config(text=input_directory)


# Function to download the video
def download_video():
    video_url = url_entry.get()
    output_directory = path_label.cget("text")

    if not video_url or not output_directory:
        messagebox.showerror(
            "Error", "Please provide a valid URL and output directory."
        )
        return

    try:
        print("Downloading... 🥱🥱")
        video = YouTube(video_url)
        stream = video.streams.get_highest_resolution()
        mp4 = stream.download(output_path=output_directory)

        video_clip = VideoFileClip(mp4)

        # Convert video to MP3 and move the MP3 file to the output directory
        audio_file = video_clip.audio
        audio_file.write_audiofile("audio.mp3")
        audio_file.close()

        # Move the MP3 file to the output directory
        shutil.move("audio.mp3", os.path.join(output_directory, "audio.mp3"))

        video_clip.close()

        # Move the video file to the output directory
        shutil.move(mp4, os.path.join(output_directory, os.path.basename(mp4)))

        print("Download finished... 😈😈")
        messagebox.showinfo("Success", "Download completed successfully!😈😈")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", "An error occurred during download.😅😥😥")


# Create the main application window
root = Tk()
root.title("Video Downloader")

# Create and layout UI components
canvas = Canvas(root, width=400, height=300)
canvas.pack()

app_label = Label(root, text="Video Downloader", fg="blue", font=("consolas", 20))
canvas.create_window(200, 20, window=app_label)

url_label = Label(root, text="Enter video URL")
url_entry = Entry(root)
canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)

path_label = Label(root, text="Select path to download")
path_btn = Button(root, text="Select", command=save_file)
canvas.create_window(200, 140, window=path_label)
canvas.create_window(200, 160, window=path_btn)

download_btn = Button(root, text="Download", padx=5, pady=5, command=download_video)
canvas.create_window(200, 250, window=download_btn)

root.mainloop()
