#produtos

Produtos = {
    100: {"codigo" :100, "item": "Cachorro Quente", "valor":1.70},
    101: {"codigo" :101, "item": "Bauru Simples", "valor":2.30},
    102: {"codigo" :102, "item": "Bauru com ovo", "valor":2.60},
    103: {"codigo" :103, "item": "Hamburguer", "valor":2.40},
    104: {"codigo" :104, "item": "Cheeseburguer", "valor":2.50},
    105: {"codigo" :105, "item": "Refrigerante", "valor":1.00}
}

codigo=int(input("Digite o código do produto: "))
quantidade=int(input("Digite a quantidade: "))

if codigo in Produtos: 
    produto = Produtos[codigo]
    nome = produto["item"]
    precoun = produto["valor"]
    total = precoun * quantidade

    print (f"Produto: {nome}")
    print (f"Valor por produto: {precoun}")
    print (f"Valor total da compra: {total}")
else:
    print ("Produto não encontrado, digite um código válido.")