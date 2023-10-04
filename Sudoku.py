inpt = ("""295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672""").replace("\n", "")

array_row = [[0 for i in range(9)] for a in range(9)]
array_column = [[0 for i in range(9)] for a in range(9)]
array_box = [[0 for i in range(9)] for a in range(9)]

# row finder
for b in range(9):
    c = 0
    for a in inpt:
        a = int(a)
        array_row[b][c] = a
        c += 1
        if c == 9:
            inpt = inpt[9:]
            break

# column finder
for b in range(9):
    for a in range(9):
        array_column[b][a] = array_row[a][b]

# box finder
for a in range(9):
    c = 0
    d = 0
    for b in range(9):
        array_box[a][b] = array_row[d][c]
        c += 1
        if c == 3:
            d += 1
            c = 0

def fun(test_range):
    tester = []
    for a in range(9):
        tester = test_range[a][:]
        for b in range(1, 10):
            if b not in tester:
                return False
    return True

if fun(array_row) == True and fun(array_column) == True and fun(array_box) == True:
    print("Correct")
else:
    print("Wrong")