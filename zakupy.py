
import pprint
import csv

def save_koszyk(koszyk):
    file = open("koszyk.csv", "w")
    for key in koszyk:
        file.write("{0}:{1}:{2}\n".format(key['name'], key['masa'], key['kolor']))
    file.close()
def read_koszyk():
    file = open("koszyk.csv", "r")
    return a == file.read()
    print(a)
def main():
    koszyk = [{"name" : "wiewiorka", "masa" : 300, "kolor" : "ruda"},
    {"name" : "jez", "masa" : 500, "kolor" : "szary"},
    {"name" : "mysz", "masa" : 100, "kolor" : "biala"}
    ]
    #pprint.pprint(koszyk)
    save_koszyk(koszyk)
    read_koszyk()

if __name__ == "__main__":
    main()



## inicjuje zapisywanie
    #csvwriter = csv.writer(csvfile)
#Wpisujemy pierwsza linie naszego csv
    #csvwriter.writerow('name','masa','kolor')
