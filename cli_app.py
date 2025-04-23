"""
Mainline module for running the application.
"""
__author__ = "jjradler"
__version__ = "0.0.1"

import logging
import time
import argparse


def minutes_to_seconds(minutes):
    return float(minutes * 60.0)


def timer_countdown(duration_seconds, interval_seconds=1.0):
    counter = duration_seconds
    print("Starting Time-Block...")
    while counter >= 0:
        logging.debug(f"counter = {counter} seconds elapsed")
        bar = "[" + "X" * int(counter) + "]" + f"{int(counter)} Seconds Left"
        print(bar, end='\r')
        time.sleep(interval_seconds)
        counter -= interval_seconds
    print("Timer Done! What did you work on?")


def main():
    while True:
        time_block_minutes = input("How long is this time block?:\t")
        time_block_seconds = minutes_to_seconds(time_block_minutes)
        timer_countdown(time_block_seconds)


if __name__ == "__main__":
    main()