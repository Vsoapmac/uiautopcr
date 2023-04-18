def bb(text: str, number: int, money: float, list: list):
    print(text)
    print(money * number)
    print(list + list)
    return [1, 2, 3, 4]


print(bb("1234", 1, 1.2, 12))
