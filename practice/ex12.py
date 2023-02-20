from random import randrange

# Get two numbers from the user and convert them to integer
start = int(input("Enter the lower bound:  "))
stop = int(input("Enter the upper bound: "))

# select a random number
rand_nr = randrange(start, stop, 1)

print(rand_nr)
