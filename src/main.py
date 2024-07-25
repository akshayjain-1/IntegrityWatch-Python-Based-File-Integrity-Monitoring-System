'''
Main function which acts as the interface for running the program
'''

from monitor import FileIntegrityMonitor

def main():
    """
    Main function for initiating integrity monitoring
    """
    monitor = FileIntegrityMonitor("/path/to/monitor")
    monitor.start_monitoring()

if __name__ == "__main__":
    main()
