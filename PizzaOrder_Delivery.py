print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#to do: Work out how much they need to pay based on their size choices?
bill = 0
if size == "S" or size=="s":
    bill+=15
elif size=="M" or size=="m":
    bill +=20
elif size=="L" or size=="l":
    bill +=25
else:
    print("You typed the wrong size.")

#to-do: work out on how much to add to their bill based on their pepperoni choice.
if pepperoni == "Y" or pepperoni=="y":
    if size == "S" or size=="s":
        bill +=2
    else:
        bill +=3

#to-do: work out on their final amount based on whether if they do not want extra-cheese
if extra_cheese == "Y" or extra_cheese =="y":
    bill += 1
print(f"Your final bill is: ${bill}")
