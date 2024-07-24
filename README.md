# ToDo API

API para gerenciar tarefas (ToDo) construída com Django REST Framework.

## Instalação

1. Clone o repositório

```bash
git clone git@github.com:joaosenger/todo_api.git # ssh
git clone https://github.com/joaosenger/todo_api.git # https
cd todo_api
```

2. Crie um ambiente virtual (não é obrigatório, mas é recomendado):

```bash
python -m venv venv # cria o ambiente virtual
source venv/bin/activate # ativa o ambiente virtual para Linux/MacOS
.\venv\Scripts\Activate.ps1 # ativa o ambiente virtual para Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Inicialização

```bash
python manage.py migrate  # inicializa as tabelas default do Django no banco de dados
python manage.py createsuperuser  # cria o usuário root
python manage.py runserver  # inicia o servidor de desenvolvimento
```

Um banco de dados SQLite será criado localmente chamado `db.sqlite3`. Para utilização em produção, recomenda-se um banco de dados mais robusto, ex.: PostgreSQL, MySQL, Oracle, etc.

Acesse https://127.0.0.1:8000/admin para acessar o Django Admin com o usuário root criado anteriormente. Aqui serão administrados os usuários da api e permissões / grupos de permissões e acesso.  

Para usar a API, segue:  

**Gerar token JWT:**  
`POST` 127.0.0.1:8000/api/v1/authentication/token/  
```json
{
    "username": "usuario",
    "passwork": "senha"
}
```  

**API ToDo:**  
Autorização: `Bearer: tokenJwt`  
`GET` 127.0.0.1:8000/api/v1/todos/ `retorna todas as tarefas`  
`GET` 127.0.0.1:8000/api/v1/todos/<int:pk> `retorna a tarefa do id especificado`  
`POST` 127.0.0.1:8000/api/v1/todos/ `cria uma nova tarefa`  
```json
{
    "task": "Nome da tarefa",
    "done": false
}
```  
`PUT` 127.0.0.1:8000/api/v1/todos/<int:pk> `altera os dados da tarefa do id especificado`  
```json
{
    "task": "Nome da tarefa",
    "done": false
}
```  
`DELETE` 127.0.0.1:8000/api/v1/todos/<int:pk> `deleta a tarefa do id especificado`  

## Linter: Flake8  

O Linter Flake8 está configurado no projeto. Recomendo que ao implementar novas funcionalidades nesse projeto o padrão de código e boas práticas da PEP 8 sejam mantidos.  

Para executar a verificação do linter:  

```bash
flake8
```
