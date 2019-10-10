"""
3)	У вас есть список, в котором могут быть разные типы данных.
Создайте новый список только чисел из этого списка.
"""

def check_num(*args):
    sp_num = [i for i in args if type(i) == int or type(i) == float]
    return sp_num


if __name__ == "__main__":
    print(check_num(23, 'less', 877, {2: 'how'}, [], 0, 'what', 3.4, -33, -33))
