from pathlib import Path

import pandas as pd

from utils import import_csv_file, project_root


def test_project_root():
    # given
    expected_root = Path(__file__).parent.parent

    # when
    actual_root = project_root()

    # then
    assert actual_root == expected_root


def test_import_csv_file():
    file = 'data_for_test/test_file.csv'

    frame = import_csv_file(file)

    assert type(frame) is pd.DataFrame
