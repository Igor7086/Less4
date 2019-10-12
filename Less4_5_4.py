# D. MixUp


def mix_up(a, b):
    return b[:2] + a[2:], a[:2] + b[:2]


print(mix_up('aaaa', 'bbbb'))
