#Verifique se uma pessoa é maior ou igual a 18 anos ou se ela tem autorização dos pais.

nome = str(input("Seu nome:"))
idade = int(input("Sua idade:"))
auth = str(input("Se é menor de idade, tem a permissão dos pais? (sim/não)")).strip().lower()
 
if idade >= 18 or auth == "sim":
    print("Liberado")
else:
    print("Negado")
