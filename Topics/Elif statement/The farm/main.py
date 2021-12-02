balance = int(input())
if balance < 23:
    print(None)
elif balance < 678:
    if balance // 23 == 1:
        print(f"{balance // 23} chicken")
    else:
        print(f"{balance // 23} chickens")
elif balance < 1296:
    if balance // 678 == 1:
        print(f"{balance // 678} goat")
    else:
        print(f"{balance // 678} goats")
elif balance < 3848:
    if balance // 1296 == 1:
        print(f"{balance // 1296} pig")
    else:
        print(f"{balance // 1296} pigs")
elif balance < 6769:
    print(f"{balance // 3848} cow")
else:
    print(f"{balance // 6769} sheep")
