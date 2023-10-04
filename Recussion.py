def fun(a):
    if a > 35:
        return 3
    return a + fun(a + 3)

print(fun(25))
