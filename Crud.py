import sqlite3
import pyotp
import threading
import streamlit as st
from OTP import gera_chave
# Conexão com o banco de dados
conn = sqlite3.connect('database.db')

# Criação do cursor para executar comandos SQL
cursor = conn.cursor()


# Cria um objeto "local" para armazenar a conexão SQLite de cada thread
local = threading.local()

# Função para obter uma conexão SQLite para a thread atual


def get_db():
    # Verifica se já existe uma conexão para esta thread
    if not hasattr(local, "conn"):
        # Cria uma nova conexão para esta thread
        local.conn = sqlite3.connect('database.db')
    return local.conn

# Função para criar um novo usuário


def criar_usuario(nome, email, senha, bio=None, imagem_perfil=None):
    cursor.execute('''
INSERT INTO usuarios (
                        nome,
                        email,
                        senha,
                        bio,
                        imagem_perfil)
VALUES (?, ?, ?, ?, ?)
                      ''',
                   (nome, email, senha, bio, imagem_perfil))
    conn.commit()
    print("Usuário criado com sucesso!")

# Função para obter um usuário pelo ID


def obter_usuario_por_id(id):
    cursor.execute("SELECT * FROM usuarios WHERE id=?", (id,))
    return cursor.fetchone()

# Função para obter todos os usuários


def obter_todos_usuarios():
    cursor.execute("SELECT * FROM usuarios")
    return cursor.fetchall()

# Função para atualizar um usuário


def atualizar_usuario(id,
                      nome=None,
                      email=None,
                      senha=None,
                      bio=None,
                      imagem_perfil=None):
    campos = []
    valores = []

    if nome:
        campos.append("nome=?")
        valores.append(nome)

    if email:
        campos.append("email=?")
        valores.append(email)

    if senha:
        campos.append("senha=?")
        valores.append(senha)

    if bio:
        campos.append("bio=?")
        valores.append(bio)

    if imagem_perfil:
        campos.append("imagem_perfil=?")
        valores.append(imagem_perfil)

    valores.append(id)

    cursor.execute(
        f"UPDATE usuarios SET {', '.join(campos)} WHERE id=?", tuple(valores))
    conn.commit()
    print("Usuário atualizado com sucesso!")

# Função para excluir um usuário


def excluir_usuario(id):
    cursor.execute("DELETE FROM usuarios WHERE id=?", (id,))
    conn.commit()
    print("Usuário excluído com sucesso!")


# Chave secreta do servidor e o aplicativo Google Authenticator
chave_secreta = 'SFNTAXADPJUAFQWZBJFIA3FQBJTVKO36'

# Função para realizar o login de um usuário


def login(email, senha, token):
    # Conecta ao banco de dados
    # conn = sqlite3.connect('banco.db')
    # cursor = conn.cursor()
    # Verifica se o usuário existe no banco de dados
    cursor.execute("SELECT * FROM usuarios WHERE email=?", (email,))
    usuario = cursor.fetchone()
    if not usuario:
        return print("Usuário não encontrado")

    # Verifica se a senha informada está correta
    if usuario[3] != senha:
        return print("Senha incorreta")

    # Cria uma instância do PyOTP com a chave secreta compartilhada
    totp = pyotp.TOTP(chave_secreta)
    print(totp.now())
    print(token)
    # Verifica se o token informado é válido
    if not totp.verify(token, valid_window=1):
        return print("Token inválido")
    # Registra o login na tabela de logs
    registrar_log(usuario[0])

    # Retorna o usuário logado
    # print(usuario)
    print(totp.verify(token))
    print('logado com sucesso')
    return usuario


def registrar_log(usuario_id):
    cursor.execute('''
INSERT INTO logs (usuario_id, data_hora)
VALUES (?, datetime('now', 'localtime'))
''', (usuario_id,))
    conn.commit()
    print("Log registrado com sucesso!")


# Exemplo de uso das funções
# criar_usuario("João Silva", "joao@email.com", "123456")
# usuario = obter_usuario_por_id(1)
# print(usuario)
todos_os_usuarios = obter_todos_usuarios()
# print(todos_os_usuarios)
# atualizar_usuario(1, nome="João da Silva")

# excluir_usuario(1)

# email = 'joao@email.com'
# senha = '123456'
# token = gera_chave()
# token_fake = '558635'
# login(email, senha, token)


st.title('Login')

# Formulário de login
email = st.text_input('E-mail')
senha = st.text_input('Senha', type='password')
tk = gera_chave()
print(tk)
token = st.text_input('TOKEM GOGLE AUTENTICATOR', type='password')

if st.button('Entrar'):
    resultado = login(email, senha, token)
    if isinstance(resultado, str):
        st.error(resultado)
    else:
        st.success('Login realizado com sucesso')
        st.write('Usuário logado:', resultado)
        # Fechamento da conexão com o banco de dados
        conn.close()


# Fechamento da conexão com o banco de dados
conn.close()
