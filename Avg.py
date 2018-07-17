'''Avg :- Write a program which Asks the user to input numbers separated by comas and return the average of all the numbers entered
 Input = 2,4,6,8
 Output = 5'''

    my_input = input("input numbers separated by comas")
my_list = my_input.split(",")
sum = 0

for i in my_list:
    sum += int(i)

print("Average of input list is ",int(sum/my_list.__len__()))
