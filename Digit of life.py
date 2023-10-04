inpt = input("Key in your birthdate: ")
inpt = list(inpt)
final = 10
for a in range(0, len(inpt)):
    inpt[a] = int(inpt[a])
final = sum(inpt)
while final > 9:
    inpt = str(final)
    inpt = list(inpt)
    for a in range(0, len(inpt)):
        inpt[a] = int(inpt[a])
    final = sum(inpt)
print(final)
