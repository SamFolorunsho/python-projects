while True:
   x = int(input("What's x?   "))
   def is_even(n):
        return n % 2 == 0
   if x <= 0:
    continue
   elif is_even(x):
        print("Even number!!!")
        break
   else:
        print("Odd!!!")
        break