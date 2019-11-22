#Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

lista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for element in lista:
    if element < 5:
        print(element)

#Instead of printing the elements one by one, make a new list that has all the elements less than 10 from this list in it and print out this new list.

def znajdzElement(element):
    nowa_lista = []
    for element in lista:
        if element < 10:
            nowa_lista.append(element)
    print(nowa_lista)

znajdzElement(element)
# Write this in one line of Python.



#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
numerek = input("wprowadz liczbe: ")

def znajdzElement(element):
    nowa_lista = []
    for element in lista:
        if element < numerek:
            nowa_lista.append(element)
    print("Te liczby ze zbioru sa mniejsze niz podany przez Ciebie numer: " + str(nowa_lista))

znajdzElement(element)
