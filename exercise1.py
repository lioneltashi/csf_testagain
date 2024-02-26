r = int(input("Please enter your age:"))
e = input("Are you a student? (yes/no):")
if (r <= 12 or (r >= 13 and r <= 18) and e == "yes"):
    print("You get a discount")
else:
    print("Sorry you are not eligible")
