from .database import Cliente,Produto
from flask import render_template
import index
class inserirBanco: 
    def inserCliente(self,valor):
        Cliente1={
            'name': valor['nome'],
            'cpf': valor['cpf'],
            'data_nascimento':valor['data'],
            'email':valor['email']
        }
        try:
            Cliente.insert_many(Cliente1).execute()
            ##Cliente.save()
            #index.GeneratePDF()
            resultadoQuery=Cliente.select().where(Cliente.name== valor['nome']).get()
            lista = {resultadoQuery.name: resultadoQuery.data_nascimento}
            index.gerarPagamento()
            render_template(index.gerarPagamento())
            #index.GeneratePDF(lista)
            return render_template('final.html')
        except:
            return render_template('cadastro.html')
        