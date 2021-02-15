from .database import Produto
class bancoCreate:
    def inserirProduto(self):
        Produto1 = {
        
            'name': 'camiseta',
            'preco': 15.40,
            'fotos':"camiseta.png",
            'descricao_produto':"roupa",
        
        }
        Produto2 = {
        
            'name': 'guitarra',
            'preco': 105.65,
            'fotos':"guitarra.png",
            'descricao_produto':"música",
            
        }
        produtosNovos=[Produto1,Produto2]
        Produto.insert_many(produtosNovos).execute()

bancoCreate.inserirProduto()