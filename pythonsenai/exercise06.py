# Criar um programa que verifica se uma pessoa tem desconto em um produto, 
# baseado na idade e sua categoria (estudante, aposentado, etc.) e no dia da semana. 
# (Use quantas categorias desejar)

# Entrada de dados

idade = int(input("Digite sua idade: "))
categoria = input("Digite sua categoria (estudante, aposentado, comum): ").lower()
dia = input("Digite o dia da semana: ").lower()

desconto = False


if idade >= 60:
    desconto = True
elif categoria == "estudante" and dia == "quarta":
    desconto = True
elif categoria == "aposentado":
    desconto = True


if desconto:
    print("Você tem direito a desconto no produto!")
else:
    print("Você não tem direito a desconto.")