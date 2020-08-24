#!/usr/bin/python
# thread.start_new_thread ( function, args[, kwargs] )

import thread
import time

# Define a function for the thread
def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
