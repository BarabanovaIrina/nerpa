from utils import default_result_path
from core.preprocess import OHLCPreprocess
from os.path import join
from core.data.data import Data

if __name__ == '__main__':
    raw_data = Data.from_csv('data/raw.csv')

    headers = ['Open', 'High', 'Low', 'Close']

    cleaned_data = OHLCPreprocess(raw_data).process()

    frame = cleaned_data.as_pd_dataframe(headers=headers)

    frame.to_csv(join(default_result_path(), 'result.csv'))
