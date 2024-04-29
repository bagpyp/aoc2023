import os


def get_day(file):
    parent_dir = os.path.basename(os.path.dirname(os.path.abspath(file)))
    return int(parent_dir.split("-")[0]) - 1
