from os.path import abspath
from pathlib import Path
import os
import pandas as pd


def project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent


def default_result_path():
    name = 'NerpaResults'
    default_data_path = os.path.join(str(Path.home()), name)
    if name not in os.listdir(str(Path.home())):
        os.mkdir(default_data_path)
    return default_data_path


def import_csv_file(relative_path: str):
    abs_path = abspath(relative_path)
    dataframe = pd.read_csv(abs_path)

    return dataframe
