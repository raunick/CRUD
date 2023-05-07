import sqlite3

# conecte-se ao banco de dados
conn = sqlite3.connect('database.db')

# crie a tabela de usuários
conn.execute('''
CREATE TABLE usuarios (
  id INTEGER PRIMARY KEY,
  nome TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  senha TEXT NOT NULL,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  bio TEXT, -- biografia do usuário
  imagem_perfil TEXT -- URL da imagem do perfil do usuário
);
''')

# crie a tabela de grupos
conn.execute('''
CREATE TABLE grupos (
  id INTEGER PRIMARY KEY,
  nome TEXT NOT NULL,
  descricao TEXT,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  alterado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  palavras_chave TEXT, -- palavras-chave relevantes para o grupo
  imagem_capa TEXT, -- URL da imagem de capa do grupo
  url_amigavel TEXT -- URL amigável para o grupo
);
''')

# crie a tabela de logs
conn.execute('''
CREATE TABLE logs (
  id INTEGER PRIMARY KEY,
  usuario_id INTEGER NOT NULL,
  data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
);
''')

# salve as mudanças
conn.commit()

# feche a conexão com o banco de dados
conn.close()
