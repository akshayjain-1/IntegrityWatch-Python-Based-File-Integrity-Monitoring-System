"""
Utility functions for the file integrity monitor.

This module provides functions for calculating the hash of a file and sending alerts.

Functions:
    calculate_hash(file_path: str) -> str: Calculates the hash of a file.
    send_alert(message: str) -> None: Sends an alert with the given message.
"""
import hashlib
import os
import smtplib
from email.mime.text import MIMEText
from typing import Optional

def calculate_hash(file_path: str) -> Optional[str]:
    """
    Calculates the hash of a file.
    The code reads chunk of 4096 bytes at a time

    Args:
        file_path (str): The path of the file to calculate the hash of.

    Returns:
        str: The hash of the file, or None if the file does not exist or cannot be read.
    """
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
    except OSError as e:
        raise OSError(f"Error reading file '{file_path}': {e}") from e

    return hash_sha256.hexdigest()

def send_alert(message: str) -> None:
    """
    Sends an alert with the given message
    
    Args:
        message(str): The email body to send
    """
    msg = MIMEText(message)
    msg['Subject'] = "File Integrity Change Alert"
    msg['From'] = "sender_email@example.com"
    msg['To'] = "receiver_email@example.com"

    try:
        # Can change the smtp server as needed
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(os.environ["EMAIL"], os.environ["EMAIL_PWD"])
        server.sendmail("sender_email@example.com", "receiver_email@example.com", msg.as_string())
        server.quit()
    except smtplib.SMTPException as e:
        raise smtplib.SMTPException(f"Error sending email: {e}") from e
