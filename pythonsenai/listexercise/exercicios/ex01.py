# Exercício 1 — Classificador de notas
# Crie uma função classificar_nota(nota) 
# que receba uma nota e retorne "Excelente", 
# "Aprovado", "Recuperação" ou "Reprovado" conforme a faixa. 
# Chame a função para cada nota de uma lista usando for.

def classificar_nota(nota):
    if nota >= 8:
        return "Excelente"
    if nota <= 7 and nota > 5:
        return "Aprovado"
    if nota == 5:
        return "Recuperação"
    if nota < 5:
        return "Reprovado"

nota = float(input("Apresente o valor: "))
print(classificar_nota(nota))