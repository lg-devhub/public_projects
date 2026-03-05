# Escreva um código que verifique se um número é par ou divisível por 3.

digitado = int(input("Apresente um valor numérico"))


if digitado % 2 == 0:
    print("O número é par")
elif digitado % 2 != 0:
    print("O número é divisível por 3")
    