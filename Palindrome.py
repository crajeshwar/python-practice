'''palindrome :- Palindromic number is a number that is the same when written forwards or backwards.
 Create a program that takes a number as input and return whether the number is palindromic, or not. '''
my_str =input("Enter a number")
new_str = ""
n = int(my_str)

while n/10:
    new_str += str(n%10)
    n=int(n/10)

if int(my_str)==int(new_str):
    print(my_str," is Palindromic")
else:
    print("NOT Palindromic")

