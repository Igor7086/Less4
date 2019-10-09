"""
Напишите функцию, которая удаляет все небуквенные символы внутри строки
(ограничимся латинским алфавитом).
Проверьте, что вы правильно закодили с помощью инструкции assert.

"""


def del_char(a):
    ii = []
    for i in a:
        if i.isalpha():
            ii.append(i)
    iii = ''.join(ii)
    assert iii.isalpha()
    return iii


print(del_char('Onl_yL+34ett4ers56"Here'))



