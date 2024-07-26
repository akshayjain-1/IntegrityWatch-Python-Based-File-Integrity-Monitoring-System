"""
The main entry point of the file integrity monitor application.

This module sets up the file integrity monitor and starts the watchdog observer.
"""

from monitor import FileIntegrityMonitor

def main():
    """
    Main function for initiating integrity monitoring
    """
    monitor = FileIntegrityMonitor("/path/to/monitor")
    monitor.start_monitoring()

if __name__ == "__main__":
    main()
