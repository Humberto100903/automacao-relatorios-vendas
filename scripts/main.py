# Script principal para execução do processo ETL e envio de relatórios

from src.etl import load_csv_data, load_sql_data, load_api_data, transform_data, generate_graph
from src.email import send_email
from src.api_clients import APIClient

# Configurações e credenciais
CSV_FILE_PATH = 'data/input/vendas.csv'
SQL_CONNECTION_STRING = 'mysql+pymysql://user:password@localhost/db'
SQL_QUERY = 'SELECT * FROM vendas'
API_URL = 'https://api.example.com/vendas'
API_KEY = 'sua_chave_api'
EMAIL_RECIPIENT = 'destinatario@example.com'

# Carregar dados
df_csv = load_csv_data(CSV_FILE_PATH)
df_sql = load_sql_data(SQL_CONNECTION_STRING, SQL_QUERY)
api_client = APIClient(API_KEY)
df_api = api_client.get_data(API_URL)

# Transformar dados
df_transformed = transform_data(df_csv)  # Você pode combinar e transformar os dados conforme necessário

# Gerar gráficos
generate_graph(df_transformed)

# Enviar relatórios por e-mail
send_email(
    subject='Relatório de Vendas',
    body='Segue em anexo o relatório de vendas.',
    to_email=EMAIL_RECIPIENT,
    attachment_path='data/output/relatorio_vendas.png'
)
