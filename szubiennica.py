#Uworz gre, w ktorej komputer wybiera losow slowo, ktore gracz musi odgadnac. Komputer informuje gracza, ile liter znajduje sie w wybranym slowie. Nastepnie gracz otrzymuje piec szans na zadanie pytania, czy jakas litera jest zawarta w tym slowie. Komputer moze odpowiedziec tylko tak lub nie. potem gracz musi odgadnac slowo.
import random

#tworze zbior hasel:
slownik = ("niezapominajka", "zebra", "ksiazka", "grecja")

#losuje haslo:
haslo = random.choice(slownik)
prawidlowe_haslo = haslo
dlugosc = len(haslo)

#zasady gry:
print("Witaj w grze szubienica. Zgadnij, jakie haslo wylosowal komputer.\nZanim to zrobisz, mozesz 5 razy zapytac, czy wybrana przez Ciebie litera wystepuje w hasle. Do dziela!")
print("\nHaslo ma " + str(dlugosc) + " znakow: " + dlugosc * "_")

#zgadywanie liter:
zgadniete = []
for odpowiedz in range(5):
    litera = raw_input("Czy w hasle wystepuje litera: ")
    if litera.lower() not in haslo:
        print("NIE")
    elif litera.lower() in haslo:
        print("TAK")
        zgadniete.append(litera)

print("Odgadles nastepujace litery: ")
print(zgadniete)

#odgadniecie hasla:
print('Sprobuj odgadnac haslo:')
zgaduj = raw_input()

if zgaduj == prawidlowe_haslo:
    print("Gratulacje, udalo Ci sie!")
else:
    print("Bledne haslo. Prawidlowa odpowiedz to: " + str(prawidlowe_haslo))
