#! /usr/bin/python

marka = "Peugeot"
model = 306
ilosc_drzwi = 5
pojemnosc = 1.3

marka_up = marka.upper()
marka_low = marka.lower()

print("Samochod " + marka + " " + str(model) + " ma " + str(ilosc_drzwi) + " drzwi.")
print(marka_up)
print(marka_low)
print("Przedliftowa wersja ma silnik o pojemnosci " + str(pojemnosc) + " litra, a poliftowa wersja ma silnik o pojemnosci " + str(pojemnosc *1.23) + " litra")
