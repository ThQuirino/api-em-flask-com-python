##Todas as tabelas são criadas aqui caso não exista ainda, e depois é gerado um arquivo (.db) com as nossas tabelas
import datetime
import peewee
pg_db =peewee.PostgresqlDatabase('val', user='postgres', password='postgres',host='127.0.0.1', port=5432)
class BaseModel(peewee.Model):
    class Meta:
        database=pg_db

class Cliente(BaseModel):    
    """
    """
    # A tabela possui apenas o campo 'name', que receberá o nome do autor sera unico
    name = peewee.CharField(unique=True)
    cpf=peewee.CharField()
    data_nascimento=peewee.DateField()
    email=peewee.CharField()
    timestamp = peewee.DateTimeField(default=datetime.datetime.now)
class Produto(BaseModel):
    """
   
    """
    # A tabela possui apenas o campo 'title', que receberá o nome do livro 
    name = peewee.CharField(unique=True)
    preco = peewee.FloatField()
    fotos = peewee.CharField(unique=True)
    descricao_produto=peewee.TextField()
    timestamp =peewee.DateTimeField(default=datetime.datetime.now)
    # Chave estrangeira para a tabela Author
   ## author = peewee.ForeignKeyField(Author)
if __name__ == '__main__':
    try:
        Cliente.create_table()
        print("Tabela 'Author' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Author' ja existe!")
    try:
        Produto.create_table()
        print("Tabela 'Produto' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Produto' ja existe!")
 