#! /usr/bin/python

print("Wprowadz haslo:")
haslo = input()

gwiazdki = (len(haslo) -2) * "*"
secret = haslo[0] + gwiazdki + haslo[-1]
print(secret)

if len(haslo) < 1:
    print("You did not pass a password.")
if len(haslo) < 5:
    print("Your password is too short.")
elif len(haslo) >= 6:
    print("your password is correct.")
