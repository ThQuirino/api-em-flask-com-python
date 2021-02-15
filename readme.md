# api-em-flask-com-python

Api feita em python utilizando o **Flask** criando um sistema de confirmação de compra em ambiente interno.
<hr>

### Instalação:
É preciso ter a versão acima da 3.6<a href='https://www.python.org/'>Python.py</a> instalada juntamente com o banco de dados postgres instalado em seu computador. É necessário ter instalado e configurado o drive para rodar o banco, Recomendo o psycopg para configuração do mesmo.
também é necessário instalar o gerenciador de pacotes **Pip**. 
Após isso, basta rodar o comando no terminal:

```
pip install pipenv
```
dentro da pasta do arquivo: 
```
pipenv install
```
para subir a virtualização:
```
pipenv shell
```
depois: 
```
python server.py runserver
```
### Banco de dados:
Modifique o arquivo **database.py** dentro da pasta **SRC**, colocando as suas configurações do banco.
<hr> 

### 🚀 Tecnologias utilizadas:
  - Python;
  - Peewee;
  - PostgreSql;
  - Pipenv;
  - Flask;
  