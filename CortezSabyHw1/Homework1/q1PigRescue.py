# Problem 1


"""
Pig Rescue
This code asks for the amount of space the user has and returns how many pigs they can adopt.
Due: 9/21/18
Author: Saby Cortez
"""

# -----------------------------------------------------
# Question 1: Put your script for the pot-bellied pig problem here
length = int(input("How many feet long is your pig pen?"))
width = int(input("How many feet wide is your pig pen?"))
ppspace = length * width
pigs = ppspace//256
print("Congrats! With your space you can adopt", pigs, "pigs!")
