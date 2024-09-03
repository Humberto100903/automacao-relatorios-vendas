# Contém classes e funções para integração com APIs

import requests
import pandas as pd

class APIClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_data(self, endpoint):
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(endpoint, headers=headers)
        return pd.json_normalize(response.json())
