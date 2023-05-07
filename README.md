# CRUD_SQLITE_OTP_STREAMLIT_PYTHON
# 🔍 CRUD de usuários com SQLite, OTP e Streamlit em Python
Este é um projeto de CRUD (Create, Read, Update, Delete) de usuários que usa SQLite como banco de dados, OTP (One-Time Password) para autenticação e Streamlit como framework de interface do usuário, tudo escrito em Python.

# 🚀 Como executar o projeto
Clone este repositório.
Instale as dependências do projeto executando pip install -r requirements.txt. 
```sh
pip install -r requirements.txt.
```
Execute o aplicativo com o comando streamlit run Crud.py.
```sh
streamlit run Crud.py.
```
# 🛠️ Melhorias
Este projeto é um ótimo ponto de partida para construir aplicativos Python com Streamlit, SQLite e OTP, mas há algumas melhorias que podem ser feitas para torná-lo mais robusto e escalável. Algumas sugestões incluem:

Separar a lógica de negócios da lógica de interface do usuário
Usar uma camada de abstração de banco de dados, como o ORM SQLAlchemy
Validar a entrada do usuário antes de passá-la para o banco de dados
Usar mensagens de erro claras e descritivas
Organizar o código em funções com nomes descritivos
Usar a convenção de nomenclatura Python
# 🤝 Contribuição
Se você quiser contribuir para este projeto, por favor, abra uma issue ou envie uma pull request. Sua contribuição é muito bem-vinda!

# 💻 Funcionalidades existentes do projeto

- Adicionar um novo usuário 🆕👤: permite adicionar um novo usuário ao banco de dados, incluindo seu nome, endereço de e-mail e senha. Ao clicar no botão de adicionar, o usuário será criado e uma mensagem de sucesso será exibida.

- Editar as informações de um usuário existente 📝👤: permite editar as informações de um usuário existente no banco de dados, incluindo seu nome, endereço de e-mail e senha. Ao clicar no botão de editar, as informações do usuário serão atualizadas e uma mensagem de sucesso será exibida.

- Excluir um usuário existente 🗑️👤: permite excluir um usuário existente do banco de dados. Ao clicar no botão de excluir, o usuário será removido do banco de dados e uma mensagem de sucesso será exibida.

 - Gerar e enviar um código OTP para o Google Authenticator do usuário ✉️🔑📧: permite gerar um código OTP (One-Time Password) e enviar para o Google Authenticator do usuário por e-mail. Esse código é usado para autenticar o usuário no aplicativo. Ao clicar no botão de gerar, um código OTP será enviado para o e-mail do usuário e uma mensagem de sucesso será exibida.

- Verificar o código OTP inserido pelo usuário e permitir ou negar o acesso 🔑✅❌: permite verificar o código OTP inserido pelo usuário e permitir ou negar o acesso ao aplicativo. Se o código for válido, o acesso será permitido e uma mensagem de sucesso será exibida. Caso contrário, o acesso será negado e uma mensagem de erro será exibida.

- Buscar um usuário por ID 🔎👤: permite buscar um usuário específico pelo seu ID no banco de dados. Ao inserir o ID do usuário e clicar no botão de buscar, as informações do usuário serão exibidas na tela.

- Listar todos os usuários cadastrados 📜👥: permite listar todos os usuários cadastrados no banco de dados. Ao clicar no botão de listar, as informações de todos os usuários serão exibidas na tela.
