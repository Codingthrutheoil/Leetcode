inpt = input("Sentence: ")
while inpt == "":
    inpt = input("Please type something!: ")
while True:
    try:
        shift_val = input("Shift value(1-25): ")
        shift_val = int(shift_val)
        while int(shift_val) < 1 or int(shift_val) > 25:
            shift_val = int(input("Only numbers from 1-25!: "))
        else:
            break
    except:
        print("Input error. Key in numbers only(1-25)!")

final_word = ""
for a in inpt:
    if a.islower():
        a = ord(a)
        if a + shift_val > 122:
            a += shift_val
            a -= 122
            a += 96
        else:
            a += shift_val
    elif a.isupper():
        a = ord(a)
        if a + shift_val > 90:
            a += shift_val
            a -= 90
            a += 64
        else:
            a += shift_val
    elif a.isdigit():
        final_word += a
        continue
    elif a.isspace():
        final_word += a
        continue
    encrypted_word = chr(a)
    final_word += encrypted_word
print(final_word)