print("Break Command: ")
for i in range(1, 6):
    if i == 3:
        break
    print("At the loop:", i)
print("Out of the loop")
print("\nContinue Command: ")
for i in range(1, 6):
    if i == 3:
        continue
    print("At the loop", i)
print("Out of the game")