#produtos
Produtos = {
    100: {"codigo" :100, "item": "Cachorro Quente", "valor":1.70},
    101: {"codigo" :101, "item": "Bauru Simples", "valor":2.30},
    102: {"codigo" :102, "item": "Bauru com ovo", "valor":2.60},
    103: {"codigo" :103, "item": "Hamburguer", "valor":2.40},
    104: {"codigo" :104, "item": "Cheeseburguer", "valor":2.50},
    105: {"codigo" :105, "item": "Refrigerante", "valor":1.00}
}
#dicionario_com_num_int
Pagamentos = {
    1: {"forma_pag" :1, "Forma de Pagamento" :"Debito ou dinheiro", "porcentagem" :0.5},
    2: {"forma_pag" :2, "Forma de Pagamento" : "PIX", "porcentagem" :0.8},
    3: {"forma_pag" :3, "Forma de Pagamento" :"3x - Sem juros"},
    4: {"forma_pag" :4, "Forma de Pagamento" :"De 4x a 10x - Juros de 0.2 por mês", "porcentagem": +0.2}
}
print ("\n")
codigo=int(input("Digite o código do produto: "))
quantidade=int(input("Digite a quantidade: "))
forma_pag=int
print ("\n")
if codigo in Produtos: 
    produto = Produtos[codigo]
    nome = produto["item"]
    precoun = produto["valor"]
    total = precoun * quantidade

    print (f"Produto: {nome}")
    print (f"Valor por produto: {precoun}")
    print (f"Valor total da compra: {total}")
    print ("\n")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print("|1 - Debito ou dinheiro com desconto de 5% -|")
    print("|2 --------PIX com desconto de 8%-----------|")
    print("|3 ----------- 3x - Sem juros---------------|")
    print("|4 ---- 4x a 10x - Juros de 2% por mês------|")
    print("|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|")
    print ("\n")
    pagamento = int(input("Digite sua forma de pagamento de 1 a 4 com base no menu acima: "))
    
    if pagamento == 1:
        total = (total - 0.05)
        print(f"Você ganhou um deconto de 5%, o valor da sua compra é de: {total}")
    if pagamento == 2:
        total = (total - 0.08)
        print(f"Você ganhou um deconto de 8%, o valor da sua compra é de: {total}")
    if pagamento == 3:
        total = total / 3 
        vtotal = total * 3
        print(f"O valor para cada parcela é de: {total} e o valor total é de: {vtotal}")

    

    
    if pagamento == 4:
        parcela=int(input("Escolha o número de parcelas de 4 a 10: "))
        if parcela == 4:
            juros= 0.02 * parcela #juros de 2% aos mês
            valor_final = total * (1+ juros)#calculando o valor total com juros
            valor_parcela = valor_final / parcela #valor de cada parcela
            print(f"O valor total da compra com juros será de:{valor_final} ")
            print(f"O valor para cada parcela ({parcela}x) é de: {valor_parcela} ")           
        elif parcela == 5:
            juros = 0.02 * parcela #juros de 2% aos mês
            valor_final = total * (1+ juros)#calculando o valor total com juros
            valor_parcela = valor_final / parcela #valor de cada parcela
            print(f"O valor total da compra com juros será de:{valor_final} ")
            print(f"O valor para cada parcela ({parcela}x) é de: {valor_parcela} ")
        elif parcela == 6:
            juros = 0.02 * parcela #juros de 2% aos mês
            valor_final = total * (1+ juros)#calculando o valor total com juros         
            valor_parcela = valor_final / parcela #valor de cada parcela
            print(f"O valor total da compra com juros será de:{valor_final} ")
            print(f"O valor para cada parcela ({parcela}x) é de: {valor_parcela} ")  
        elif parcela == 7:
            juros = 0.02 * parcela #juros de 2% aos mês
            valor_final = total * (1+ juros)#calculando o valor total com juros         
            valor_parcela = valor_final / parcela #valor de cada parcela
            print(f"O valor total da compra com juros será de:{valor_final} ")
            print(f"O valor para cada parcela ({parcela}x) é de: {valor_parcela} ")  
        elif parcela == 8:
            juros = 0.02 * parcela #juros de 2% aos mês
            valor_final = total * (1+ juros)#calculando o valor total com juros         
            valor_parcela = valor_final / parcela #valor de cada parcela
            print(f"O valor total da compra com juros será de:{valor_final} ")
            print(f"O valor para cada parcela ({parcela}x) é de: {valor_parcela} ")  
        elif parcela == 9:
            juros = 0.02 * parcela #juros de 2% aos mês
            valor_final = total * (1+ juros)#calculando o valor total com juros         
            valor_parcela = valor_final / parcela #valor de cada parcela
            print(f"O valor total da compra com juros será de:{valor_final} ")
            print(f"O valor para cada parcela ({parcela}x) é de: {valor_parcela} ")  
        elif parcela == 10:
            juros = 0.02 * parcela #juros de 2% aos mês
            valor_final = total * (1+ juros)#calculando o valor total com juros         
            valor_parcela = valor_final / parcela #valor de cada parcela
            print(f"O valor total da compra com juros será de:{valor_final} ")
            print(f"O valor para cada parcela ({parcela}x) é de: {valor_parcela} ")  
    else:
        if pagamento in Pagamentos:
            pagamento = Pagamentos [forma_pag]
            nome = pagamento ["Forma de Pagamento"]
            porcentagem = pagamento ["porcentagem"]
        

else:
    print ("Produto não encontrado, digite um código válido.")