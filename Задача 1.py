from math import factorial

card_deck = 36
player = 3
count = int(factorial(card_deck) / factorial(card_deck - player))
print(f'{count} способов раздачи по одной карте из колоды 36 карт на троих игроков')
