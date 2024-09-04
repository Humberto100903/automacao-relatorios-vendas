# Sistema de Automação de Relatórios de Vendas

## Descrição

Este projeto visa a automação da geração de relatórios de vendas utilizando Python. O sistema foi desenvolvido para integrar dados de várias fontes, como arquivos CSV, bancos de dados SQL e APIs externas, e gerar relatórios semanais e mensais com visualizações gráficas detalhadas. O objetivo é otimizar o processo de criação de relatórios, reduzindo o tempo e eliminando erros manuais.

## Funcionalidades

- **Extração e Transformação de Dados:** Integra dados de diversas fontes e os transforma para análise.
- **Geração de Relatórios:** Cria relatórios detalhados com informações de vendas por região, produto e canal.
- **Visualização Gráfica:** Inclui gráficos para visualizar o desempenho das vendas ao longo do tempo.
- **Envio Automático de Relatórios:** Automatiza o envio dos relatórios por e-mail para os stakeholders.

## Estrutura de Pastas
automacao_relatorios_vendas/ 
│ 
├── data/ 
│   ├── input/ 
│ │ ├── vendas.csv 
│ │ ├── dados.sql 
│ │ └── api_data.json 
│ ├── output/ 
│ │ ├── relatorio_vendas.png 
│ │ ├── grafico_vendas_semanal.png 
│ │ ├── grafico_vendas_regiao.png 
│ │ ├── grafico_vendas_produto.png 
│ │ └── grafico_vendas_canal.png 
│ └── config/ 
│ └── config.yaml 
│ ├── src/ 
│ ├── etl.py 
│ ├── report_generator.py 
│ ├── email_sender.py 
│ └── api_integration.py 
│ ├── requirements.txt 
├── README.md 
└── main.py


## Instalação

1. **Clone o repositório:**

   <git clone https://github.com/seuusuario/automacao-relatorios-vendas.git>
   <cd automacao-relatorios-vendas>

2. **Crie um ambiente virtual e ative-o:**
   
  <python -m venv venv>
  <source venv/bin/activate  # No Windows, use `venv\Scripts\activate`>

3. **Instale as dependências:**
   
  <pip install -r requirements.txt>

## Uso

1. **Execute o script principal:**

  <python main.py>
