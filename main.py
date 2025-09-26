#Criar um banco de dados sqlite e uma tabela
import sqlite3
#Criar a conexão com o bancp de dados chamado de "escola.db"
conexao = sqlite3.connect("escola.db")
#Criar o objeto chamado de "cursor"que sera usadp ára executar os comandos sql
cursor = conexao.cursor()

#Criar uma tabela no banco
# cursor.execute("""
# CREATE TABLE  IF NOT EXISTS alunos (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     idade INTEGER,
#     curso TEXT
#     )             
#     """)
# nome = input("Digite o nome do aluno: ")
# idade = int(input(f"Digite a idade do {nome}: "))
# curso = input(f"Digite o curso do {nome}: ").lower()
# cursor.execute("""
# INSERT INTO alunos (nome,idade,curso)
# VALUES (?, ?, ?)                
# """,
# (nome,idade,curso)         
# )
# #confirmar as alteraçãoes no banco 
# conexao.commit()


#inserir varios alundos de uma vez
# alunos = [
# ("Yago",28, "Direirto"),
# ("Jessica",24, "Computação"),
# ("Breno",52, "Computação"),
# ]

# #executemany permite inserir multiplas linhas de um só 
# cursor.executemany("""
# INSERT INTO alunos (nome, idade, curso)                   
# VALUES (? ,? ,?)                   
# """,
# (alunos)
# )
# conexao.commit()
#Atualizar dados no banco 
# cursor.execute("""
# UPDATE alunos               
# SET idade = ?, curso = ?
# WHERE id = ?


#               """,
              
# (61, "medicina",3)

              
              
        
    

# )
# conexao.commit()


#Funcao listar Dados no banco
#consultar os dados no banco
# cursor.execute("SELECT * FROM alunos ")
#fetchal traz todas as linhas da consulta
# for linha in cursor.fetchall():
#     print(f"ID: {linha[0]} | NOME:{linha [1]} |Idade:{linha [2]} | CURSO: {linha[3]} ")
# print("-"*80)


# pesquisar = input("Digite  o curso que deseja pesquisar os alunos: ")
# cursor.execute("SELECT nome , idade FROM alunos WHERE curso = ?", (pesquisar,))
# print(f"Alunos do Curso de {pesquisar}")
# for linha in cursor.fetchall():
#     print(f" NOME:{linha [0]} |IDADE:{linha [1]}  |CURSO:{linha [2]}")

# Deletar dados do banco
cursor.execute("DELETE FROM alunos WHERE id = ?" , (1,))
conexao.commit()
#sempre fechar a conexãp com o banco de dados, se não o pc explode
conexao.close()