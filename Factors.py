'''Factors = write a program which ask the user to input an integer and return the factors of that number without that number
 Input = 6
 Output = 1,2,3
'''
from functools import reduce
my_input = int(input("Enter a number :\n"))

factors = []

for i in range(1,my_input):
    if my_input%i == 0:
        factors.append(i)

print("Factors of {0} are {1}".format(my_input,factors))

factors = []
def factor(x):
    if x == 0:
        return factors
    else:
        if my_input % x == 0:
            factors.append(x)
        return factor(x-1)

print("Factors of {0} are {1}".format(my_input,factor(my_input-1)))

'''CODE for PERFECT NUMBER'''
sum = reduce(lambda x,y: x+y, factors)
if sum == my_input:
    print("{0} is Perfect number ".format(my_input))
else:
    print("NOT PERFECT NUMBER")
