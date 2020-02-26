import os, sys
import logging


class Log:

    def __init__(self, filename):
        self.log = logging.getLogger()
        self.log.setLevel(logging.DEBUG)
        ch = logging.FileHandler(filename=filename)
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.log.addHandler(ch)