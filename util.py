import os


def get_day(file):
    parent_dir = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
    return int(parent_dir.split("-")[0])
