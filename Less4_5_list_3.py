# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use sorted() function and a custom key= function to extract the last element form each tuple.

# sorted(student_tuples, key=lambda student: student[2])


def sort_last(tuples):
    return sorted(tuples, key=lambda tup: tup[-1])


print(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]))


