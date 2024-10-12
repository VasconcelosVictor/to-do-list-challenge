# Desafio Lista de Tarefas

## Introdução

**Lista de Tarefas** é um aplicativo que permite a criação de tarefas e registro de tempo pra cada tarefa.

## Funcionalidades

- Autenticação
- Crud e Tarefase Registro de tempo
- Filtros nas paginas de Tarefa e Registro de tempo

## Modelagem 

+---------------------+           +--------------------------+
|      User          |           |         Tasks             |
|---------------------|           |--------------------------|
| - id                |<-------+  | - id                     |
| - username          |        |  | - user (FK to User)      |
| - password          |        +--| - created_at             |
| - email             |           | - description            |
+---------------------+           | - status                 |
                                  |--------------------------|
                                  | + get_time_record()       |
                                  +--------------------------+
                                              |
                                              |  1-to-1
                                              |
                                  +--------------------------+
                                  |     TimeRecord            |
                                  |--------------------------|
                                  | - registration_date       |
                                  | - minutes_worked          |
                                  | - description             |
                                  | - task (OneToOne to Tasks)|
                                  +--------------------------+
                                  | + convert_minutes()       |
                                  +--------------------------+

                                  

## Requisitos

- Python 
- Django 
- Mysql

## Instalação

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/VasconcelosVictor/to-do-list-challenge.git
    ```

2. **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

4. **Instale as dependências do backend:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Configure o banco de dados:**

    Crie um banco de dados na sua maquina e modifique as configurações de Banco de Dados pra sua Base.
    ```python
          DATABASES = {
              ''default': {
              'ENGINE': 'django.db.backends.mysql',  
              'NAME': 'NOME_DO_SEU_DATABASE',               
              'USER': 'SEU_USUÁRIO',                     
              'PASSWORD': 'SUA_SENHA',                  
              'HOST': 'localhost',                   
              'PORT': '3306',                      
          }
    
        }
    
     ```
## Execulte os Migrations do projeto 
    ```bash
    python manage.py migrate
    ```

6. **Crie um superusuário:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

8. **Acesse a aplicação:**
    Abra o navegador e vá para `http://localhost:8000`



## CASO DE TESTE 
  ```bash
    python manage.py test task
  ```


## Uso / Funcionalidades

## USUÁRIO
- **Registro de Usuário:** Para adicionar um usuário acesse a roda /admin do django clique em adicionar usuário e preencha os campos.
- **Login:** Faça login com suas credenciais.

## TAREFAS 
- **Cadastro de Tarefa:** Clique em Adicionar Tarefa e Insira um Título na sua tarefa.
- **Editar Tarefa:** Na tela de Lista de Tarefas clique em cima do Título da Tarefa que deseja editar e você vai ser redirecionado pra tela de edição.
- **Listar Tarefas:** Na Barra de navegação basta clicar na aba Tarefas que você já está na pagina de listagem.
- **Deletar:** Para deletar um tarefa basta você clicar no icone de lixeira dentro da lista.
- **Alterar Status:** Para Alterar o status da tarefa basta clicar em cima do status da tarefa que voce deseja alterar e pronto ele ja vai ser alterado.
- **Filtrar:** Pra filtrar uma tarefa basta clicar em filtros e aplicar a pesquisa que deseja fazer.
  
## REGISTRO DE TEMPO
- **Cadastro de Registro de tempo:** Clique em Registrar Tempo e insira as informações do registro.
- **Editar Registro de tempo:** Pra Editar é o mesmo processo basta clicar no mesmo botão e você vai ser levado pra tela de edição.
- **Listar Registro de tempo:** Na Barra de navegação basta clicar na aba Registro que você já está na pagina de listagem.
- **Deletar Registro de tempo:** Pra deletar um Registro basta você clicar no icone de lixeira dentro da lista.
- **Filtrar Registro de tempo:** Pra filtrar uma Registro basta clicar em filtros e aplicar a pesquisa que deseja fazer.


## Contato

- **Nome:** Victor Vasconcelos
- **LinkedIn:** [meu linkedin](https://www.linkedin.com/in/victor-vasconcelos-barbosa/)




