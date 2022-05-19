import unittest
from test.helpers import ClassificationModel

import torch
from torch.utils.data import DataLoader, TensorDataset

from pytorch_ood.api import RequiresFitException
from pytorch_ood.detector import Mahalanobis


class MahalanobisTest(unittest.TestCase):
    """
    Test mahalanobis method
    """

    def setUp(self) -> None:
        torch.manual_seed(123)

    def test_something(self):
        nn = ClassificationModel()
        model = Mahalanobis(nn)

        y = torch.cat([torch.zeros(size=(10,)), torch.ones(size=(10,))])
        x = torch.randn(size=(20, 10))
        dataset = TensorDataset(x, y)
        loader = DataLoader(dataset)

        model.fit(loader)

        scores = model(x)
        print(scores)

        scores = model(torch.ones(size=(10, 10)) * 10)
        print(scores)

        self.assertIsNotNone(scores)

    def test_nofit(self):
        nn = ClassificationModel()
        model = Mahalanobis(nn)
        x = torch.randn(size=(20, 10))

        with self.assertRaises(RequiresFitException):
            model(x)