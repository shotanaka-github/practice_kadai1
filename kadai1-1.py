for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("だいがく爆破したい")
    elif i % 3 == 0:
        print("勉強したい")
    elif i % 5 == 0:
        print("就活したい")
    else:
        print(i)
