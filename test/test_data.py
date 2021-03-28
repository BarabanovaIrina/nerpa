from core.data.data import Data
from pandas import DataFrame


def test_data_as_pd_dataframe():
    # given
    data = Data.from_csv('data_for_test/test_file.csv')
    frame = data.as_pd_dataframe()

    assert type(frame) is DataFrame
