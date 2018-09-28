# Problem 2


"""
Mystery

This script prints the range of numbers you ask it to in order and then in again in reverse.

Due:9/21/18
Author: <Saby Cortez>
"""

# -----------------------------------------------------
# Question 2: Mystery script. Figure out what this is doing and annotate it


userNum = int(input("How high should I count? "))
# asks user how high they want it to count
for count in range(userNum):
    # Creates a loop of numbers to count
    print(count + 1)
    # Prints the numbers +1 so it's inclusive
print("---")
# Makes space between counts
for count in range(userNum, 0, -1):
    # Tells it to go in reverse order
    print(count)
    # Prints reverse count
print("Done!")
# Announces that it's done
