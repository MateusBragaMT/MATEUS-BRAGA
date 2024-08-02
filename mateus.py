quantidade_produtos = int(input("Quantos produtos você deseja cadastrar? "))

lista_produtos = []  

for _ in range(quantidade_produtos):
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))
    
    produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
    lista_produtos.append(produto)

soma_quantidades = 0
soma_precos = 0

print("\nNomes dos produtos cadastrados:")
for produto in lista_produtos:
    print(produto["nome"])
    soma_quantidades += produto["quantidade"]
    soma_precos += produto["preco"]

media_precos = soma_precos / soma_quantidades

print("\nSoma de todas as quantidades:", soma_quantidades)
print("Média dos preços:", media_precos)
