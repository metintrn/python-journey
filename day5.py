#password generator
import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=["0","1","2","3","4","5","6","7","8","9"]
symbols=["!","#","%","&","(",")","*","+"]
print("welcome to pyPassword generator")
nr_letters=int(input("How many letters would you like in your letters?\n"))
nr_symbols=int(input("How many symbols  would you like?\n"))
nr_numbers=int(input("How many numbers would you like\n"))

passwor_list=[]
for chaar in range(0,nr_letters):
    passwor_list.append(random.choice(nr_letters))

for char in range(0,nr_symbols):
    passwor_list.append(random.choice(symbols))

for char in range(0,nr_numbers):
    passwor_list.append(random.choice(numbers))


random.shuffle(passwor_list)
password=""
for char in passwor_list:
    password+=passwor_list
    
print(f" your password : {password}")

#This Python program generates a random password using letters, numbers, and symbols based on user input.
#It uses lists, loops, and randomization to create a secure password.
