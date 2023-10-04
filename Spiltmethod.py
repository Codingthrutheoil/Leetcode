def mysplit(strng):
    b = ""
    final = []
    if strng.isspace():
        return final
    strng = strng + " "
    for a in strng:
        if a.isspace():
            final.append(b)
            b = ""
            continue
        b = b + a
    for a in final:
        if a == "":
            final.remove(a)
    return final