inpt = input("Please key in the sentence: ")
inpt = inpt.lower()
inpt = inpt.replace(" ", "")
checker = ""
for a in range(len(inpt)):
    checker += inpt[len(inpt)-a-1]
if inpt == checker:
    print("It's a palindrome")
else:
    print("It's not a palindrome")