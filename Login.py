import sqlite3
import customtkinter as ctk

conn = sqlite3.connect(r'C:\SQLITE\BANCOTESTE\data.db')
cursor = conn.cursor()

def logar(name,password):
    nome_login= name
    Senha_login = password

    cursor.execute("SELECT senha FROM usuarios WHERE nome = ?",(nome_login,))
    try:
        senha_banco = cursor.fetchone()[0]
        
        if senha_banco == Senha_login:
            print("Login efetuado com sucesso!")
        else:
            print('senha incorreta!')

    except Exception as e:
        print('Usuario ou senha incorreto!')

root = ctk.CTk()

root.mainloop()

 