"""
5)	У вас есть словарь – характеристик человека.
Ключи например: “name”, “surname”, “age”, “position”, “address”, “skills”.
- Сгенерируйте новый словарь с такими же ключами, а в значениях типы значений.
- Сгенерируйте новый словарь с только парами ключ-значение, если значение исходного
словаря было строкой. Значения нового словаря должны быть переведены
в нижний регистр и удалены всё небуквенные символы из них.
"""
who = {"name": "Bob", "surname": "Black", "age": 45, "position": "boss", "address": "BakerStreet-13", "salary$": 2500}
who_keys = who.keys()
who_values = who.values()

who_values_type = [type(i) for i in who_values]
who_types = dict(zip(who_keys, who_values_type))
print(who_types)

who_string = {v: k.lower().strip('1234567890-') for v, k in who.items() if (type(k) is not int)}

print(who_string)
