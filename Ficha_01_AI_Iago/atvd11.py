## Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir para ler qual acondição de pagamento escolhida e efetuar o cálculo adequado.

## Código Condição de pagamento
## 1 À vista em dinheiro ou cheque, recebe 10% de desconto
## 2 À vista no cartão de crédito, recebe 15% de desconto
## 3 Em duas vezes, preço normal de etiqueta sem juros
## 4 Em duas vezes, preço normal de etiqueta mais juros de 10%

name_product = str(input("Digite o nome do produto: "))
value_product = float(input("Digite o valor do produto: "))

pay = int(input("1 À vista em dinheiro ou cheque, 2 À vista no cartão de crédito, 3 Em duas vezes, 4 Em duas vezes "))

def forma_de_pagamento(pay):
    if pay == 1:
        descont = value_product - (value_product * 10)/100
        return(descont)

    elif pay == 2:
        descont = value_product - (value_product * 15)/100
        return(descont)

    elif pay == 3:
        return(value_product)
    
    elif pay == 4:
        descont = value_product + (value_product * 10)/100
        return(descont)

    else:
        return("Forma de pagamento não encontrada!")



print(forma_de_pagamento(pay))