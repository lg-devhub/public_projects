# Escreva um código que verifique se uma pessoa é alfabetizada 
# (sabe ler e escrever) e tem mais de 25 anos de idade.

idade = int(input("Sua idade:"))
firstphrase = int(input("Quantas letras tem o alfabeto?"))
secondphrase = str(input("Qual é a primeira letra da palavra 'casa'?"))
thirdphrase = str(input("Escreva/digite por extenso o nome do objeto que contém tinta para escrever")).strip().lower()

if firstphrase == 26 and secondphrase == 'c' and thirdphrase == 'caneta' and idade > 25:
    print("É alfabetizado e tem mais de 25 anos de idade")
elif firstphrase == 26 and secondphrase == 'c' and thirdphrase == 'caneta' and idade < 25:
        print("É alfabetizado e tem menos de 25 anos de idade")

