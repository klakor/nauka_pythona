samolot = {"name": "boeing",
            "przebieg": 10000,
            "type": "pasazerski"}
for key, value in samolot.items():
    print("{0}:{1}".format(key, value))

for key in samolot:
    print("{0}:{1}".format(key, samolot[key]))
