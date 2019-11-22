# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

liczba = input("Wprowadz liczbe: ")

def znajdzDzielniki(liczba):
    dzielniki = []
    for dzielnik in range(1, liczba+1):
        if liczba % dzielnik == 0:
            dzielniki.append(dzielnik)
    print(dzielniki)
    return dzielniki


znajdzDzielniki(int(liczba))


#for liczba in range(1, liczba+1):
    #print(str(number) + " ma dzielniki " + str(znajdzDzielniki(number)))
    #slownik[liczba] = znajdzDzielniki(liczba)

#print(slownik)
