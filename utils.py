import sys

from console import Console

def exit_application(signal_received, frame):
    Console.exit_message()
    sys.exit(0)
