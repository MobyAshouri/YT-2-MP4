from pytube import YouTube
from pathlib import Path
import customtkinter as ctk
import winsound

def test():

    loading = ctk.CTkToplevel(win)
    loading.resizable(False, False)
    loading.geometry("300x100")
    loading.title("Working...")
    loading.iconbitmap("assets/Youtube_logo.ico")

    global label
    label = ctk.CTkLabel(loading, text="Download In Progress")
    
    link = text.get()
    yt = YouTube(link, on_complete_callback=done)
    ys = yt.streams.get_highest_resolution()
    ys.download(str(Path.home() / "Downloads"))

    label.place(x=18, y=40)

    loading.mainloop()

def done(unused, finished):
    print("done")
    label.configure(text="Video has been downloaded in downloads folder")
    label.update()
    winsound.PlaySound("Sound.wav", winsound.SND_FILENAME)
    
win = ctk.CTk()
win.title("YT-2-MP4")
win.geometry("400x120")
win.resizable(False, False)
win.iconbitmap("assets/Youtube_logo.ico")

text = ctk.CTkEntry(win, width=300, height=30, fg_color="white", text_color="black")
text.place(x=50, y=20)

button = ctk.CTkButton(win, text="Download", command=test, width=200, height=30, fg_color="red", hover_color="white")
button.place(x=100, y=70)

win.mainloop()