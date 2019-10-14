
# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.


def match_ends(words):
    return [i for i in words if len(i) >= 2 and i[0] == i[-1]]


if __name__ == '__main__':
    print(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']))
    print(match_ends(['aaa', 'be', 'abc', 'hello']))

