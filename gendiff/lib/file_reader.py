import pathlib
import os


def get_data_from_file(file_path: str) -> tuple:
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'Check your file path: {file_path}')

    file_suffix = pathlib.Path(file_path).suffix
    with open(file_path) as file:
        return file.read(), file_suffix
