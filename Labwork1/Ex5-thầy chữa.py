fav = ["white", "gray", "blue"]
color = input("Your color? ")
if color in fav:
    print("good, no black")
    print(f" position at {fav.index(color)}")
else:
    print("you're too bad")