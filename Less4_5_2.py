# B. both_ends

def both_ends(s):
    if len(s)>2:
        return s[:2] + s[-2:]
    else:
        return "_"


print(both_ends('qwerty'))


