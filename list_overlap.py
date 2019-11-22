#Take two lists, say for example these two:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#list(set(a).intersection(set(b)))
new_list = []
for element in a:
    if element in b:
        new_list.append(element)

print(new_list)

same_values = set(a) & set(b)
print same_values

for k in a:
    for v in b:
        if k == v:
            print(k)

# Randomly generate two lists to test this
import random

lista1 = [random.randrange(1, 50, 1) for i in range(7)]
print ("lista1 : " +  str(lista1))

lista2 = [random.randrange(1, 50, 1) for i in range(10)]
print ("Lista2 : " +  str(lista2))

random_list = []
for element in lista1:
    if element in lista2:
        random_list.append(element)
print("Wspolne elementy obu list to: " + str(random_list))
