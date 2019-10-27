
import pprint
import csv

def save_koszyk(koszyk):
    for key in koszyk:
        file = open("koszyk.csv", "w")
        file.write("{0}:{1}".format(key, koszyk))
        file.close()

def main():
    koszyk = [{"name" : "wiewiorka", "masa" : 300, "kolor" : "ruda"},
    {"name" : "jez", "masa" : 500, "kolor" : "szary"},
    {"name" : "mysz", "masa" : 100, "kolor" : "biala"}
    ]
    pprint.pprint(koszyk)
    save_koszyk(koszyk)

if __name__ == "__main__":
    main()
with open('koszyk.csv', 'w', encoding='utf-8') as csvfile:
# inicjuje zapisywanie
    csvwriter = csv.writer(csvfile)
#Wpisujemy pierwsza linie naszego csv
    csvwriter.writerow('name','masa','kolor')
