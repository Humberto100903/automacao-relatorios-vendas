# Contém funções para ETL (extração, transformação, carga)

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

def load_csv_data(file_path):
    return pd.read_csv(file_path)

def load_sql_data(connection_string, query):
    engine = create_engine(connection_string)
    return pd.read_sql(query, engine)

def load_api_data(api_url, params=None):
    response = requests.get(api_url, params=params)
    return pd.json_normalize(response.json())

def transform_data(df):
    # Adicione suas transformações de dados aqui
    return df

def generate_graph(df, output_path='data/output/relatorio_vendas.png'):
    plt.figure(figsize=(10, 6))
    df.plot(kind='bar')  # Exemplo de gráfico de barras
    plt.title('Relatório de Vendas')
    plt.xlabel('Mês')
    plt.ylabel('Vendas')
    plt.savefig(output_path)
