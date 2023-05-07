import streamlit as st
import sqlite3


def obter_usuario_por_id(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id=?", (id,))
    usuario = cursor.fetchone()
    conn.close()

    if usuario:
        st.success('Usuário localizado com sucesso!')
        return usuario
    else:
        st.error('Usuário não encontrado.')
        return None


st.title('Buscar Usuario')
id = st.text_input('ID', value='', key='id')

if st.button('Buscar conta', key='buscar'):
    usuario = obter_usuario_por_id(id)
    if usuario:
        st.write('Usuário encontrado:')
        st.code(usuario)
    else:
        st.info('Digite um ID válido.')
