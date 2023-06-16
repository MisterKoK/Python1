from threading import Thread
from pytube import YouTube
import sys
import time


def progressbar(count):
    for i in range(count):
        sys.stdout.write("[ % -1s] %d %%" % ('=' * i, 10 * i))
        time.sleep(0.30)
        sys.stdout.write('\r')
    sys.stdout.write("[ % -1s] %d %%" % ('=' * i, 10 * i))
    sys.stdout.write('\n')


def download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")

thread1 = Thread(target=progressbar(11))
thread2 = Thread(target=download(link))

thread1.start()  # Старт потока №1
thread2.start()  # Старт потока №2

thread1.join()
thread2.join()
