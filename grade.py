while True:
    score = int(input("Score:   "))
    if score > 100 or score < 0:
        print("Please input a valid number")
        continue
    elif score >= 90:
        print("Grade is A")
        break
    elif score >= 80:
        print("Grade is B")
        break
    elif score >= 70:
        print("Grade is C")
        break
    elif score >= 60:
        print("Grade is D")
        break
    elif score >= 50:
        print("Grade is E")
        break
    else:
        print("Grade is F")
        break