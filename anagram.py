inpt_1 = sorted(((input("Please key in the first phrase: ")).lower()).replace(" ",""))
inpt_2 = sorted(((input("Please key in the second phrase: ")).lower()).replace(" ",""))
if inpt_1 == inpt_2:
    print("Anagrams")
else:
    print("Not anagrams")