"""
A file integrity monitor that watches for changes to files in a specified path.

Classes:
    FileIntegrityMonitor: A class for monitoring file integrity.
"""
import time
import os
from typing import Dict
import watchdog
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from utils import calculate_hash, send_alert


class FileIntegrityMonitor:
    """
    A class for monitoring file integrity
    """

    def calculate_initial_hashes(self) -> Dict[str, str]:
        """
        This function calculates the hash of all files in the specified path
        
        Args: None
        
        Returns:
            A dictionary of file paths and their corresponding hashes.
        """
        hashes = {}

        # Iterate over the current direcotry and subdirecotry to get all files
        for current_dir, _, files in os.walk(self.path):
            for file in files:
                file_path = os.path.join(current_dir, file)
                hashes[file_path] = calculate_hash(file_path)
        return hashes

    def start_monitoring(self) -> None:
        """
        This function starts the monitoring process
        """
        event_handler = FileChangeHandler(self.hashes)
        observer = Observer()
        observer.schedule(event_handler, self.path, recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    def __init__(self, path: str):
        self.path = path
        self.hashes: Dict[str, str] = self.calculate_initial_hashes()


class FileChangeHandler(FileSystemEventHandler):
    """
    A class for handling file changes
    """

    def on_modified(self, event: FileSystemEvent) -> None:
        """
        This function is called when a file is modified. 
        
        Args:
            event (FileSystemEvent)
        """
        if isinstance(event, watchdog.events.FileModifiedEvent):
            file_path = event.src_path

            new_hash = calculate_hash(file_path)
            if new_hash != self.hashes.get(file_path):
                self.hashes[file_path] = new_hash
                print("File modification detected. Sending Alert")
                send_alert(f"File {file_path} has been modified.")
        else:
            pass

    def on_created(self, event: FileSystemEvent) -> None:
        """
        This function is called when a file is created.
        
        Args:
            event (FileSystemEvent)
        """
        if isinstance(event, watchdog.events.FileCreatedEvent):
            file_path = event.src_path
            self.hashes[file_path] = calculate_hash(file_path)
            print("File Creation detected. Sending alert")
            send_alert(f"File created: {file_path}")
        elif isinstance(event, watchdog.events.DirCreatedEvent):
            dir_path = event.src_path
            print("Directory Creation detected. Sending alert")
            send_alert(f"Directory created: {dir_path}")

    def on_deleted(self, event: FileSystemEvent) -> None:
        """
        This function is called when a file is deleted.
        
        Args:
            event (FileSystemEvent)
        """
        file_path = event.src_path
        if file_path in self.hashes:
            del self.hashes[file_path]
            print("File deletion detected. Sending alert")
            send_alert(f"File deleted: {file_path}")

    def __init__(self, hashes: Dict[str, str]):
        self.hashes = hashes
