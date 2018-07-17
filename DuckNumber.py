'''
Duck number :- A Duck number is a number which has zeroes present in it, but there should be no zero present in the beginning of the number.
For example 3210, 7056, 8430709 are all duck numbers whereas 08237, 04309 are not.
'''
my_input = input("Enter number : ")

if not my_input.startswith("0") and my_input.__contains__("0"):
    print(my_input," Is Duck Number")
else:
    print(my_input," is NOT")

n=int(my_input)
lis = []
while n/10:
    lis.append(int(n%10))
    n=int(n/10)
print(lis)

if lis.__contains__(0) and not my_input.startswith("0"):
    print(my_input," Is Duck Number")
else:
    print(my_input," NOT Number")
