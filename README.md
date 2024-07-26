# File Integrity Monitor
------------------------
------------------------

## Overview
------------

The File Integrity Monitor is a Python-based utility that helps monitor the integrity of files by calculating their hash values and sending alerts when changes are detected. This project provides a simple and efficient way to ensure the integrity of critical files and detect any unauthorized modifications.

## Getting Started
---------------

### Prerequisites

* Python 3.7 or later
* Email account with SMTP access (e.g., Gmail, Outlook)

### Dependencies

* `watchdog` library: Installation covered in the next step

### Installation

1. Clone the repository: `git clone https://github.com/akshayjain-1/File-Integrity-Monitoring.git`
2. Navigate to the project directory: `cd file-integrity-monitor`
3. Install the required libraries: `pip install -r requirements.txt`

### Configuration

1. Set the `EMAIL` and `EMAIL_PWD` environment variables with your email account credentials.
For example, on Linux or macOS, you can use the following commands:
`export EMAIL="your_email@example.com" export EMAIL_PWD="your_password"`
On Windows, you can set environment variables through the System Properties or using the `set` command.

2. Update the `sender_email@example.com` and `receiver_email@example.com` placeholders in the `send_alert` function with your actual email addresses.

## Usage
-----

### Calculating File Hash

1. Import the `calculate_hash` function: `from monitor import calculate_hash`
2. Call the `calculate_hash` function with the file path as an argument: `hash_value = calculate_hash('path/to/file.txt')`
3. The function returns the SHA-256 hash value of the file as a string.

### Sending Alerts

1. Import the `send_alert` function: `from monitor import send_alert`
2. Call the `send_alert` function with the alert message as an argument: `send_alert('File integrity alert: file.txt has been modified!')`
3. The function sends an email with the alert message to the configured recipient.

## Functions
------------

### `calculate_hash(file_path: str) -> Optional[str]`

Calculates the SHA-256 hash value of a file.

* `file_path`: The path of the file to calculate the hash of.
* Returns: The hash value of the file as a string, or `None` if the file does not exist or cannot be read.

### `send_alert(message: str) -> None`

Sends an alert with the given message.

* `message`: The email body to send.
* Sends an email with the alert message to the configured recipient.

## Troubleshooting
-----------------

### Common Issues

* `FileNotFoundError`: The file specified in the `calculate_hash` function does not exist.
* `OSError`: An error occurred while reading the file.
* `smtplib.SMTPException`: An error occurred while sending the email.

### Solutions

* Check the file path and ensure it exists.
* Verify the file permissions and ensure the script has read access.
* Check the email account credentials and SMTP server settings.

## Contributing
--------------

Contributions are welcome! If you'd like to contribute to the project, please fork the repository, make your changes, and submit a pull request.