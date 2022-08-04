import pathlib
import os


def file_reader(file_path: str) -> tuple:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'Check your file path: {file_path}')

    file_suffix = pathlib.Path(file_path).suffix
    with open(file_path) as file:
        return file.read(), file_suffix
