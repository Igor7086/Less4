# C. fix_start

def fix_start(s):
    ss = s[0]
    for i in range(len(s)-1):
        if s[i+1] in ss:
            ss += '*'
        else:
            ss += s[i+1]
    return ss


print(fix_start('qweeertyqwe'))