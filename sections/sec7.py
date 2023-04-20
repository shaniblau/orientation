import shutil
from os.path import isfile, join


def copy_dir(source: str, destination: str, extensions: list = None):
    if extensions is None:
        shutil.copytree(source, destination)
    else:
        shutil.copytree(source, destination,
                        ignore=lambda d, files: [f for f in files if isfile(join(d, f)) and f[-2:] not in extensions])


