#Uworz gre, w ktorej komputer wybiera losow slowo, ktore gracz musi odgadnac. Komputer informuje gracza, ile liter znajduje sie w wybranym slowie. Nastepnie gracz otrzymuje piec szans na zadanie pytania, czy jakas litera jest zawarta w tym slowie. Komputer moze odpowiedziec tylko tak lub nie. potem gracz musi odgadnac slowo.
import random

#tworze zbior hasel:
slownik = {"niezapominajka":"niebieski kwiat", "zebra":"zwierze parzystokopytne", "linijka":"do mierzenia", "ateny":"antyczne miasto", "pies":"ssak z futrem", "tulipan":"czerwony kwiat", "rzym":"antyczne miasto", "ekierka":"do mierzenia", "ksiazka":"ma strony", "wenecja":"wloskie miasto", "krakow":"polskie miasto", "warszawa":"polskie miasto", "katowice":"polskie miasto", "antylopa":"zwierze parzystokopytne", "zyrafa":"zwierze parzystokopytne"}

#losuje haslo:
haslo = random.choice(list(slownik.keys()))
prawidlowe_haslo = haslo
dlugosc = len(haslo)
podpowiedz = slownik[haslo]

#zasady gry:
print("Witaj w grze szubienica. Zgadnij, jakie haslo wylosowal komputer.\nZanim to zrobisz, mozesz 5 razy zapytac, czy wybrana przez Ciebie litera wystepuje w hasle. Uzywaj tylko pojedynczych liter! Do dziela!")
print("\nHaslo ma " + str(dlugosc) + " znakow: " + dlugosc * "_")
print("\nPodpowiedz: " + str(podpowiedz))

#zgadywanie liter:
zgadniete = []
for odpowiedz in range(5):
    litera = raw_input("Czy w hasle wystepuje litera: ")
    if litera.lower() not in haslo:
        print("     NIE")
    elif litera.lower() in haslo:
        print("     TAK")
        zgadniete.append(litera)

print("\n\nOdgadles nastepujace litery: ")
print(zgadniete)

#odgadniecie hasla:
print('\n\nSprobuj odgadnac haslo:')
zgaduj = raw_input()

if zgaduj == prawidlowe_haslo:
    print("\nGratulacje, udalo Ci sie!")
else:
    print("\nBledne haslo. Prawidlowa odpowiedz to: " + str(prawidlowe_haslo))
