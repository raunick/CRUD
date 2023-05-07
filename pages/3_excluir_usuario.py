import streamlit as st
import sqlite3


def excluir_usuario(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=?", (id,))
    conn.commit()
    print("Usuário excluído com sucesso!")
    st.warning('Usuário excluído com sucesso!')
    conn.close()


st.title('Excluir Usuario')
id = st.text_input('ID', value='', key='chave')

if st.button('Excluir conta:'):
    if excluir_usuario(id):
        st.warning('Usuário excluído com sucesso!')
