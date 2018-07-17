'''list overlap :- Take two lists, say for example these two:
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
 and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
  Make sure your program works on two lists of different sizes.

  o/P [1, 2, 3, 5, 8, 13]'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
''' NORMAL---
for i in a:
    for j in b:
        if i == j and not c.__contains__(i):
            c.append(i)      
'''

'''Using List Comprahension'''
c = [ x for x in set(a) for y in b if x==y ]
print("List Comprahension: ",c)

'''Using Lamda'''
c = filter(lambda x: a.__contains__(x), b)
print("Lambda  ",list(c))


