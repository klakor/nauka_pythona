#wymieszane litery
#komputer wybiera losowo slowo, a potem miesza w nim litery
#Gracz powinien odgadnac pierwotne slowo

import random

#utworzenie sekwencji slow do wyboru

WORDS = ("uczestnik", "zabawa")

#wybierz losowo jedno slowo z sekwencji

word = random.choice(WORDS)

#utworzenie zmiennej w celu pozniejszej weryfikacji poprawnosci

correct = word

#utworzenie 'pomieszanej' wersji slowa

jumble =""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

#rozpocznij gre

print(
    """
                Witaj w grze 'wymieszane litery'!

        Uporzadkuj litery, aby odtworzyc prawidlowe slowo.
        (Aby zakonczyc zgadywanie, nacisnij klawisz Enter bez podawania odpowiedzi.)
                                                                            """
)

print("Zgadnij, jakie to slowo:", jumble)

#uzyskanie odpowiedzi gracza


quess = input("\nTwoja odpowiedz to: ")
while quess != correct and quess != "":
    print("Niestety to nie to slowo")

    if quess != correct:
        quess = input("\nTwoja odpowiedz to: ")


if quess == correct:
        print("Zgadza sie! Zgadles! \n")


print ("Dziekuje za udzial w zabawie!")
input("\n\nAby zakonczyc program nacisnij klawisz Enter")
