from flask import Flask, render_template,request
import index
import re
from src import procurarDados
from src import inserir
app=Flask("PDF")
@app.route('/',methods=["GET","POST"])
def index():
    #if __name__=='__main__':
    if(request.method =='POST'):
        valor=request.form.get("name")
        comparar=re.match(r'\s',valor)
        if(comparar != None or valor ==''):
            return "o campo nao deve ser nulo" 
        else:
            
            ProdutoBanco=procurarDados.bancoDados(valor) 
            if(ProdutoBanco.procurarProduto()=='erro'):
                return 'produto em falta no estoque'

        return render_template('dados.html')
    return render_template('index.html')


@app.route('/enviar',methods=['GET','POST'])
def enviar_dados():
    if(request.method=='POST'):
        nome=request.form.get("nome")
        email=request.form.get("email")
        cpf=request.form.get("cpf")
        data=request.form.get("data")
        comparar=re.match(r'[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}',cpf) 
        if(comparar == None or cpf ==''):
            print('cpf invalido')
            return render_template('dados.html')
        else:
            lista={"nome":nome,"email":email,"cpf":cpf,"data":data}
            ClienteBanco=inserir.inserirBanco().inserCliente(lista)
            if(ClienteBanco=='Boleto'):
               return render_template('final.html')
            else:
               return render_template('cadastro.html')
    return render_template('dados.html') 


@app.route('/cadastrado',methods=['GET','POST'])
def enviar_dados_cadastrados():
    if(request.method=='POST'):
        cpf=request.form.get("cpf")
        comparar=re.match(r'\s',cpf)
        if(comparar != None or comparar ==''):
            return "o campo nao deve ser nulo" 

        else:
            ProdutoBanco=procurarDados.bancoDados(cpf)
            if(ProdutoBanco.procurarCpf()=='erro'):
                print('Nome errado. Por favor, digite novamente')
                return render_template('cadastro.html')
        return render_template('final.html')
    return render_template('cadastro.html')
app.run()