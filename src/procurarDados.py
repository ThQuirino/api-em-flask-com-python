from .database import Cliente,Produto
from flask import render_template
import index

class bancoDados:
    def __init__(self,valor):
        self.valor=valor
    def procurarProduto(self):
        try:
            produtos = Produto.get(Produto.name == self.valor).get()
            print(produtos.name,produtos.preco)
        except:
            return 'erro'
        
    def procurarCpf(self):
            try:
                usuario = Cliente.get(Cliente.cpf == self.valor).get()
                lista = {usuario.name: usuario.data_nascimento}
                index.gerarPagamento()
                return 'ok'
                #index.GeneratePDF(lista)
            except:
                return 'erro'

   # def genericoBancoProcurar(self):
   #    if('cpf' in self.valor):
   #       try:
   #             usuario = Cliente.get(Cliente.cpf == self.valor).get()
   #             lista = {usuario.name: usuario.data_nascimento}
   #             index.GeneratePDF(lista)
   #         except:
   #             return 'erro'
   #     else:
   #         try:
   #             produtos = Produto.get(Produto.name == self.valor).get()
   #             print(produtos.name,produtos.preco)
   #         except:
   #             return 'erro'