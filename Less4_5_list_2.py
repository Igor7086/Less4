# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.


def front_x(words):
    words1 = []
    words2 = []
    for i in words:
        if i[0] == 'x':
            words1.append(i)
        else:
            words2.append(i)
    words2.sort()
    return words1 + words2


print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))



