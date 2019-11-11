def print_dict(slownik):
    for key in samolot:
        print("{0}:{1}".format(key, slownik[key])
if __name__== "__main__":
    samolot = {'name': 'boeing', 'przebieg': 10000, 'type': 'pasazerski'}
    print_dict(samolot)
