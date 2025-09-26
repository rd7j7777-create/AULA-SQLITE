#Criar um banco de dados sqlite e uma tabela
import sqlite3
#Criar a conexão com o bancp de dados chamado de "escola.db"
conexao = sqlite3.connect("escola.db")
#Criar o objeto chamado de "cursor"que sera usadp ára executar os comandos sql
cursor = conexao.cursor()

#Criar uma tabela no banco
cursor.execute("""
CREATE TABLE  IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    curso TEXT
    )             
    """)

