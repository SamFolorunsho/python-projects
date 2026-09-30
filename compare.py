while True:
    x = int(input("What's x?   "))
    y = int(input("What's y?   "))
    def power(a, b):
        return a ** b

    if x!= y:
        print(f"x raised to y is {power(x, y):,}")
        break
    else:
        print("x and y are equal;   cannot run calculation")
        continue