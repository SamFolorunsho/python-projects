def square(n):
    return pow(n, 3)
while True:
 x = int(input("What's x?   "))
 if x == 0:
    print("The inserted number will give an undefined answer...please give a different input")
    continue
 else:
   print(f"x squared is {square(x):,}")
   break