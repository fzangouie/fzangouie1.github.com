import os

__author__ = 'user'


class Config:
    def __init__(self):
        static_path = os.path.join(os.path.dirname(__file__), "static")

