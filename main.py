#!/usr/bin/env python3
## revox's youtube downloader (v0.3)
## https://github.com/revoxhere/youtube-downloader
from __future__ import unicode_literals
from tkinter import *
import youtube_dl, time
preset = ""

def webm():
    global ydl_opts, preset
    preset = "WEBM Video (max quality)"
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': 'true',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'webm',
        }],
    }
    download()

def mkv():
    global ydl_opts, preset
    preset = "MKV Video (max quality)"
    ydl_opts = {
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mkv',
        }],
    }
    download()

def mp4():
    global ydl_opts, preset
    preset = "MP4 Video (max quality)"
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': 'true',
        'format': 'bestvideo+bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }
    download()

def wav():
    global ydl_opts, preset
    preset = "WAV (max quality)"
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
    }
    download()

def aac():
    global ydl_opts, preset
    preset = "AAC (max quality)"
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'aac',
        }],
    }
    download()

def flac():
    global ydl_opts, preset
    preset = "FLAC (max quality)"
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
        }],
    }
    download()

def mp3low():
    global ydl_opts, preset
    preset = "MP3 Low (96kbps)"
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '96',
        }],
    }
    download()

def mp3medium():
    global ydl_opts, preset
    preset = "MP3 Medium (192kbps)"
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    download()

def mp3high():
    global ydl_opts, preset
    preset = "MP3 High (328kbps)"
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': 'true',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '328',
        }],
    }
    download()


def download():
    url = urlbutton.get()
    print(url)
    if url:
        try:
            label = Label(roots, text = " "*100, bg="white", font=("Arial", 12)).grid(row=4, columnspan=3, column=0, padx=2, pady=2)
            roots.update_idletasks()
            label = Label(roots, text = "Downloading using "+preset+" preset.", bg="white",foreground="#60a3bc", font=("Arial", 12)).grid(row=4, columnspan=3, column=0, padx=2, pady=2)
            roots.update_idletasks()

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([str(url)])
                    
            label = Label(roots, text = " "*100, bg="white", font=("Arial", 12)).grid(row=4, columnspan=3, column=0, padx=2, pady=2)
            roots.update_idletasks()
            label = Label(roots, text = "Done!", bg="white",foreground="#009432", font=("Arial", 12)).grid(row=4, columnspan=3, column=0, padx=2, pady=2)
            roots.update_idletasks()
        except:
            label = Label(roots, text = " "*100, bg="white", font=("Arial", 12)).grid(row=4, columnspan=3, column=0, padx=2, pady=2)
            roots.update_idletasks()
            label = Label(roots, text = "Error! Check the URL!", bg="white", foreground="#e55039", font=("Arial", 12)).grid(row=4, columnspan=3, column=0, padx=2, pady=2)
            roots.update_idletasks()
    else:
        label = Label(roots, text = " "*100, bg="white", font=("Arial", 12)).grid(row=4, columnspan=3, column=0, padx=2, pady=2)
        roots.update_idletasks()
        label = Label(roots, text = "Error! URL box is empty!", foreground="#e55039", bg="white", font=("Arial", 12)).grid(row=4, columnspan=3, column=0, padx=2, pady=2)
        roots.update_idletasks()
    urlbutton.delete(0, END)
    roots.update_idletasks()


def paste():
    urlbutton.delete(0, END)
    global ClipBoard
    AnnoyingWindow = Tk()
    try:
        ClipBoard = AnnoyingWindow.clipboard_get()
    except:
        pass
    AnnoyingWindow.destroy()
    try:
        urlbutton.insert(0, ClipBoard)
    except:
        pass
    
def roots():
        global urlbutton, roots, paste, mp3low, mp3medium, mp3high, flac, aac, wav, mp4, mkv, webm

        roots = Tk() #register window
        roots.title('revox\'s youtube downloader')
        roots.configure(background='white')

        label = Label(roots, text="Provide Video URL:", bg="white", fg="#3c6382", font = 'Arial').grid(row=0, column=0, padx=2, pady=2)
        urlbutton = Entry(roots, background="#FAFAFA", foreground="#000000")
        urlbutton.grid(row=0, column=1, padx=2, pady=2)
        grab = Button(roots, text='Paste from clipboard', command=paste, bg="white", font = 'Arial', fg="#546de5", width=15).grid(row=0, column=2, padx=2, pady=2)

        mp3low = Button(roots, text='MP3 Medium (96)', command=mp3low, bg="#f6b93b", font = 'Arial', fg="white", width=15).grid(row=1, column=0, padx=2, pady=2)
        mp3medium = Button(roots, text='MP3 High (196)', command=mp3medium, bg="#78e08f", font = 'Arial', fg="white", width=15).grid(row=1, column=1, padx=2, pady=2)
        mp3high = Button(roots, text='MP3 Very High (328)', command=mp3high, bg="#009432", font = 'Arial', fg="white", width=15).grid(row=1, column=2, padx=2, pady=2)

        flac = Button(roots, text='Flac Max', command=flac, bg="#D980FA", font = 'Arial', fg="white", width=15).grid(row=2, column=0, padx=2, pady=2)
        aac = Button(roots, text='AAC Max', command=aac, bg="#0652DD", font = 'Arial', fg="white", width=15).grid(row=2, column=1, padx=2, pady=2)
        wav = Button(roots, text='WAV Max', command=wav, bg="#6F1E51", font = 'Arial', fg="white", width=15).grid(row=2, column=2, padx=2, pady=2)

        mp4 = Button(roots, text='MP4 Video', command=mp4, bg="#C4E538", font = 'Arial', fg="white", width=15).grid(row=3, column=0, padx=2, pady=2)
        mkv = Button(roots, text='MKV Video', command=mkv, bg="#e15f41", font = 'Arial', fg="white", width=15).grid(row=3, column=1, padx=2, pady=2)
        webm = Button(roots, text='WEBM Video', command=webm, bg="#0097e6", font = 'Arial', fg="white", width=15).grid(row=3, column=2, padx=2, pady=2)
        
        label = Label(roots, text = " "*100, bg="white", font=("Arial", 12)).grid(row=4, columnspan=3, column=0, padx=2, pady=2)
        roots.mainloop()

roots()
 
