import os
import sqlalchemy
import argparse
import pandas as pd
import sqlite3
# from datetime import datetime, timedelta


# diretórios e sub-diretórios do projeto
BASE_DIR = os.path.dirname(
     os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, 'data')
SQL_DIR = os.path.join(BASE_DIR, 'src', 'sql')

parser = argparse.ArgumentParser()
parser.add_argument('--date_end', '-e', help='Data fim da extração', default='2018-06-01')
args = parser.parse_args()

date_end = args.date_end
# date_init = datetime.strptime(date_end, '%Y-%m-%d') - timedelta(days=365)
# date_init = date_init.strftime('%Y-%m-%d')
ano = int(date_end.split('-')[0]) - 1
mes = int(date_end.split('-')[1])
date_init = f'{ano}-{mes}-01'

# importa a query
with open(os.path.join(SQL_DIR, 'segmentos.sql')) as query_file:
    query = query_file.read()

query = query.format(date_init = date_init,
                    date_end = date_end)

# abrindo a conexão com o banco
str_conn = 'sqlite:///{path}'
str_conn = str_conn.format(path=os.path.join(DATA_DIR, 'olist.db'))
conn = sqlalchemy.create_engine(str_conn)

create_query = f"""
CREATE TABLE tb_seller_sgmt AS 
{query}
;"""

insert_query = f"""
DELETE FROM tb_seller_sgmt WHERE dt_sgmt = '{date_end}';
INSERT INTO tb_seller_sgmt 
{query}
;"""

try:
    conn.execute(create_query)
except: 
    for q in insert_query.split(';')[:-1]:
        conn.execute(q)