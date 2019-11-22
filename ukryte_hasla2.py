import getpass

print("Witaj na forum geniusze IT. Aby sie zalogowac, podaj nazwe uzytkownika i haslo. Mozesz tez zalogowac sie jako gosc (haslo: gosc).")
uzytkownik = raw_input("Wprowadz nazwe uzytkownika: ")
uzytkownik1 = uzytkownik.lower()
haslo = getpass.getpass("Wprowadz haslo:")
haslo1 = haslo.lower()
dlugosc = len(haslo1)
print("Wprowadz haslo: " + dlugosc * "*" )
print("_" * 40)

slownik = {"bgates": "microsoft", "emusk": "tesla", "sjobs":"apple"}

if uzytkownik1 in slownik:
    if haslo1 == slownik[uzytkownik1]:
        print("Witaj " + str(uzytkownik1) + ", zalogowales sie.")
    else:
        print("Nieprawidlowe haslo.")
elif uzytkownik1 == "gosc" and haslo1 == "gosc":
    print("Witaj, zalogowales sie jako gosc.")
else:
    print("Brak uzytkownika " + str(uzytkownik1) + " w bazie danych. Zarejestruj sie.")
