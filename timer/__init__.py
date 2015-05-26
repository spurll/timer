# Written by Gem Newman. This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 3.0 Unported License.


from __future__ import print_function
from datetime import datetime


class timer:
    def __init__(self, label="Elapsed time", display=print):
        self.label = label
        self.display = display

    def __enter__(self):
        self.start = datetime.now()

    def __exit__(self, type, value, traceback):
        self.display("{}: {}".format(self.label, datetime.now() - self.start))
