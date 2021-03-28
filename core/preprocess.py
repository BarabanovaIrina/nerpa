from datetime import datetime
from core.data.data import Data
from abc import ABC, abstractmethod


class PreprocessStrategy(ABC):
    def __init__(self, data: Data):
        self.data = data

    @abstractmethod
    def process(self) -> Data:
        raise NotImplementedError

    def _chek_and_clean_timestamps(self):
        self.data.idx = [datetime.utcfromtimestamp(int(timestamp) / 1000).strftime('%Y-%m-%d %H:%M:%S')
                         for timestamp in self.data.idx]


class OHLCPreprocess(PreprocessStrategy):
    def __init__(self, data: Data):
        super().__init__(data)

    def process(self) -> Data:
        self._chek_and_clean_timestamps()

        self.data.features = self.data.features.T[:4].T

        return self.data
