import sys

from console import Console


def catch_exit_application(signal_received, frame):
    Console.exit_message(reason='Ctrl-C detected.', nl=True)
    sys.exit(0)


def error_exit_application():
    Console.exit_message(reason='Error detected.', nl=False)
    sys.exit(0)
