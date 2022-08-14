def card_number(card):
    return '*' * (len(card)-4) + card[-4:]
print(card_number('1111222233334445'))