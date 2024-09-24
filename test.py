import ctypes
import time

waitTime = int(75)

while True:
    ctypes.windll.winmm.mciSendStringW('set cdaudio door open', None, 0, None)

    time.sleep(waitTime)

    ctypes.windll.winmm.mciSendStringW('set cdaudio door closed', None, 0, None)

    time.sleep(3.5)
