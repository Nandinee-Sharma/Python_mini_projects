import random
print("Welcome to the password generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
no_of_letters = int(input("How many letters would you like in your password? "))
no_of_symbols = int(input("How many symbols would you like in your password? "))
no_of_numbers = int(input("How many numbers would you like in your password? "))

#easy
password = []
for char in range(0,no_of_letters):
    password.append(random.choice(letters))
for char in range(0,no_of_letters):
    password.append(random.choice(symbols))
for char in range(0,no_of_numbers):
    password.append(random.choice(numbers))
random.shuffle(password) #this prints a list containing characters of password
password_final = ""
#now converting the list into string
for char in password:
    password_final +=char
print(f"Your password is: {password_final}" )
