samochody = ["syrena", "polonez", "fiat", "kia"]
ilosc = [3, 5, 5, 5]

for idx in range(len(samochody)):
    print("idx: " + str(idx) + " : " + samochody[idx])
    print(samochody[idx] + " ma ilosc drzwi " + str(ilosc[idx]))

samochody[-1]
samochody[1,-1]
samochody[1:]
samochody[10]
