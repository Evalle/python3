#!/usr/bin/env python3

from printtask import Printer, Task
from queue import Queue
import random

def sim(num_seconds, pages_per_min):

    labprinter = Printer(pages_per_min)
    print_queue = Queue()
    waitingtimes = list()

    for current_second in range(num_seconds):

        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not labprinter.busy()) and (not print_queue.isempty()):
            nexttask = print_queue.dequeue()
            waitingtimes.append(nexttask.wait_time(current_second))
            labprinter.start_next(nexttask)

        labprinter.tick()

    average_wait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2fsecs %3d tasks remaining. " % (average_wait, print_queue.size()))

def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    sim(3600, 10)

