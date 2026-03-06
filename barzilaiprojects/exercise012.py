no_vogals_word = ""
word_user = input("Enter some Word: ")
word_user = word_user.upper()
for letter in word_user:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        no_vogals_word += letter

print(no_vogals_word)