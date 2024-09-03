# Testes para funções de ETL

import unittest
import pandas as pd
from src.etl import load_csv_data, transform_data

class TestETL(unittest.TestCase):

    def test_load_csv_data(self):
        df = load_csv_data('data/input/vendas.csv')
        self.assertIsInstance(df, pd.DataFrame)

    def test_transform_data(self):
        df = pd.DataFrame({'vendas': [100, 200, 300]})
        df_transformed = transform_data(df)
        # Adicione suas asserções baseadas na transformação esperada
        self.assertTrue(df_transformed is not None)

if __name__ == '__main__':
    unittest.main()
