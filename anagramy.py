import random
slownik = ("onomatopeja", "oksymoron", "tezaurus", "mastodont", "parabola")

slowo = random.choice(slownik)
poprawna_odp = slowo

anagram = ""
while slowo:
  pozycja = random.randrange(len(slowo))
  anagram += slowo[pozycja]
  slowo = slowo[:pozycja] + slowo[(pozycja + 1):]

print("Witaj w programie anagramy.\nSprobuj odgadnac ukryte slowo")
print("\nAby zakonczyc zgadywanie, nacisnij klawisz Enter bez podawania odpowiedzi.")
print("")
print("Ukryte slowo to: " + anagram)

odpowiedz = raw_input("Jaka jest Twoja odpowiedz? ")

while odpowiedz != poprawna_odp and odpowiedz != "":
  if odpowiedz != poprawna_odp:
    print("Bledna odpowiedz. Sprobuj jeszcze raz")
    odpowiedz = input()

if odpowiedz == poprawna_odp:
  print("Gratulacje, Twoja odpowiedz jest prawidlowa.")
