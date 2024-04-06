import tkinter as tk
import customtkinter
from pytube import YouTube
import threading

def start_download():
    yt_link = link.get()
    threading.Thread(target=download_video, args=(yt_link,)).start()

def download_video(yt_link):
    try:
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()

        app.after(0, lambda: title.configure(text=yt_object.title, text_color="white"))
        app.after(0, lambda: finish_label.configure(text="Downloading...", text_color="blue"))

        video.download()
        app.after(0, lambda: finish_label.configure(text="Downloaded!", text_color="green"))
    except Exception as e:
        app.after(0, lambda: finish_label.configure(text="Download Error", text_color="red"))
        print(f"An error occurred: {e}")

def on_progress(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = bytes_downloaded / total_size * 100
        per = str(int(percentage_of_completion))
        pPercent.configure(text=per + "%")
        pPercent.update()

        # Update Progress Bar
        progressBar.set(float(percentage_of_completion) / 100)

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue") 

# Our app frame
app = customtkinter.CTk() # Initialize the app
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert YouTube link here", height=50, font=("Arial", 16, "bold"))
title.pack(padx="24", pady="24")

# Input
url_var = tk.StringVar()
link = customtkinter.CTkEntry(app, width=500, height=50, corner_radius=50, textvariable=url_var)
link.pack()

# Finished Downloading
finish_label = customtkinter.CTkLabel(app, text="", font=("Arial", 14, "bold"))
finish_label.pack()

# Progress Percentage
pPercent = customtkinter.CTkLabel(app, text="0%")
pPercent.pack()

# Progress Bar
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx="10", pady="10")

# Download  
download_button = customtkinter.CTkButton(app, text="Download", corner_radius=50, width=150, height=50, font=("Arial", 14, "bold"), command=start_download)
download_button.pack()

# Run app 
app.mainloop()
