import getpass

print("Witaj na forum geniusze IT. Aby sie zalogowac, podaj nazwe uzytkownika i haslo. Mozesz tez zalogowac sie jako gosc (haslo: gosc).")
uzytkownik = raw_input("Wprowadz nazwe uzytkownika:"")
haslo = getpass.getpass("Wprowadz haslo:")
dlugosc = len(haslo)
print("Wprowadz haslo: " + dlugosc * "*" )
print("_" * 40)

slownik = {"BGates": "microsoft", "EMusk": "tesla", "SJobs":"apple"}

if uzytkownik in slownik:
    if haslo == slownik[uzytkownik]:
        print("Witaj " + str(uzytkownik) + ", zalogowales sie.")
    else:
        print("Nieprawidlowe haslo.")
elif uzytkownik == "gosc" and haslo == "gosc":
    print("Witaj, zalogowales sie jako gosc.")
else:
    print("Brak uzytkownika " + str(uzytkownik) + " w bazie danych. Zarejestruj sie.")
