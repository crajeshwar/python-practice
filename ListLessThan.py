a = [1, 1, 2, 3, 5, 8, 3, 4, 13, 13, 21, 34, 55, 8]

'''for i in a:
     if i <= 12:
         print(i)'''

'''Using List Comprahension'''
result_lc = [x for x in a if x <= 12]
print("list comprahension ",result_lc)


'''FILTER'''
result = filter(lambda x: x<=12, a)
print("filter ",list(result))
