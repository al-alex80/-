import random

lose_total = 0
total = 100000
for i in range(total):
    x1 = random.randint(0, 9)
    x2 = random.randint(0, 9)
    while x1 == x2:
        x2 = random.randint(0, 9)
    if int(str(x1) + str(x2)) % 18 == 0:
        lose_total += 1
print(f'вероятность того, что наудачу образованное с помощью двух данных карточек число делится на 18 равно примерно: {lose_total / total}')
