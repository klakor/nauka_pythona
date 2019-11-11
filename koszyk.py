def main():
    koszyk = [
                {"nazwa" : "wiewiorka", "masa" : 300, "kolor" : "ruda"},
                {"nazwa" : "jez", "masa" : 500, "kolor" : "szary"},
                {"nazwa" : "mysz", "masa" : 100, "kolor" : "biala"}]

    plik = open("zakupy.csv", "w")
    for pozycja in koszyk:
        for key in ["nazwa", "masa", "kolor"]:
            plik.write("{0} ".format(pozycja[key]))
        plik.write('\n')

    plik.close()

if __name__ == "__main__":
    main()
