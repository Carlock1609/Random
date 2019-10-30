#! python

def filtered():
    items = [
        ("Product1", 10),
        ("Product2", 9),
        ("Product3", 12),
    ]

    filtered = list(filter(lambda item: item[1] >= 10, items))
    print(filtered)
# filtered()

def mapping():
    items = [
        ("Product1", 10),
        ("Product2", 9),
        ("Product3", 12),
    ]

    prices = list(map(lambda item: item[1], items))
    print(prices)
# mapping()
