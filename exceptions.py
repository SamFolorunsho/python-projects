def main():
    y = get_number()
    print(f"x is {y}")

def get_number():
    while True:
        try:
            return int(input("What's x?   "))
        except ValueError:
            pass


main()
        