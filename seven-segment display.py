lst = [[0 for a in range(5)] for i in range(10)]
lst[0][0] = "###"
lst[0][1] = "# #"
lst[0][2] = "# #"
lst[0][3] = "# #"
lst[0][4] = "###"
lst[1][0] = "#"
lst[1][1] = "#"
lst[1][2] = "#"
lst[1][3] = "#"
lst[1][4] = "#"
lst[2][0] = "###"
lst[2][1] = "  #"
lst[2][2] = "###"
lst[2][3] = "#  "
lst[2][4] = "###"
lst[3][0] = "###"
lst[3][1] = "  #"
lst[3][2] = "###"
lst[3][3] = "  #"
lst[3][4] = "###"
lst[4][0] = "# #"
lst[4][1] = "# #"
lst[4][2] = "###"
lst[4][3] = "  #"
lst[4][4] = "  #"
lst[5][0] = "###"
lst[5][1] = "#  "
lst[5][2] = "###"
lst[5][3] = "  #"
lst[5][4] = "###"
lst[6][0] = "###"
lst[6][1] = "#  "
lst[6][2] = "###"
lst[6][3] = "# #"
lst[6][4] = "###"
lst[7][0] = "###"
lst[7][1] = "  #"
lst[7][2] = "  #"
lst[7][3] = "  #"
lst[7][4] = "  #"
lst[8][0] = "###"
lst[8][1] = "# #"
lst[8][2] = "###"
lst[8][3] = "# #"
lst[8][4] = "###"
lst[9][0] = "###"
lst[9][1] = "# #"
lst[9][2] = "###"
lst[9][3] = "  #"
lst[9][4] = "###"
a = 0
str_inpt = input("Please input your number: ")
sepstr_list = list(str_inpt)
sepint_list = []
for a in sepstr_list:
    a = int(a)
    sepint_list.append(a)
final_printlist = [[0 for i in range(len(sepint_list))] for a in range(5)]
for a in range(5):
    final_printlist[a] = (lst[sepint_list[0]][a])
    final_printlist[a] += " "
del sepint_list[0]
while len(sepint_list) != 0:
    for i in range(5):
        final_printlist[i] += lst[sepint_list[0]][i]
        final_printlist[i] += " "
    i = 0
    del sepint_list[i]
for i in range(5):
    print(final_printlist[i])