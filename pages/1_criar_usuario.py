import streamlit as st
import sqlite3
import time

nome = st.empty()
email = st.empty()
senha = st.empty()


def criar_usuario(nome, email, senha, bio=None, imagem_perfil=None, grupo=1):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Verifica se o e-mail já está cadastrado
    cursor.execute('SELECT COUNT(*) FROM usuarios WHERE email = ?', (email,))
    if cursor.fetchone()[0] > 0:
        st.error('E-mail já cadastrado')
        conn.close()
        return False

    # Insere o novo usuário no banco de dados
    cursor.execute('''
        INSERT INTO usuarios (
            nome,
            email,
            senha,
            bio,
            imagem_perfil,
            grupo_id
        ) VALUES (?, ?, ?, ?, ?,?)
    ''', (nome, email, senha, bio, imagem_perfil, grupo))
    conn.commit()
    progress_text = "Seu Usuario esta sendo criado, por favor aguarde:"
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    conn.close()
    # Limpa os campos após a criação do usuário

    return True


st.title('Criar Usuario')
nome = st.text_input('Nome', value='', key='nome')
email = st.text_input('E-mail',  value='', key='email')
senha = st.text_input('Senha', type='password', value='', key='senha')
# bio = st.text_area('Bio')
# imagem_perfil = st.file_uploader('Foto de perfil',
# type=['jpg', 'jpeg', 'png'])

if st.button('Criar conta'):
    if criar_usuario(nome, email, senha):
        st.success('Usuário criado com sucesso!')
