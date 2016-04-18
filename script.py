# testing demo stuff can go here!

# def say_hello(name):
#     if name.lower() == "emma":
#         print("Ohhhh, Emmachka. :/")
#     else:
#         print("Hello "+name)
#         print("Nice to meet you!")

# say_hello("Joel")
# say_hello("class")
# say_hello("Emma")
# say_hello("Dave")

# name = "Alice" # global variable 'name'

# def say_hello(name): #local variable 'name'
#     name = name #assign to self (redundant!!!)
#     print("Hi "+name) #using local variable

# say_hello("Bob") #param (value) assigned to LOCAL variable

# print(name) #using GLOBAL variable

# def square(number):
#     result = number*number
#     return result

# def triple(number):
#     return number*3

# #remember to give the result a label!
# x2 = square(6)
# x3 = triple(8)

# print(x2)
# print(x3)

# def say_hello(name):
#     print("Hello "+name)

# greeting = say_hello(name)
# print(greeting) #error! no value has been returned to be stored in greeting

# count = 5
# while count > 0:
#     print(count)
#     count = count - 1

# print("Blast off!")

# flip a coin until it shows up heads

# import random # for random numbers

# still_flipping = True
# while still_flipping:
#     flip = random.randint(0,1)
#     if flip == 0:
#         flip = "Heads"
#     else:
#         flip = "Tails"
#     print(flip)
#     if flip == "Heads":
#         still_flipping = False

# input validation
# returns a user-inputted number between min and max

# def input_number(min, max):
#     valid = False
#     while(not valid):
#         number = int(input("Pick a number between "+str(min)+" and "+str(max)+": "))
#         if(min <= number <= max):
#             return number
#             valid = True
#         else:
#             print("Invalid number. Please enter a valid number.")

# # call function and print result
# print(input_number(1,5))

# for count in range(0,101,10):
#     print(count)

# for count in range(5):
#     print(5 - count)
# print("Blast off! ZOOM!")

line = "To be or not to be"
words = line.split(' ')

for word in words:
    print(word)

for letter in line:
    print(letter)