#! /usr/bin/python

samochody = ["syrena", "polonez"]
print(samochody[0])
print(samochody[1])

for s in samochody:
    print(s)

print("Numery samochodow w katalogu to:")
for idx in range(len(samochody)):
    print("idx: " + str(idx) + " : " + samochody[idx])
