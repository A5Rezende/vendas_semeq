# 📦 Projeto Django - Nome do Projeto

Este é um sistema desenvolvido com Django, um framework web Python. Siga as instruções abaixo para rodar o projeto em sua máquina.

## ✅ Requisitos

Antes de começar, verifique se você tem instalado:

- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [pip](https://pip.pypa.io/en/stable/)
- [PostgreSQL](https://www.postgresql.org/download/)

> **Obs:** Certifique-se de que o PostgreSQL esteja rodando e que você criou um banco de dados e um usuário com permissões.

---

## 🚀 Como rodar o projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/A5Rezende/vendas_semeq.git
cd vendas_semeq
```

2. **Instale as dependências do projeto:**

```bash
pip install django 
pip install django psycopg2
```

3. **Configure o banco de dados:**

```bash
Crie um banco de dados PostegreSQL

Edite o arquivo settings.py com as informções do seu banco de dados:

DB_NAME=seu_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432

```

4. **Rode as migrações para preparar o banco de dados:**

```bash
python manage.py migrate
```

5. **Carregue os dados iniciais (fixtures):**

```bash
python manage.py loaddata vendas/fixtures/dados_iniciais.json
```

6. **Inicie o servidor:**

```bash
python manage.py runserver
```