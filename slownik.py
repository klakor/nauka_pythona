samolot = {'name': 'boeing',
        'przebieg': 10000,
        'typ': 'pasazerski'}

#in python3 samolot.items()
for key, value in samolot.items():
    print("{0} : {1}".format(key, value))
print(samolot['name'] + " jest samolotem " + samolot['typ'] + "m.")

#
for key in samolot:
    print("{0}:{1}".format(key, value))
