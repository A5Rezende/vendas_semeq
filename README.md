# 📦 Projeto Django - Nome do Projeto

Este é um sistema desenvolvido com Django, um framework web Python. Siga as instruções abaixo para rodar o projeto em sua máquina.

## ✅ Requisitos

Antes de começar, verifique se você tem instalado:

- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [pip](https://pip.pypa.io/en/stable/)
- [postgreSQL]

---

## 🚀 Como rodar o projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/usuario/nome-do-projeto.git
cd nome-do-projeto

2. **Configure as dependencias:**

```bash
git clone https://github.com/usuario/nome-do-projeto.git
cd nome-do-projeto

3. **Rode as migrações para preparar o banco de dados:**

```bash
python manage.py migrate

4. **Rode as os dados iniciais para preparar o banco de dados:**

```bash
python manage.py loaddata vendas/fixtures/dados_iniciais.json

5. **Inicie o servidor:**

```bash
python manage.py runserver

6. **Acesse o navegador:**

```bash
http://127.0.0.1:8000/