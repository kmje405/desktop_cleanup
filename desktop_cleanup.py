#!/usr/bin/env python3

import os
import shutil
import logging
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the directory to monitor and the destination folders based on file extensions
DESKTOP = str(Path.home() / "Desktop")
FILE_TYPE_FOLDERS = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Videos': ['.mp4', '.mov', '.wmv', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac', '.flac']
}

# Ensure the folders exist
for folder in FILE_TYPE_FOLDERS.keys():
    os.makedirs(os.path.join(DESKTOP, folder), exist_ok=True)

# Determine the script's directory and set up logging
script_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(script_dir, "desktop_cleanup.log")
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        self.move_files()

    def move_files(self):
        for filename in os.listdir(DESKTOP):
            src_path = os.path.join(DESKTOP, filename)
            if os.path.isfile(src_path):
                self.move_file(src_path)

    def move_file(self, src_path):
        file_extension = os.path.splitext(src_path)[1].lower()
        for folder, extensions in FILE_TYPE_FOLDERS.items():
            if file_extension in extensions:
                dest_path = os.path.join(DESKTOP, folder, os.path.basename(src_path))
                shutil.move(src_path, dest_path)
                logging.info(f'Moved {src_path} to {dest_path}')
                break

if __name__ == "__main__":
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=DESKTOP, recursive=False)
    
    # Move files at startup
    event_handler.move_files()

    observer.start()
    logging.info("Started monitoring the desktop folder.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
        logging.info("Stopped monitoring the desktop folder.")
    observer.join()
