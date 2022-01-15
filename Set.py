# 20CE029 Misari Gami
# GitHub repository link : https://github.com/MisariGami/Pra2/blob/main/Set.py

# a. Write a Python program to add member(s) in a set and clear a set
# Creating a Set
set1 = set()
print("Initial blank Set: ",set1)
# add menbers using add method
for i in range(1,8):
    set1.add(i)
print("Set after adding element")
print(set1)
# remove element using remove method
set1.remove(3)
# remove element using Discard method
set1.discard(5)
print("Set after removing element 3 and 5")
print(set1)

# b. Write a Python program to remove an item from a set if it is present in the set.
set1 = {1,2,3,4,5}
# discard element
set1.discard(3)
set1.discard(7)
print(set1)

# c. Write a Python program to create an intersection, Union, difference of sets.
# sets
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
# intersection
print("Intersection :", A & B)
# union
print("Union : ", A | B)
# difference
print("Difference :", A - B)

# d. Write a Python program to find maximum and the minimum value in a set.
set1 = {-32,23,4,43,51,6,21,67,94}
# minimum value
print(min(set1))
# maximum value
print(max(set1))

# e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
# list
list = [1,2,7,7,7,8]
def most_frequent(list):
    count = 0
    n = list[0]
    for i in list:
        cur_frequency = list.count(i)
        if(cur_frequency > count):
            count = cur_frequency
            n = i 
    return n 
print("Most common element in list :",most_frequent(list))
# dictionary
d = {"name":"python", "version":8.9, "key":8.9}
list = list(d.values())
def most_frequent(list):
    count = 0
    n = list[0]
    for i in list:
        cur_frequency = list.count(i)
        if cur_frequency > count:
            count = cur_frequency
            n = i
    return n
print("Most common element in list :",most_frequent(list))
