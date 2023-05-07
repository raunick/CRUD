import streamlit as st
import sqlite3
# import time

nome = st.empty()
email = st.empty()
senha = st.empty()


def atualizar_usuario(id,
                      nome=None,
                      email=None,
                      senha=None,
                      bio=None,
                      imagem_perfil=None):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
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
    st.success('Usuário criado com sucesso!')
    conn.close()


st.title('Editar Usuario')
id = st.text_input('ID', value='', key='chave')
nome = st.text_input('Nome', value='', key='update_nome')
email = st.text_input('E-mail',  value='', key='update_email')
senha = st.text_input('Senha', type='password', value='', key='update_senha')
# bio = st.text_area('Bio')
# imagem_perfil = st.file_uploader('Foto de perfil',
# type=['jpg', 'jpeg', 'png'])

if st.button('Atualizar conta:'):
    if atualizar_usuario(id, nome, email, senha):
        st.success('Usuário criado com sucesso!')
