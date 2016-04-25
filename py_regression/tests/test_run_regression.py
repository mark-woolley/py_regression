from unittest2 import TestCase
import pandas as pd

from py_regression.run_regression import RunRegression

class TestRunRegression(TestCase):

    def toy_test(self):
        df = pd.DataFrame({'y': [1,2,3,4],
                           'x1': [1.1, 1.5, 1.2, 0.8],
                           'x2': [3.2, 4.5, 2.1, 8.9]})
        results = RunRegression(df=df, formula="y ~ x1 + x2").results
        expected_params = [2.697754, -1.039100, 0.213307]
        self.assertEqual(len(results.params), len(expected_params))
        self.assertListAlmostEqual(results.params, expected_params, places=5)

    def assertListAlmostEqual(self, first, second, places=5):
        for i in range(0, len(first)):
            self.assertAlmostEqual(first[i], second[i], places=places)