#!/usr/bin/env python3

class Printer(object):

    def __init__(self, ppm):
        self.pagerate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False


    def start_next(self, new_task):
        self.current_task = newtask
        self.time_remaining = newtask.get_pages() * 60 / self.pagerate
