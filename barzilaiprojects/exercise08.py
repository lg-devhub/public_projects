secret_number = 42
tryit = 1

while tryit <= 3:
    iguess = int(input("Adivinhe o número secreto: "))
    if iguess == secret_number:
        print("Congrats, you win ")
        break
    else:
        if iguess > secret_number:
            print("The secret number is lower than: ", iguess)
        else:
            print("The secret number is higher than: ", iguess)
    tryit += 1
if tryit > 3:
    print("You lost")
    print("The secret number was: ", secret_number)