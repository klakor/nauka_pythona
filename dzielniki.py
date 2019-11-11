
def znajdzDzielniki(number):
    dzielniki = []
    for dzielnik in range(1, number+1):
        if number % dzielnik == 0:
            dzielniki.append(dzielnik)
    return dzielniki

slownik_dzielniki = {}

for number in range(1, 10):
    #print(str(number) + " ma dzielniki " + str(znajdzDzielniki(number)))
    slownik_dzielniki[number] = znajdzDzielniki(number)

print(slownik_dzielniki)

for key in slownik_dzielniki:
    print(str(key) + " ma dzielniki: " + str(slownik_dzielniki[key]))
