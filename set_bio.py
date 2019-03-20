from telethon import TelegramClient
import socks
import win32gui
from telethon.tl.functions.account import UpdateProfileRequest

classname = '{97E27FAA-C0B3-4b8e-A693-ED7881E99FC1}'# 
win = win32gui.FindWindow(classname, None)
text = win32gui.GetWindowText(win)
print(text)

api_id = id from https://my.telegram.org/
api_hash = api from ^
client = TelegramClient('session_name', api_id, api_hash).start()

client(UpdateProfileRequest(
    about=text
))
