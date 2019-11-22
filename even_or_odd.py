#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

liczba = input("Wprowadz liczbe: ")

def parzysta(liczba):
    if liczba % 2 == 0:
        print(str(liczba) + " - ta liczba jest parzysta.")

    else:
        print(str(liczba) + " - ta liczba jest nieparzysta")

parzysta(liczba)

# If the number is a multiple of 4, print out a different message.
if liczba % 4 == 0:
    print("Dzielnikiem " + str(liczba) + " jest 4.")

#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

numer = input("Wprowadz liczbe: ")
dzielnik = input("Wprowadz nastepna liczbe: ")

def dzielenie(numer):
    if numer % dzielnik == 0:
        print(str(numer) + " dzieli sie bez reszty przez " + str(dzielnik) + ".")
    else:
        print(str(numer) + " dzielony przez " + str(dzielnik) + "daje wynik " + str(numer // dzielnik) + " oraz reszte: " + str(numer % dzielnik) + ".")

dzielenie(liczba)
