# Função para saber quanto o preço de um produto fica com desconto
preco_original = float(input("Digite o preço original do produto: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

def calcular_desconto(preco_original, percentual_desconto):
    desconto = (preco_original * percentual_desconto) / 100
    preco_com_desconto = preco_original - desconto
    return preco_com_desconto

preco_final = calcular_desconto(preco_original, percentual_desconto)

print(f"O preço final após aplicar o desconto é: R${preco_final:.2f}")