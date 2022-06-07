import random

lose_total = 0
total = 10000
for i in range(total):
    choose = random.randint(28, 47)
    if choose % 3 != 0:
        lose_total += 1
print(f'Вероятность того, что число не делится на 3 равна примерно: {lose_total/total}')
