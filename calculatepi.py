"""
calculatepi.py
Author: Nick Lee
Credit: I modified the line of code that calculated e to generate an aproximate pi
Assignment: Calculate pi

Write and submit a Python program that computes an approximate value of π by calculating the following sum:

(see: https://github.com/HHS-IntroProgramming/Calculate-Pi/blob/master/README.md)

This sum approaches the true value of π as n approaches ∞.

Your program must ask the user how many terms to use in the estimate of π, how many decimal places, 
then print the estimate using that many decimal places. Exactly like this:

I will estimate pi. How many terms should I use? 100
How many decimal places should I use in the result? 7
The approximate value of pi is 3.1315929


Note: remember that the printed value of pi will be an estimate!

"""
import math
n = int(input("I will estimate pi. How many terms should I use? "))
decimal = int(input("How many decimal places should I use in the result? "))

denom = sum([(2*k+1) for k in range(0,n)])
numer = sum([((-1)**k) for k in range (0,n)])
pi = 4*(numer/denom)

# pi = 4*sum([((-1)**k)/(2*k+1) for k in range(0, n)])


print ("The approximate value of pi is {0}".format(round(pi,decimal)))
print ("The real value of pi is {0}".format(round(math.pi,decimal)))
