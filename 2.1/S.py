name = str(input())
price = int(input())
weight = int(input())
money = int(input())
k = '='
m = ' '
print(f'{k * 16}Чек{k * 16}')
print(f'Товар: {m * (35 - 7 - len(name))}{name}')
print(f'Цена: {m * (35 - 17 - len(str(weight)) - len(str(price)))}{weight}кг * {price}руб/кг')
print(f'Итого: {m * (35 - 10 - len(str(weight * price)))}{weight * price}руб')
print(f'Внесено: {m * (35 - 12 - len(str(money)))}{money}руб')
print(f'Сдача: {m * (35 - 10 - len(str(money - weight * price)))}{money - weight * price}руб')
print(f'{k * 35}')
