#number = input("Wprowadz liczbe: ")

def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

for number in range(1, 100):
    if isEven(number):
        print(str(number) + " to jest liczba parzysta")
    #else:
        #print(str(number) + " nie jest liczba pierwsza")
