# Escreva um programa que peça ao usuário inserir duas notas (entre 0 e 100) e determine se o aluno passou ou não. 
# Um aluno passa se a soma das notas for maior ou igual a 60 e nenhuma nota é menor que 40.

nota01 = float(input("Apresente a primeira nota (entre 0 e 100)"))
nota02 = float(input("Apresente a segunda nota (entre 0 e 100)"))
somanota = nota01 + nota02

if somanota < 40:
    print("Notas acima de 40, apenas. Reinicie o programa")
elif somanota >= 60:
    print("O aluno está aprovado")
else:
    print("Reprovado")

