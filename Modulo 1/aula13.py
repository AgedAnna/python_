

age = int(input("Digite sua idade"))
print(f'sua idade : {age}')

if age > 18:
    print("pode dirigir")
else:
    print("foi triste")


produtos = []

print("Bem vindo ao mercado da Anna")
print("Produtos:")

condicao = str(input("Deseja adicionar produtos ?"))

while condicao == "sim" :
    print("Bem vindo ao mercado")
    condicao = str(input("Deseja adicionar produtos ?"))

    if condicao == "nao":
        break