'''Mobile no generator = Write a program which ask the user to input an integer and return a mobile random number starting with that integer
 Input = 7
 Output = 7538686294'''
import  random
my_input = int(input("input number you want to start with"))

print(random.sample(range(my_input*100000000,(my_input+1)*100000000),1))
