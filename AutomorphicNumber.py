'''
Automorphic number :- An automorphic number is a number whose square "ends" in the same digits as the number itself. For example, 5^2 = 25, ends with 5
 6^2= 36, ends with 6
 Write a program to check if a given number is a Automorphic number or not
 Bonus :- After being successful in making the above code.
 Try to find automorphic numbers in a range
 Example :-
 Input = 6
 Output = 1,5,6
'''
n = int(input("Enter number : "))

if n**2%10 == n:
    print(n," is Automorphic")
else:
    print(n," IS NOT")

lis = list(filter(lambda x: x**2%10==x,range(1,n)))
print(lis)
