def scramble(s1, s2):
    if len(s1) < len(s2):
        False

    for d in s2:
        if d not in s1:
            return False

    dct2 = {x: s2.count(x) for x in s2}

    for d in dct2:
        if dct1[d] < s2.count(d):
            return False
    return True

print(scramble('sclzvsvbivdorip', 'spizpzyheaxhlamyy'))
