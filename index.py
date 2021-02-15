
from reportlab.pdfgen import canvas
from flask import redirect
import paypalrestsdk
def GeneratePDF(lista):
    try:
        nome_pdf = input('Informe o nome do PDF: ')
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        x = 720
        for nome,idade in lista.items():
            x -= 20
            pdf.drawString(247,x, '{} : {}'.format(nome,idade))
        pdf.setTitle(nome_pdf)
        pdf.setFont("Helvetica-Oblique", 14)
        pdf.drawString(245,750, 'Lista de Convidados')
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(245,724, 'Nome e idade')
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))


#lista={"nome":"10"}
#GeneratePDF(lista)
def gerarPagamento():
    paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "AQMMO-E46etPWKENRZl2GI1wiAGFomixikiELmMrUtNNJm3rsu0qj-L6CeyDyIByGqfK5LHel6eQnYdW",
  "client_secret": "EEzBRBr1CM5eNNyOIVryu6BPIhZ8dOQFVzH88fQwDgRjwBlnnLbzYftUjLbLMe-taDn8MP_zx4vQpdiT" })
    payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"},
    "redirect_urls": {
        "return_url": "http://localhost:3000/payment/execute",
        "cancel_url": "http://localhost:3000/"},
    "transactions": [{
        "item_list": {
            "items": [{
                "name": "item",
                "sku": "item",
                "price": "5.00",
                "currency": "USD",
                "quantity": 1}]},
        "amount": {
            "total": "5.00",
            "currency": "USD"},
        "description": "This is the payment transaction description."}]})

    if payment.create():
        print("Payment created successfully")
    else:
        print(payment.error)
    for link in payment.links:
        if link.rel == "approval_url":
        # Convert to str to avoid Google App Engine Unicode issue
        # https://github.com/paypal/rest-api-sdk-python/pull/58
            approval_url = str(link.href)
            print("Redirect for approval: %s" % (approval_url))
            redirect(approval_url)
            return 'Boleto'
    #payment = paypalrestsdk.Payment.find("PAY-57363176S1057143SKE2HO3A")
    
    #if payment.execute({"payer_id": "DUFRQ8GWYMJXC"}):
    #print("Payment execute successfully")
    #else:
    #print(payment.error) # Error Hash
gerarPagamento()