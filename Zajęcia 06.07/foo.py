ranks = [2, 3, 4, 5]
    suits = ['diamonds', 'clubs', 'hearts']
    # [('diamonds', 2), ('diamonds', 3)...]
    cards = []
    for s in suits:
        # diamonds, clubs, hearts
        for r in ranks:
            # 2, 3, 4, 5
            cards.append((s, r))

    cards2 = [(s, r) for s in suits for r in ranks]
    print(cards2)
    even = [x for x in range(1, 11) if x % 2 == 0]
    print(even)
    char = 'A'
    some_list = [char + str(y) for y in range(1, 11)]
    print(some_list)