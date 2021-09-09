# Biblioteca Local Django

Seguindo este tutorial

https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/skeleton_website

repositorio 
https://github.com/mdn/django-locallibrary-tutorial

## Visão geral

Este aplicativo da web cria um catálogo online para uma pequena biblioteca local, onde os usuários podem navegar pelos livros disponíveis e gerenciar suas contas.

Os principais recursos que foram implementados atualmente são:

* Existem modelos de livros, cópias de livros, gênero, linguagem e autores.
* Os usuários podem visualizar listas e informações detalhadas de livros e autores.
* Os usuários administradores podem criar e gerenciar modelos. O admin foi otimizado (o registro básico está 
presente em admin.py, mas comentado).
* Os bibliotecários podem renovar livros reservados



## Quick Start

Para colocar este projeto em execução localmente em seu computador:

1. Configure o [ambiente de desenvolvimento Python](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/development_environment). Recomendamos o uso de um ambiente virtual Python.

2. Supondo que você tenha o Python configurado, execute os seguintes comandos (se você estiver no Windows, pode usar `py` ou em `py -3` vez de `python` para iniciar o Python):

   ```
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py collectstatic
   python3 manage.py test # Run the standard tests. These should all pass.
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```
3. Abra um navegador `http://127.0.0.1:8000/admin/` para abrir o site de administração
4. Crie alguns objetos de teste de cada tipo.
5. Abra a aba para `http://127.0.0.1:8000` ver o site principal, com seus novos objetos.