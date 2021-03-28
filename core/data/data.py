from os.path import abspath
import numpy as np
import pandas as pd
from typing import List


class Data:
    def __init__(self, idx, features, target, headers=None):
        self.headers = headers
        self.idx = idx
        self.features = features
        self.target = target

    @staticmethod
    def from_csv(path):
        abs_path = abspath(path)
        dataframe = pd.read_csv(abs_path)

        pure_data = np.array(dataframe).T
        idx = pure_data[0]
        features = pure_data[1:].T

        return Data(idx=idx, features=features, target=None)

    def as_pd_dataframe(self, headers: List[str] = None):
        frame = pd.DataFrame(data=self.features, index=self.idx, columns=headers)

        return frame

    def __repr__(self):
        return {
            'idx': self.idx,
            'features': self.features,
            'target': self.target,
        }

    def __str__(self):
        return str(self.__repr__())
