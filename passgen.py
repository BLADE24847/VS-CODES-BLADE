import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
length = int(input("Enter length of password: "))

password = ""

for i in range(length):
    password += random.choice(characters)

print("Your random password is:", password)
