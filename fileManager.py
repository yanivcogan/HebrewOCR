import os
from os import listdir
from os.path import isfile, join

from pathlib import Path
import pathlib


def get_file_paths_in_directory(root, base=""):
    files = []
    dir_content = listdir(root+base)
    for f in dir_content:
        check_for = join(root, base, f)
        if isfile(check_for):
            files.append(join(base, f))
        else:
            files.extend(get_file_paths_in_directory(root, join(base, f)))
    return files


def mkdir_p(path):
    dir_path = Path(path).parent
    pathlib.Path(dir_path).mkdir(parents=True, exist_ok=True)


def path_to_pdf(path):
    return os.path.splitext(path)[0]+".pdf"
