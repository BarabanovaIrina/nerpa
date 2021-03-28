from core.data.data import Data
from core.preprocess import OHLCPreprocess


def test_preprocess_process():
    # given
    data = Data.from_csv('data_for_test/test_file.csv')

    # when
    cleaned_data = OHLCPreprocess(data).process()

    # then
    assert cleaned_data.idx[0] == '2017-08-17 04:01:00'
