def calculate_vat(netto):
    vat = float(netto * 23)/100
    return vat

if __name__ == "__main__":
    vat = calculate_vat(1000)
    print("{0}".format(vat))
