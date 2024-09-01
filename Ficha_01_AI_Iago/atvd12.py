## Escreva um algoritmo que leia o número de identificação, as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a média de aproveitamento, usando a fórmula:
# MA := (nota1 + nota 2 * 2 + nota 3 * 3 + ME)/7
# A atribuição dos conceitos obedece a tabela abaixo. O algoritmo deve escrever o número do aluno, suas notas, a média dos exercícios, a média de aproveitamento, o conceito correspondente e a mensagem 'Aprovado' se o conceito for A, B ou C, e 'Reprovado' se o conceito for D ou E.
# Média de aproveitamento Conceito 
# >= 90 A
# >= 75 e < 90 B >= 60 e < 75 C >= 40 e < 60 D < 40 E

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 1: "))
n3 = float(input("Digite a nota 1: "))
me = float(input("Digite a média dos exercícios: "))

ma = (n1 + n2 * 2 + n3 * 3 + me)/7

