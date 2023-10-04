inpt_1 = sorted(((input("Please key in the first phrase: ")).lower()).replace(" ",""))
inpt_2 = ((input("Please key in the second phrase: ")).lower()).replace(" ","")
checker = []
for a in inpt_1:
    checker.append(inpt_2.find(a))
if -1 in checker:
    print("No")
else:
    print("Yes")