import os
from glob import glob

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

pattern = os.path.join(ROOT_DIR, "[0-9]*-*")
days = [p for p in glob(pattern) if os.path.isdir(p)]
