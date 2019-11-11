plik = open("cw_samochody.txt", "w")

samochody = ['syrena', 'polonez', 'fiat', 'kia']
ilosc_drzwi = [3, 5, 5, 5]

for idx in range(len(samochody)):
    plik.write('\nindeks: ' + str(idx+1) + ': ' + samochody[idx] + ' - ')
    plik.write(samochody[idx] + ' ma ilosc drzwi ' + str(ilosc_drzwi[idx]))

plik.close()
